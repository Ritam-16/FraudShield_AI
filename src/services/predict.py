import joblib
import pandas as pd
import numpy as np


class FraudPredictor:

    FEATURES = [
        "amount",
        "hour",
        "high_value",
        "off_hours",
        "log_amount",
    ]

    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def _prepare_transaction(self, transaction):
        amount = float(transaction["amount"])
        time_value = transaction["time"]

        hour = int(time_value.split(":")[0])

        return {
            "amount": amount,
            "hour": hour,
            "high_value": int(amount >= 100000),
            "off_hours": int(1 <= hour <= 3),
            "log_amount": float(np.log1p(amount)),
        }

    def predict(self, transaction):
        features = self._prepare_transaction(transaction)

        df = pd.DataFrame([{
            feature: features[feature]
            for feature in self.FEATURES
        }])

        prediction = self.model.predict(df)[0]
        probability = self.model.predict_proba(df)[0][1]

        probability = min(probability, 0.999)

        return {
            "prediction": int(prediction),
            "fraud_probability": float(probability),
            "features": features
        }