
from pydantic import BaseModel


class SumRequest(BaseModel):

    x: int

    y: int
