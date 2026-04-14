import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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