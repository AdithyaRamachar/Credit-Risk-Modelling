import mlflow
import mlflow.pyfunc
from config import MLFLOW_TRACKING_URI, MODEL_NAME, MODEL_STAGE

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

def load_model():
    model_uri = f"models:/{MODEL_NAME}/{MODEL_STAGE}"
    return mlflow.pyfunc.load_model(model_uri)

model = load_model()