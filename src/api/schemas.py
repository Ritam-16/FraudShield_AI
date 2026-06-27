from pydantic import BaseModel


class TransactionRequest(BaseModel):
    sender_account: str
    receiver_account: str
    amount: float
    time: str


class FraudResponse(BaseModel):
    prediction: int
    prediction_label: str
    fraud_probability: float
    rule_score: int
    triggered_rules: list[str]
    reasons: list[str]
    risk_score: float
    risk_level: str