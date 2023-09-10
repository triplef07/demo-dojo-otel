import uuid
from typing import Optional
from pydantic import BaseModel, Field

class AlbumModel(BaseModel):
    id:str = Field(default_factory=uuid.uuid4, alias="_id")
    title:str = Field(...)
    artist:str = Field(...)
    year:int = Field(...)
    genre:str = Field(...)
    stock:int = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "rumahsakit",
                "artist": "rumahsakit",
                "genre": "Britpop",
                "year":"1998",
                "stock":10
            }
        }

class AlbumModelUpdate(BaseModel):
    title:Optional[str]
    artist:Optional[str]
    year:Optional[str]
    genre:Optional[str]
    stock:Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "rumahsakit",
                "artist": "rumahsakit",
                "genre": "Britpop",
                "year":"1998",
                "stock":10
            }
        }