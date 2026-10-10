from pydantic import BaseModel

class AiResponseSchema(BaseModel):

    question:str
    response:str