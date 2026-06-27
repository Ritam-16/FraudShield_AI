from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def train_logistic(X_train, y_train):
    """
    Train Logistic Regression model.
    """

    model = Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=5000,
                random_state=42
            )
        )
    ])

    model.fit(X_train, y_train)

    return model