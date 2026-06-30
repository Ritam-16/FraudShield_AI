from pydantic import BaseModel, ConfigDict


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


class AssistantResponse(BaseModel):
    severity: str
    recommended_action: str
    user_title: str
    user_message: str
    next_steps: list[str]
    admin_summary: str
    llm_used: bool


class FraudAssistantResponse(FraudResponse):
    assistant: AssistantResponse