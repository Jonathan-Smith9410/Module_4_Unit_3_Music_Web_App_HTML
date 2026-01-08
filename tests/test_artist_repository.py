from lib.artist_repository import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

def test_get_artists_as_string(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artists = repository.get_artists_as_string()
    assert artists == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_create_artist(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.create(Artist(None, "Wild nothing", "Indie"))
    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]