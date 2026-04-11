import os
import mlflow
import mlflow.pyfunc
from config import (
    MLFLOW_TRACKING_URI,
    DAGSHUB_USERNAME,
    DAGSHUB_TOKEN,
    MODEL_NAME,
    MODEL_STAGE
)

# 🔐 Set credentials
os.environ["MLFLOW_TRACKING_USERNAME"] = DAGSHUB_USERNAME
os.environ["MLFLOW_TRACKING_PASSWORD"] = DAGSHUB_TOKEN

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


def load_model():
    model_uri = f"models:/{MODEL_NAME}/{MODEL_STAGE}"
    return mlflow.pyfunc.load_model(model_uri)


model = load_model()