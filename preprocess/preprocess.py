from typing import Union, Dict, List
import sys


import os
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def encode(df: pd.DataFrame, encoders_path: str, col_names: List[str] = None) -> pd.DataFrame:

    # список всех кодировщиков
    encoders = os.listdir(encoders_path)

    for name in encoders:
        # распаковываем кодировщик из пикл-файла
        with open(os.path.join(encoders_path, name), 'rb') as f:
            encoder = joblib.load(f)
        # получаем имена столбцов для кодировщиков
        col_name = name.replace('_', ' ').replace(' encoder.pkl', '')


        # проходим по столбцам, проверяем, есть ли они в данных
        if col_name in col_names:

            # применяем кодировщика, в зависимости от его типа
            if isinstance(encoder, LabelEncoder):
                df[col_name] = encoder.transform(df[col_name])

            elif isinstance(encoder, OneHotEncoder):
                encoded = encoder.transform(df[[col_name]]).toarray()
                encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([col_name]))
                df = pd.concat([df.drop(columns=[col_name]), encoded_df], axis=1)

    return df



def preprocess(input_data: Union[Dict, pd.DataFrame, np.array, List], col_names: List[str] = None, encoders_path: str = None) -> pd.DataFrame:

    try:
        df = pd.DataFrame([{
            "gender": input_data["gender"],
            "race ethnicity": input_data["race_ethnicity"],
            "parental level of education": input_data["parental_level_of_education"],
            "lunch": input_data["lunch"],
            "test preparation course": input_data["test_preparation_course"],
        }])

    except Exception as e:
        raise ValueError(
            f"Incorrect value supplied for preprocessing: input:{input_data}, error: {e}"
        )

    if encoders_path:
        df = encode(df, encoders_path, col_names)


    return df

