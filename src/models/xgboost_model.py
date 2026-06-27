from xgboost import XGBClassifier


def train_xgboost(X_train, y_train):
    """
    Train XGBoost model.
    """

    model = XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)

    return model