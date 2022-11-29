from pydantic import BaseModel


class Query(BaseModel):
    movie_name: str
    no_of_recommendation: int


class ResOut(BaseModel):
    movie_name: str
    genre: str
