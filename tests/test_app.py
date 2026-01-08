from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

# """
# Test calling POST
# Should see new album in the list
# """
# def test_post_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums", data={
#         "title": "Gold",
#         "release_year": "1992",
#         "artist_id": "2"
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ""

#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Doolittle, 1989, 1)\n" \
#         "Album(2, Surfer Rosa, 1988, 1)\n" \
#         "Album(3, Waterloo, 1974, 2)\n" \
#         "Album(4, Super Trouper, 1980, 2)\n" \
#         "Album(5, Bossanova, 1990, 1)\n" \
#         "Album(6, Lover, 2019, 3)\n" \
#         "Album(7, Folklore, 2020, 3)\n" \
#         "Album(8, I Put a Spell on You, 1965, 4)\n" \
#         "Album(9, Baltimore, 1978, 4)\n" \
#         "Album(10, Here Comes the Sun, 1971, 4)\n" \
#         "Album(11, Fodder on My Wings, 1982, 4)\n" \
#         "Album(12, Ring Ring, 1973, 2)\n" \
#         "Album(13, Gold, 1992, 2)"

# # POST /albums
# #  Expected response (400 Bad Request):
# # """
# # Necessary album data expected
# # """

# """
# Test posting album with no data
# """

# def test_post_album_with_no_data(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/albums")
#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == "Necessary album data expected"


# """
# Test getting all albums
# """
# def test_get_albums(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     get_response = web_client.get("/albums")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         "Album(1, Doolittle, 1989, 1)\n" \
#         "Album(2, Surfer Rosa, 1988, 1)\n" \
#         "Album(3, Waterloo, 1974, 2)\n" \
#         "Album(4, Super Trouper, 1980, 2)\n" \
#         "Album(5, Bossanova, 1990, 1)\n" \
#         "Album(6, Lover, 2019, 3)\n" \
#         "Album(7, Folklore, 2020, 3)\n" \
#         "Album(8, I Put a Spell on You, 1965, 4)\n" \
#         "Album(9, Baltimore, 1978, 4)\n" \
#         "Album(10, Here Comes the Sun, 1971, 4)\n" \
#         "Album(11, Fodder on My Wings, 1982, 4)\n" \
#         "Album(12, Ring Ring, 1973, 2)"



# """
# When I call GET /artists I see a list of artists
# """

# def test_get_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

# """
# When I call POST /artists with the info
# I see the band in the list when I call GET /artists
# """
# def test_post_artists(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/artists", data={
#         'name': "Wild nothing",
#         'genre': "Indie"
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ""

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"

# """
# When I call POST /artists with no info
# I receive an error message:
# You need to submit a name and genre
# """

# def test_post_artists_with_no_info(db_connection, web_client):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post("/artists")
#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == "You need to submit a name and genre"

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"




"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
