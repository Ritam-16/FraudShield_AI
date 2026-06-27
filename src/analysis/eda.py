import pandas as pd


def basic_info(df):
    print("=" * 60)
    print("DATASET SHAPE")
    print("=" * 60)
    print(df.shape)

    print("\n")

    print("=" * 60)
    print("COLUMN NAMES")
    print("=" * 60)
    print(df.columns.tolist())

    print("\n")

    print("=" * 60)
    print("DATA TYPES")
    print("=" * 60)
    print(df.dtypes)

    print("\n")

    print("=" * 60)
    print("FIRST 5 ROWS")
    print("=" * 60)
    print(df.head())

    print("\n")

    print("=" * 60)
    print("LAST 5 ROWS")
    print("=" * 60)
    print(df.tail())

def missing_values(df):
        print("=" * 60)
        print("MISSING VALUES")
        print("=" * 60)

        print(df.isnull().sum())

def duplicate_rows(df):

    print("=" * 60)
    print("DUPLICATE ROWS")
    print("=" * 60)

    print(df.duplicated().sum())

def statistical_summary(df):

    print("=" * 60)
    print("STATISTICAL SUMMARY")
    print("=" * 60)

    print(df.describe())

def fraud_distribution(df):

    print("=" * 60)
    print("FRAUD DISTRIBUTION")
    print("=" * 60)

    print(df["is_fraud"].value_counts())

    print("\n")

    print(df["is_fraud"].value_counts(normalize=True) * 100)