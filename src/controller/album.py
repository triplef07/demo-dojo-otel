from pymongo import MongoClient
from pymongo.collection import Collection
from ..models.album import AlbumModel
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

mongo_url = os.getenv("MONGO_URL","mongodb://localhost:27017")

client = MongoClient(mongo_url)
db = client["rental_db"]
collection = db["albums"]

# Fungsi 1: Membuat data album baru dengan validasi 
def create_new_album(album: AlbumModel):
    try:
        inserted_id = collection.insert_one(album).inserted_id
        return str(inserted_id)
    except DuplicateKeyError:
        raise ValueError("Album with the same title, artist, and year already exists.")

# Fungsi 2: Mendapatkan data satu album berdasarkan title dan artist 
def get_album(title: str, artist: str):
    album = collection.find_one({"title": title, "artist": artist})
    if album:
        return album
    else:
        return None

# Fungsi 3: Mendapatkan data banyak album berdasarkan artist 
def get_albums_by_artist(artist: str) -> List[AlbumModel]:
    albums = collection.find({"artist": artist})
    return list(albums)

# Fungsi 4: Menghapus data album berdasarkan id (ObjectId) 
def delete_album(album_id: str):
    result = collection.delete_one({"_id": ObjectId(album_id)})
    return result.deleted_count > 0

# Fungsi 5: Update data album berdasarkan id (ObjectId) 
def update_album(
    album_id: str,
    title: Optional[str] = None,
    artist: Optional[str] = None,
    year: Optional[int] = None,
    genre: Optional[str] = None,
    stock: Optional[int] = None
):
    update_data = {}
    if title:
        update_data["title"] = title
    if artist:
        update_data["artist"] = artist
    if year:
        update_data["year"] = year
    if genre:
        update_data["genre"] = genre
    if stock:
        update_data["stock"] = stock
    result = collection.update_one({"_id": ObjectId(album_id)}, {"$set": update_data})
    return result.modified_count > 0