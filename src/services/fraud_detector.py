from config.model_config import MODEL_PATH

from src.engines.risk_engine import RiskEngine
from src.engines.rule_engine import RuleEngine
from src.services.predict import FraudPredictor


class FraudDetector:

    def __init__(self):

        self.predictor = FraudPredictor(MODEL_PATH)
        self.rule_engine = RuleEngine()
        self.risk_engine = RiskEngine()

    def analyze(self, transaction):

        # ----------------------------
        # Machine Learning Prediction
        # ----------------------------

        ml_result = self.predictor.predict(transaction)

        # ----------------------------
        # Business Rule Evaluation
        # ----------------------------

        rule_result = self.rule_engine.evaluate(transaction)

        # ----------------------------
        # Final Risk Assessment
        # ----------------------------

        risk_result = self.risk_engine.evaluate(
            fraud_probability=ml_result["fraud_probability"],
            rule_score=rule_result["rule_score"]
        )

        return {

            "prediction": ml_result["prediction"],

            "prediction_label": (
                "Fraud"
                if ml_result["prediction"]
                else "Legitimate"
            ),

            "fraud_probability": risk_result["fraud_probability"],

            "rule_score": risk_result["rule_score"],

            "triggered_rules": rule_result["triggered_rules"],

            "reasons": rule_result["reasons"],

            "risk_score": risk_result["risk_score"],

            "risk_level": risk_result["risk_level"]

        }