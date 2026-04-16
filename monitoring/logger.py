import json
import os
from datetime import datetime

LOG_PATH = "/tmp/logs.json"

def log_prediction(input_data: dict, prediction: float):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": input_data,
        "prediction": prediction
    }
    try:
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Logging failed: {e}")