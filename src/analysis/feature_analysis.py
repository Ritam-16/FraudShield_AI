import matplotlib.pyplot as plt
import pandas as pd

def correlation_matrix(df):

    numeric_df = df.select_dtypes(include=["int64", "float64"])

    correlation = numeric_df.corr()

    print(correlation["is_fraud"].sort_values(ascending=False))


def fraud_statistics(df):

    fraud = df[df["is_fraud"] == 1]

    normal = df[df["is_fraud"] == 0]

    print("\nFraud Transactions\n")

    print(fraud.describe())

    print("\nNormal Transactions\n")

    print(normal.describe())


def average_amount(df):

    print(

        df.groupby("is_fraud")["amount"].mean()

    )

def average_hour(df):

    print(

        df.groupby("is_fraud")["hour"].mean()

    )

def anomaly_statistics(df):

    print(

        df.groupby("is_fraud")["anomaly_score"].mean()

    )

def feature_distribution(df):

    numeric = df.select_dtypes(include=["int64", "float64"])

    numeric.hist(

        figsize=(15,12),

        bins=30

    )

    plt.tight_layout()

    plt.show()

