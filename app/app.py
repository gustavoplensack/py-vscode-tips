

import json

from flask import Flask, request

from src.schemas import SumRequest
from src.services import SumService

app = Flask(__name__)


SUM_SERVICE = SumService()


@app.get("/health_check")
def health_check():
    return {"message": "hello world! This text is intended to be veeeeeeery long because flake8 will be mad"}


@app.post("/soma")
def sum_route():

    sum_request = SumRequest(**request.get_json())

    return {"value": SUM_SERVICE.proccess(sum_request=sum_request)}
