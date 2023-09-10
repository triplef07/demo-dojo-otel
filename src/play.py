from controller.album import create_new_album, delete_album, get_album, get_albums_by_artist, update_album

album = {
          "title":"Matraman",
          "artist":"The Upstairs",
          "year":2004,
          "genre":"New Wave",
          "stock":12
        }

cek = get_albums_by_artist("rumahsakit")
print(cek)