from fastapi import APIRouter

from src.api.schemas import TransactionRequest, FraudAssistantResponse
from src.services.fraud_detector import FraudDetector
from src.assistants.fraud_assistant import FraudAssistant


router = APIRouter()

detector = FraudDetector()
assistant = FraudAssistant()


@router.post(
    "/predict",
    response_model=FraudAssistantResponse,
    summary="Predict transaction fraud risk with AI assistant"
)
def predict_fraud(transaction: TransactionRequest):
    fraud_result = detector.analyze(transaction.model_dump())

    fraud_result["assistant"] = assistant.generate_response(fraud_result)

    return fraud_result