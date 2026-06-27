from src.engines.rule_engine import RuleEngine

engine = RuleEngine()

transaction = {

    "amount": 450000,

    "hour": 2,

    "amount_deviation": 3.4,

    "sender_frequency": 55

}

result = engine.evaluate(transaction)

print(result)