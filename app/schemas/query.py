from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class Source(BaseModel):
    document: str
    chunk: int


class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]