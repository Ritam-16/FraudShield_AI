from src.data_loader import load_data

from src.analysis.eda import (
    basic_info,
    duplicate_rows,
    fraud_distribution,
    missing_values,
    statistical_summary,
)

from src.analysis.visualization import (
    plot_fraud_distribution,
    amount_distribution,
    fraud_vs_amount,
)

from src.analysis.feature_analysis import (
    correlation_matrix,
    fraud_statistics,
    average_amount,
    average_hour,
    feature_distribution,
    anomaly_statistics,
)

from src.analysis.feature_importance import plot_feature_importance

from src.pipeline.preprocessing import DataPreprocessor
from src.pipeline.dataset_builder import DatasetBuilder
from src.pipeline.train_test import split_dataset

from src.models.logistic_model import train_logistic
from src.models.random_forest_model import train_random_forest
from src.models.xgboost_model import train_xgboost

from src.evaluation import evaluate_model
from src.model_utils import save_model


# Set True only when you want to perform EDA
RUN_EDA = True


def main():

    # -----------------------------
    # Load Dataset
    # -----------------------------
    df = load_data()

    # -----------------------------
    # Preprocessing
    # -----------------------------
    processor = DataPreprocessor(df)

    clean_df = (
        processor
        .handle_missing_values()
        .remove_duplicates()
        .convert_datetime()
        .extract_time_features()
        .create_high_value()
        .create_off_hours()
        .amount_log()
        .drop_columns()
        .get_dataframe()
    )

    # -----------------------------
    # Build Dataset
    # -----------------------------
    builder = DatasetBuilder(clean_df)

    X, y = builder.select_features()

    X_train, X_test, y_train, y_test = split_dataset(X, y)

    print(f"\nTraining Shape : {X_train.shape}")
    print(f"Testing Shape  : {X_test.shape}")

    print("\nTraining Labels")
    print(y_train.value_counts())

    print("\nTesting Labels")
    print(y_test.value_counts())

    # -----------------------------
    # Exploratory Data Analysis
    # -----------------------------
    if RUN_EDA:
        correlation_matrix(clean_df)
        fraud_statistics(clean_df)
        average_amount(clean_df)
        average_hour(clean_df)
        feature_distribution(clean_df)
        anomaly_statistics(clean_df)

    # -----------------------------
    # Logistic Regression
    # -----------------------------
    print("\nTraining Logistic Regression...")

    logistic = train_logistic(X_train, y_train)

    evaluate_model(logistic, X_test, y_test)

    # -----------------------------
    # Random Forest
    # -----------------------------
    print("\nTraining Random Forest...")

    rf = train_random_forest(X_train, y_train)

    evaluate_model(rf, X_test, y_test)

    # -----------------------------
    # XGBoost
    # -----------------------------
    print("\nTraining XGBoost...")

    xgb = train_xgboost(X_train, y_train)

    evaluate_model(xgb, X_test, y_test)

    # -----------------------------
    # Save Models
    # -----------------------------
    save_model(logistic, "logistic_model.pkl")
    save_model(rf, "random_forest_model.pkl")
    save_model(xgb, "xgboost_model.pkl")

    # -----------------------------
    # Feature Importance
    # -----------------------------
    plot_feature_importance(xgb, X_train)


if __name__ == "__main__":
    main()