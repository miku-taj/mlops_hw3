import pandas as pd
import joblib
import numpy as np


class Model:
    def __init__(self, model_path: str = None) -> None:
        self.model_path = model_path

    def _load(self) -> None:
        with open(self.model_path, 'rb') as f:
            self.model = joblib.load(f)

    def predict(self, input_data: pd.DataFrame) -> pd.DataFrame:
        self._load()
        preds_df = pd.DataFrame(
            np.round(self.model.predict(input_data)),
            columns=["math score", "reading score", "writing score"]  # adjust names
        )
        return preds_df