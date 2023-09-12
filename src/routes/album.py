from fastapi import APIRouter, HTTPException, Request,status
from fastapi.encoders import jsonable_encoder
from ..controller.album import create_new_album, delete_album, get_album,get_albums_by_artist, update_album
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

@album_router.post("/")
async def post_new_album(album:AlbumSchema):
    try:
        create_new_album(jsonable_encoder(album))
        return {"message":"album successfully save"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Failed to save album")

@album_router.delete("/")
async def delete_album_by_id(id:str):
    album = delete_album(id)
    if (album == True):
        return{"message":"album successfully save"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Failed to delete album")
    
@album_router.put("/{artist}/{title}/addStock")
async def add_album_stock(artist:str,title:str):
    album = get_album(title,artist)
    if album is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Album with title:{title} and artist:{artist} is not found")
    album["stock"] = album["stock"]+1
    try:
        update_album(album["_id"],stock=album["stock"])
        return{"message":"Album stock increased successfully"}
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="failed to add album stock")

@album_router.put("/{artist}/{title}/decreaseStock")
async def add_album_stock(artist:str,title:str):
    album = get_album(title,artist)
    if album is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Album with title:{title} and artist:{artist} is not found")
    album["stock"] = album["stock"]-1
    if (album["stock"] <= 0):
        return{"message":"Album stock decreased successfully"}
    try:
        update_album(album["_id"],stock=album["stock"])
        return{"message":"Album stock decreased successfully"}
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="failed to add album stock")
