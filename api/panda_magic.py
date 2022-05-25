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
async def upload_csv(files: List[UploadFile], request: Request):
    required_columns = ["Hostname", "Device Policy", "Result"]
    items = []
    file_result = []
    for i in files:
        file_items = []
        file_dataframe = pd.read_csv(i.file)
        append_dataframe = file_dataframe[required_columns]
        file_items.append(append_dataframe)
        items.append(append_dataframe)
    combined_dataframes = pd.concat(items)
    result = combined_dataframes["Result"]
    count_percent = result.value_counts().to_dict()
    combined_dataframes.to_csv("static/full_compliance_report.csv")
    path =str(request.base_url) + "static/full_compliance_report.csv"
    for i in items:
        result = i["Result"]
        hostname = i["Hostname"]
        file_count_percent = result.value_counts().to_dict()
        file_result.append({"Hostname": hostname, "percent": file_count_percent}) 
    return {"data":count_percent, "url": path, "files": file_result}
   
