from src.engines.risk_engine import RiskEngine

engine = RiskEngine()

result = engine.evaluate(

    fraud_probability=0.91,

    rule_score=85

)

print(result)