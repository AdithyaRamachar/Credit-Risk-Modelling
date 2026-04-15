import os
import pickle

_model = None

def get_model():
    global _model
    if _model is None:
        # In Lambda, LAMBDA_TASK_ROOT is /var/task
        # Locally, use the project root
        base = os.environ.get("LAMBDA_TASK_ROOT", 
               os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        model_path = os.path.join(base, "artifacts", "model", "model.pkl")
        print(f"Loading model from: {model_path}")
        with open(model_path, 'rb') as f:
            _model = pickle.load(f)
    return _model