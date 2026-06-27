import pandas as pd
import numpy as np


class DataPreprocessor:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    def handle_missing_values(self):

        print("\nHandling Missing Values...")

        print(self.df.isnull().sum())

        self.df.fillna("None", inplace=True)

        return self

    # --------------------------------------------------
    # Duplicate Rows
    # --------------------------------------------------

    def remove_duplicates(self):

        before = len(self.df)

        self.df.drop_duplicates(inplace=True)

        after = len(self.df)

        print(f"Removed {before - after} duplicate rows.")

        return self

    # --------------------------------------------------
    # Datetime
    # --------------------------------------------------

    def convert_datetime(self):

        self.df["transaction_time"] = pd.to_datetime(
            self.df["transaction_time"]
        )

        return self

    # --------------------------------------------------
    # Time Features
    # --------------------------------------------------

    def extract_time_features(self):

        self.df["hour"] = self.df["transaction_time"].dt.hour

        self.df["day"] = self.df["transaction_time"].dt.day

        self.df["month"] = self.df["transaction_time"].dt.month

        self.df["weekday"] = self.df["transaction_time"].dt.weekday

        self.df["is_weekend"] = (
            self.df["weekday"] >= 5
        ).astype(int)

        return self

    # --------------------------------------------------
    # Rule Feature 1
    # --------------------------------------------------

    def create_high_value(self):

        self.df["high_value"] = (
            self.df["amount"] > 100000
        ).astype(int)

        return self

    # --------------------------------------------------
    # Rule Feature 2
    # --------------------------------------------------

    def create_off_hours(self):

        self.df["off_hours"] = (
            (self.df["hour"] >= 1)
            &
            (self.df["hour"] <= 3)
        ).astype(int)

        return self

   

    # --------------------------------------------------
    # ML Feature
    # --------------------------------------------------

    def amount_log(self):

        self.df["log_amount"] = np.log1p(
            self.df["amount"]
        )

        return self

    # --------------------------------------------------
    # Remove unnecessary columns
    # --------------------------------------------------

    def drop_columns(self):

        columns = [

            "transaction_id",

            "sender_account_id",

            "receiver_account_id",

            "receiver_account_number",

            "receiver_name",

            "transaction_time",

            "transaction_hour",

            "transaction_dayofweek",

            "is_high_value",

            "is_off_hours",

            "is_repeated_amount",

            "status",

            "rule_triggered",

            "risk_level"

        ]

        self.df.drop(
            columns=columns,
            inplace=True,
            errors="ignore"
        )

        return self

    # --------------------------------------------------

    def get_dataframe(self):

        return self.df