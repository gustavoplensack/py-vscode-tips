

class SumService:

    def __init__(self) -> None:
        pass
    

    def proccess(self,sum_request):
        x = sum_request.x
        y = sum_request.y
        
        sum = sum_request.x + sum_request.y

        return sum




