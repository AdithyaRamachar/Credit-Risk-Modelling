import os
os.environ['MLFLOW_TRACKING_USERNAME'] = '----------'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '-----------'
import mlflow
mlflow.set_tracking_uri('https://dagshub.com/adithya.anytime.anywhere/Credit-Risk-Modelling.mlflow')
client = mlflow.tracking.MlflowClient()
runs = [
    'af754627e4384fe28d36ef31e28a2d7a',
    '10c0eb020ac84340886903981a5b0d3c',
    'e931784b8f044720b6274d99a5ae1d4b',
    'd1f928555615433eb30410dc98c2e309',
    'e2bc0a5043b04397be5f8dee9afbe52b',
    '9c301b9c4a99460298a4e66dae6a7eac',
    '3ad06a20ee4b4684a1d23c2f8632c949'
]
for run_id in runs:
    run = client.get_run(run_id)
    artifacts = client.list_artifacts(run_id)
    artifact_names = [a.path for a in artifacts]
    run_name = run.data.tags.get('mlflow.runName', 'no-name')
    print(f"Run: {run_id} | Name: {run_name} | Artifacts: {artifact_names}")
