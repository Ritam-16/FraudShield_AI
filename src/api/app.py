from fastapi import FastAPI

from src.api.routes import router


app = FastAPI(
    title="FraudShield AI API",
    description="Fraud detection API using ML, rule engine, and risk engine.",
    version="1.0.0"
)

app.include_router(router)