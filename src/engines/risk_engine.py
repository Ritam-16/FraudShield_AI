from config.risk_config import (
    ML_WEIGHT,
    RULE_WEIGHT,
    HIGH_RISK,
    MEDIUM_RISK,
)


class RiskEngine:

    def evaluate(self, fraud_probability, rule_score):

        fraud_probability_percent = fraud_probability * 100

        risk_score = (
            fraud_probability_percent * ML_WEIGHT
            +
            rule_score * RULE_WEIGHT
        )

        risk_score = min(risk_score, 100)

        # Direct override for very confident ML prediction
        if fraud_probability_percent >= 85:
            risk_level = "HIGH"

        elif risk_score >= HIGH_RISK:
            risk_level = "HIGH"

        elif risk_score >= MEDIUM_RISK:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        return {
            "fraud_probability": round(fraud_probability_percent, 2),
            "rule_score": rule_score,
            "risk_score": round(risk_score, 2),
            "risk_level": risk_level
        }