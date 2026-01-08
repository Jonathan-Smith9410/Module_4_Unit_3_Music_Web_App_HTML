from lib.artist import Artist

"""
Constructs with name and genre
"""

def test_constructs():
    artist = Artist(1, "Test Name", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Name"
    assert artist.genre == "Test Genre"

def test_artists_format():
    artist = Artist(1, "Test Name", "Test Genre")
    assert str(artist) == "Artist(1, Test Name, Test Genre)"