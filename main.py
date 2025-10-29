from typing import Dict
from fastapi import FastAPI
import uvicorn
from dto.dto import ModelInput, ModelOutput
from preprocess.preprocess import preprocess
from model.model import Model

import os
import sys

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))


column_names = ['gender', 'race ethnicity', 'parental level of education', 'lunch', 'test preparation course']
model_path = "./model/model_versions/random_forrest_model-0.1.0.pkl"
encoders_path = "./encoders"

app = FastAPI()

@app.get("/")
async def welcome() -> Dict:
    return {"message": "Welcome to My App!",
            "status": "success"}

@app.get("/health")
async def health_check() -> Dict:
    return {"status": "success"}

@app.post("/predict")
async def predict(input: ModelInput):
    model = Model(model_path)
    processed_input = preprocess(input.model_dump(), col_names=column_names, encoders_path=encoders_path)
    predictions = model.predict(processed_input)

    model_name = model.model_path.split('-')[0].split('/')[-1]
    model_version = model.model_path.split('-')[1].replace('.pkl', '')
    output = ModelOutput(math_score=predictions['math score'],
                         reading_score=predictions['reading score'],
                         writing_score=predictions['writing score'],
                         model_name=model_name,
                         model_version=model_version)
    return output


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)

