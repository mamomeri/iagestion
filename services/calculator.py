# services/calculator.py
def evaluate_expression(expression: str) -> float:
    try:
        return eval(expression, {"__builtins__": {}})
    except Exception as e:
        return f"Error: {e}"