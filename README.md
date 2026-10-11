# Student Class API

FastAPI endpoint that serves the supplied student CSV in original row order.

## Endpoint
- `GET /api` — all students
- `GET /api?class=1A` — filter by one class
- `GET /api?class=1A&class=1B` — filter by multiple classes

CORS allows GET and OPTIONS from any origin. The response preserves the original CSV row order.

## Local run
```bash
pip install -r requirements.txt
uvicorn api.index:app --host 0.0.0.0 --port 8000
```
