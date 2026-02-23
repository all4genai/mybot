from fastapi import FastAPI

app = FastAPI(title="mybot-api")


@app.get("/")
def root():
    return {"status": "ok", "service": "mybot-api"}


@app.get("/health")
def health():
    return {"status": "healthy"}
