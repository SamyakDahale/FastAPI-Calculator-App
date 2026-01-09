FastAPI Calculator
A simple web calculator with a FastAPI backend. The project provides a modern HTML/CSSfrontend (index.html + style.css)
that calls FastAPI endpoints to perform arithmetic operations (add, subtract, multiply, divide).

Features
Web UI calculator (served at /)
API endpoints for basic arithmetic:
GET /add?a=&b=
GET /subtract?a=&b=
GET /multiply?a=&b=
GET /divide?a=&b/ 
Lightweight, single-file FastAPI app (main.py)
Requirements
Python 3.12+
fastapi
uvicorn
(Dependencies are listed in pyproject.toml: fastapi, uvicorn)

Install & Run
Clone the repo: git clone https://github.com/SamyakDahale/FastAPI-Calculator-App.git cd FastAPI-Calculator-App

Create and activate a virtual environment: python -m venv .venv

macOS / Linux
source .venv/bin/activate

Windows (PowerShell)
.venv\Scripts\Activate.ps1

Install dependencies: pip install fastapi uvicorn

Run the app: uv run uvicorn main:app --reload

Alternative (if using the uv wrapper mentioned in note1.txt):

initialize uv wrapper (snap) once, then
uv run uvicorn main:app --reload

Open the web UI: http://127.0.0.1:8000/

API Usage
Examples (curl):

Add curl "http://127.0.0.1:8000/add?a=5&b=3" Response: { "operation": "add", "a": 5, "b": 3, "result": 8 }

Subtract curl "http://127.0.0.1:8000/subtract?a=10&b=4"

Multiply curl "http://127.0.0.1:8000/multiply?a=6&b=7"

Divide curl "http://127.0.0.1:8000/divide?a=10&b=2" If b == 0 the API responds with HTTP 400 and detail "Division by zero".

The frontend (index.html) uses fetch to call the endpoints and displays results in the calculator UI.

Project structure
main.py — FastAPI application; serves index.html and style.css and exposes arithmetic endpoints
index.html — frontend calculator UI + JS to call the API
style.css — styling for the calculator
pyproject.toml — project metadata and dependencies
note1.txt — local notes for using the uv wrapper and running the app
.python-version, .gitignore, uv.lock — environment / lock files
Contributing
Contributions welcome. Open an issue or a pull request with proposed changes. Keep changes small and include a short description of what you changed and why.

Notes
The app is intentionally minimal and meant for demo / learning purposes.
If you want to publish or containerize it, you can add a Dockerfile or requirements file as needed.
