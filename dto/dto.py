from typing import Union, Literal, List
from pydantic import BaseModel, ConfigDict


class ModelInput(BaseModel):
    gender: Union[Literal["female", "male"], List[Literal["female", "male"]]]
    race_ethnicity: Union[Literal["group A", "group B", "group C", "group D", "group E"],
                          List[Literal["group A", "group B", "group C", "group D", "group E"]]]
    parental_level_of_education: Union[Literal["some college", "associate's degree", "high school", "some high school", "bachelor's degree", "master's degree"],
                                      List[Literal["some college", "associate's degree", "high school", "some high school", "bachelor's degree", "master's degree"]]]
    lunch: Union[Literal["standard", "free/reduced"], List[Literal["standard", "free/reduced"]]]
    test_preparation_course: Union[Literal["none", "completed"], List[Literal["none", "completed"]]]

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ModelOutput(BaseModel):
    math_score: Union[int, list]
    reading_score: Union[int, list]
    writing_score: Union[int, list]

    model_name: str
    model_version: str
    model_config = ConfigDict(arbitrary_types_allowed=True)