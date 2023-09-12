from pydantic import BaseModel, Field

class AlbumSchema(BaseModel):
    title:str
    artist:str
    year:int
    genre:str
    stock:int