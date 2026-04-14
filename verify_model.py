# verify_model.py
import os
os.environ['MLFLOW_TRACKING_USERNAME'] = '----------'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '-----------'

import mlflow

mlflow.set_tracking_uri('https://dagshub.com/adithya.anytime.anywhere/Credit-Risk-Modelling.mlflow')

client = mlflow.tracking.MlflowClient()
models = client.search_registered_models()
for m in models:
    print(f"Model: {m.name}")
    for v in m.latest_versions:
        print(f"  Version: {v.version} | Stage: {v.current_stage} | Run: {v.run_id}")
