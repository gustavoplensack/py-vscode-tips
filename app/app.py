

from flask import Flask, request

app = Flask(__name__)

import json

from src.schemas import SumRequest
from src.services import SumService

SUM_SERVICE = SumService()


@app.get("/health_check")
def health_check():
    return {"message":"hello world!"}

@app.post("/sum")
def sum_route():
    
    sum_request = SumRequest(**request.get_json())

    

    
    return {"value":SUM_SERVICE.proccess(sum_request=sum_request)}
    

