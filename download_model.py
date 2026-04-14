import os
os.environ['MLFLOW_TRACKING_USERNAME'] = 'adithya.anytime.anywhere'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'e1e5810da884bd5a7b1cac9184c0da99f6920cb3'

import mlflow

mlflow.set_tracking_uri('https://dagshub.com/adithya.anytime.anywhere/Credit-Risk-Modelling.mlflow')

# Download model artifact directly from the run
local_path = mlflow.artifacts.download_artifacts(
    artifact_uri="runs:/9c301b9c4a99460298a4e66dae6a7eac/model",
    dst_path="./artifacts/model"
)
print(f"Model downloaded to: {local_path}")