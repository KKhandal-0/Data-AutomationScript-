import os
import logging
import polars as pl

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DynamicDataPipeline:
    def handle_missing_values(
        self, df: pl.DataFrame, strategy: str = "drop"
    ) -> pl.DataFrame:
        """Handles missing values by either dropping rows or imputing."""
        if strategy == "drop":
            logging.info("Dropping records with missing values.")
            return df.drop_nulls()

        elif strategy == "impute":
            logging.info("Imputing missing values using median/mode.")
            imputation_expressions = []
            for col in df.columns:
                if df[col].dtype == pl.String:
                    mode_series = df[col].mode()
                    fallback = mode_series[-1] if len(mode_series) > 0 else "Unknown"
                    imputation_expressions.append(pl.col(col).fill_null(fallback))
                elif df[col].dtype.is_numeric():
                    imputation_expressions.append(
                        pl.col(col).fill_null(pl.col(col).median())
                    )
                else:
                    imputation_expressions.append(pl.col(col))
            return df.with_columns(imputation_expressions)

        return df

    def handle_outliers_dynamic(self, df: pl.DataFrame) -> pl.DataFrame:
        """Automatically isolates and clips outliers for all numerical columns."""
        outlier_expressions = []
        numeric_cols = [col for col in df.columns if df[col].dtype.is_numeric()]

        for col in numeric_cols:
            q1 = df.select(pl.col(col).quantile(0.25)).item()
            q3 = df.select(pl.col(col).quantile(0.75)).item()
            iqr = q3 - q1

            # Only clip if there is genuine variance in the column
            if iqr > 0:
                outlier_expressions.append(
                    pl.col(col).clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
                )

        return df.with_columns(outlier_expressions) if outlier_expressions else df

    def run(self, input_path: str, output_path: str, strategy: str = "drop"):
        if not os.path.exists(input_path):
            logging.error(f"File not found: {input_path}")
            return

        try:
            df = pl.read_csv(input_path)
            # Fixed: Now utilizes your strategy selection block
            df_missing_handled = self.handle_missing_values(df, strategy=strategy)
            df_final = self.handle_outliers_dynamic(df_missing_handled)

            df_final.write_csv(output_path)
            logging.info(f"Successfully processed and exported to: {output_path}")
        except Exception as e:
            logging.critical(f"Pipeline failed: {str(e)}")


if __name__ == "__main__":
    pipeline = DynamicDataPipeline()
    pipeline.run(
        input_path="data/raw/raw_data.csv",
        output_path="data/processed/clean_data.csv",
        strategy="drop",  # Switch to "impute" whenever you need to toggle behavior
    )
