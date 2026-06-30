import os

from dotenv import load_dotenv
from openai import OpenAI

from src.llm.prompts import SYSTEM_PROMPT

load_dotenv()


class OpenAIClient:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found.")

        self.client = OpenAI(api_key=api_key)

    def generate_fraud_message(self, fraud_result) -> str:
        """
        Generate a short customer-facing fraud notification.
        """

        reasons = ", ".join(fraud_result["reasons"])

        prompt = f"""
{SYSTEM_PROMPT}

Fraud context:
Reasons: {reasons}

Generate one short banking notification for the customer.
"""

        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=0.2,
            max_output_tokens=30,
        )

        return response.output_text.strip()