from pydantic import BaseModel, Field

class AlbumSchema(BaseModel):
    id:str 
    title:str
    artist:str
    year:int
    genre:str
    stock:int