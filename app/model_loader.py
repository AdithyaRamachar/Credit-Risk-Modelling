import os
import pickle

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "artifacts", "model", "model.pkl"
        )
        with open(model_path, 'rb') as f:
            _model = pickle.load(f)
    return _model