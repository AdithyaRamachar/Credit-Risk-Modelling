# register_model.py
import os
os.environ['MLFLOW_TRACKING_USERNAME'] = 'adithya.anytime.anywhere'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'e1e5810da884bd5a7b1cac9184c0da99f6920cb3'

import mlflow

mlflow.set_tracking_uri('https://dagshub.com/adithya.anytime.anywhere/Credit-Risk-Modelling.mlflow')

client = mlflow.tracking.MlflowClient()

# Create version by linking the artifact path directly
version = client.create_model_version(
    name="Random_Forest_Tuned_Model",
    source="mlflow-artifacts:/daaaeb97e2864a1086faed2ea3091a35/9c301b9c4a99460298a4e66dae6a7eac/artifacts/model",
    run_id="9c301b9c4a99460298a4e66dae6a7eac"
)
print(f"Created version: {version.version}")

# Promote to Production
client.transition_model_version_stage(
    name="Random_Forest_Tuned_Model",
    version=version.version,
    stage="Production"
)
print("Promoted to Production successfully")