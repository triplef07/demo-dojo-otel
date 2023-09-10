from fastapi import APIRouter, HTTPException, Request,status
from ..controller.album import get_album,get_albums_by_artist
from typing import List
from ..schema.album import AlbumSchema
from bson import json_util
import json


album_router = APIRouter(prefix="/album")

@album_router.get("/")
async def get_album_by_title_and_artist(title:str,artist:str):
    album = get_album(title=title,artist=artist) 
    if album is not None:
        return json.loads(json_util.dumps(album))
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Album with title:{title} and artist:{artist} is not found")

@album_router.get("/{artist}")
async def get_album_by_artist_route(artist:str):
    album_list = get_albums_by_artist(artist=artist)
    if len(album_list)> 0:
        return json.loads(json_util.dumps(album_list))
    raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Album with artist:{artist} is not found")

