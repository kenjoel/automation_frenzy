from typing import List

from fastapi import FastAPI, UploadFile
import pandas as pd

app = FastAPI()


@app.get("/")
def root():
    return "Hello, welcome to this world"


@app.post("/")
def upload_csv(file: List[UploadFile]):
    if len(file) > 1:
        file_dataframes = pd.concat(pd.read_csv(fname.file) for fname in file)
        required_columns = ["Timestamp", "Hostname", "Device Policy", "Result"]
        test1 = file_dataframes[required_columns]
        one_column = test1.to_csv("somethingelse.csv")

    else:
        dataframe = pd.read_csv(file[0].file)
        required_columns = ["Timestamp", "Hostname", "Device Policy", "Result"]
        test1 = dataframe[required_columns]
        one_file = test1.to_csv("someshit.csv")
