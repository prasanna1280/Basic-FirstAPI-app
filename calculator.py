from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Calculator API is running"}


@app.get("/calculate")
def calculate(a: float, b: float, operation: str):
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(
            status_code=400,
            detail="Use add, subtract, multiply, or divide",
        )

    return {"a": a, "b": b, "operation": operation, "result": result}
