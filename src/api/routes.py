from fastapi import APIRouter

from src.api.schemas import TransactionRequest, FraudResponse
from src.services.fraud_detector import FraudDetector


router = APIRouter()

detector = FraudDetector()


@router.post(
    "/predict",
    response_model=FraudResponse
)
def predict_fraud(transaction: TransactionRequest):
    return detector.analyze(transaction.model_dump())

    return result