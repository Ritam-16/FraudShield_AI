from config.rules_config import (
    HIGH_AMOUNT_THRESHOLD,
    HIGH_AMOUNT_SCORE,
    OFF_HOUR_START,
    OFF_HOUR_END,
    OFF_HOUR_SCORE,
)


class RuleEngine:

    def evaluate(self, transaction):
        amount = float(transaction["amount"])
        hour = int(transaction["time"].split(":")[0])

        rule_score = 0
        triggered_rules = []
        reasons = []

        if amount >= HIGH_AMOUNT_THRESHOLD:
            rule_score += HIGH_AMOUNT_SCORE
            triggered_rules.append("RULE001")
            reasons.append("High transaction amount")

        if OFF_HOUR_START <= hour <= OFF_HOUR_END:
            rule_score += OFF_HOUR_SCORE
            triggered_rules.append("RULE002")
            reasons.append("Transaction during off-hours")

        return {
            "rule_score": rule_score,
            "triggered_rules": triggered_rules,
            "reasons": reasons,
        }