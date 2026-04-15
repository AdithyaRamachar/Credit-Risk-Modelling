from fastapi import FastAPI
from app.schema import CustomerDataRaw
from app.utils import preprocess
from app.model_loader import get_model
from monitoring.logger import log_prediction
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Credit Risk API is running", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: CustomerDataRaw):
    df = preprocess(data.dict())
    model = get_model()
    pred = model.predict_proba(df)[0][1]
    log_prediction(data.dict(), pred)
    return {"probability_default": float(pred)}

handler = Mangum(app, lifespan="off", api_gateway_base_path="/prod")