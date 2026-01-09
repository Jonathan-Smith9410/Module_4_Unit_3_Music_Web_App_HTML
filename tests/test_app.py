from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page,test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(["Doolittle"])
    expect(p_tags).to_have_text(["Release year: 1989\nArtist: Pixies"])