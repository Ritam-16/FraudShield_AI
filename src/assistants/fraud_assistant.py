from src.llm.openai_client import OpenAIClient


class FraudAssistant:

    def __init__(self):
        self.llm = OpenAIClient()

    def generate_response(self, fraud_result):

        base_response = self._fallback_response(fraud_result)

        # Use LLM only for HIGH-risk transactions
        if fraud_result["risk_level"] != "HIGH":
            base_response["llm_used"] = False
            return base_response

        try:
            llm_message = self.llm.generate_fraud_message(fraud_result)

            if llm_message:
                base_response["user_message"] = llm_message
                base_response["llm_used"] = True

        except Exception as e:
            print("\n========== LLM ERROR ==========")
            print(e)
            print("================================")

            base_response["llm_used"] = False

        return base_response

    def _fallback_response(self, fraud_result):

        risk_level = fraud_result["risk_level"]
        probability = fraud_result["fraud_probability"]
        reasons = fraud_result["reasons"]
        triggered_rules = fraud_result["triggered_rules"]

        if risk_level == "HIGH":
            return {
                "severity": "HIGH",
                "recommended_action": "BLOCK_TRANSACTION",
                "user_title": "Payment stopped",
                "user_message": (
                    f"Your payment was stopped because it was classified as high risk. "
                    f"Fraud probability is {probability}%. "
                    f"Reason: {self._format_reasons(reasons)}."
                ),
                "next_steps": [
                    "Verify your identity using OTP.",
                    "Contact support if this transaction was not made by you."
                ],
                "admin_summary": (
                    f"High-risk transaction detected. "
                    f"Triggered rules: {triggered_rules}. "
                    f"Fraud probability: {probability}%."
                ),
                "llm_used": False
            }

        if risk_level == "MEDIUM":
            return {
                "severity": "MEDIUM",
                "recommended_action": "REQUIRE_VERIFICATION",
                "user_title": "Verification required",
                "user_message": (
                    f"This payment needs additional verification. "
                    f"Fraud probability is {probability}%. "
                    f"Reason: {self._format_reasons(reasons)}."
                ),
                "next_steps": [
                    "Complete OTP verification.",
                    "Retry the payment after verification."
                ],
                "admin_summary": (
                    f"Medium-risk transaction detected. "
                    f"Triggered rules: {triggered_rules}. "
                    f"Fraud probability: {probability}%."
                ),
                "llm_used": False
            }

        return {
            "severity": "LOW",
            "recommended_action": "ALLOW_TRANSACTION",
            "user_title": "Payment allowed",
            "user_message": (
                f"Your payment appears safe. "
                f"Fraud probability is {probability}%."
            ),
            "next_steps": [
                "No additional action is required."
            ],
            "admin_summary": (
                f"Low-risk transaction. "
                f"Triggered rules: {triggered_rules}. "
                f"Fraud probability: {probability}%."
            ),
            "llm_used": False
        }

    def _format_reasons(self, reasons):
        if not reasons:
            return "No strong rule-based fraud indicators were detected"

        return ", ".join(reasons)