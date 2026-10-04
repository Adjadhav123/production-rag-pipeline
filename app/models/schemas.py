from typing import List 

from pydantic import BaseModel 



class ChatRequest(BaseModel):
    question : str 
    user_id: str | None = None


class Source(BaseModel):
    document : str | None = None 
    page : int | None = None 
    chunk_id : str | None = None


class ChatResponse(BaseModel):
    answer : str | None = None 
    source : List[Source]

    
     
