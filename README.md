# mybot

Minimal FastAPI service for Render + GitHub Actions deploy.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

## Endpoints

- `/` -> basic status
- `/health` -> health check
