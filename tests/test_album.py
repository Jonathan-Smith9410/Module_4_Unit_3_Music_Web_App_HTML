from lib.album import *

"""
Album constructs with an id, name, year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", 1990 , 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1990
    assert album.artist_id == 1

"""
Test album formats nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Album", 1990 , 1)
    assert str(album) == "Album(1, Test Album, 1990, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Album", 1990 , 1)
    album2 = Album(1, "Test Album", 1990 , 1)
    assert album1 == album2
