from fastapi import FastAPI
from app.schema import CustomerDataRaw
from app.utils import preprocess
from app.model_loader import model
from monitoring.logger import log_prediction

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: CustomerDataRaw):
    df = preprocess(data.dict())
    pred = model.predict(df)[0]

    log_prediction(data.dict(), pred)

    return {
        "probability_default": float(pred)
    }