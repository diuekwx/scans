from pydantic import BaseModel


class SearchRequest(BaseModel):
    title: str
