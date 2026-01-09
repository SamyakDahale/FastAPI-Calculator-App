from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

from fastapi.responses import FileResponse

@app.api_route("/", methods=["GET", "HEAD"])
def read_root():
    return FileResponse("index.html")

@app.get("/style.css")
def get_style():
    return FileResponse("style.css")

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "add", "a": a, "b": b, "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"operation": "divide", "a": a, "b": b, "result": a / b}
