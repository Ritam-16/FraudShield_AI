from src.services.fraud_detector import FraudDetector

detector = FraudDetector()

transaction = {
    "sender_account": "ACC001",
    "receiver_account": "ACC099",
    "amount": 250000,
    "time": "02:15:00"
}

result = detector.analyze(transaction)

print("\n============== FRAUD DETECTOR RESULT ==============\n")

for key, value in result.items():
    print(f"{key} : {value}")