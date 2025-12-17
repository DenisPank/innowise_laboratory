from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ok"}

@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)