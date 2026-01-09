from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

#     # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

#     # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def title_and_release(self):
        rows = self._connection.execute('SELECT id, title, release_year from albums')
        albums = []
        for row in rows:
            item = [row["title"], row["release_year"], row["id"]]
            albums.append(item)
        return albums
#   Find method

    def find(self, id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def find_single_album(self, id):
        rows = self._connection.execute('SELECT albums.title, albums.release_year, artists.name FROM albums JOIN artists ON artists.id = albums.artist_id WHERE albums.id = %s', [id])
        album = rows[0]
        return album

    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None
    
    def delete(self, title):
        self._connection.execute('DELETE FROM albums WHERE title = %s', [title])
        return None