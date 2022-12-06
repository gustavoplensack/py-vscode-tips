

from flask import Flask

app = Flask(__name__)

from services import SumService
from src.schemas import SumRequest

SUM_SERVICE = SumService()


@app.route("/health_check")
def health_check():
    return

@app.route("/sum",method=["POST"])
def sum_route():
    
    sum_request = SumRequest(request.get_json())
    

    
    return {"value":SUM_SERVICE.proccess(sum_request=sum_request)}
    


if __name__ == "__main__":

    app.run()
