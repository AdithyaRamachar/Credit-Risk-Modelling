import json
from datetime import datetime

def log_prediction(input_data, prediction):
    log = {
        "timestamp": str(datetime.now()),
        "input": input_data,
        "prediction": float(prediction)
    }

    with open("logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")