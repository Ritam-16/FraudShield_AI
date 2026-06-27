from src.services.predict import FraudPredictor

predictor = FraudPredictor("models/random_forest_model.pkl")

sample = {

    "amount": 50000,

    "hour": 14,

    "day": 12,

    "month": 5,

    "weekday": 2,

    "is_weekend": 0,

    "log_amount": 10.82,

    "sender_frequency": 40,

    "receiver_frequency": 37,

    "sender_txn_count": 15,

    "receiver_txn_count": 18,

    "amount_deviation": 0.8
}

result = predictor.predict(sample)

print(result)