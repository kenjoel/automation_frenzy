from cgi import test
from typing import List

from fastapi import Request, UploadFile
import pandas as pd
from starlette.datastructures import URL

from api import app


@app.get("/")
def root():
    return "Hello, welcome to this world"


@app.post("/upload")
async def upload_csv(file: List[UploadFile], request: Request):
    file_dataframes = pd.concat(pd.read_csv(fname.file) for fname in file)
    required_columns = ["Hostname", "Device Policy", "Result"]
    test1 = file_dataframes[required_columns]
    result = test1["Result"]
    count_percent = result.value_counts().to_dict()
    test1.to_csv("static/full_compliance_report.csv")
    path =str(request.base_url) + "static/full_compliance_report.csv"
    print(count_percent)
    
    return {"data":count_percent, "url": path}
   


    # else:
    #     dataframe = pd.read_csv(file[0].file)
    #     required_columns = ["Hostname", "Device Policy", "Result"]
    #     test1 = dataframe[required_columns]
    #     one_file = test1.to_csv("someshit.csv")
