from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_album(page,test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(["Doolittle"])
    expect(p_tags).to_have_text(["Release year: 1989\nArtist: Pixies"])

def test_get_albums(page,test_web_address, db_connection):
    db_connection.seed("seeds/simplified_music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: Doolittle\nReleased: 1989\n" \
        "\n" \
        "Go to the Doolittle page\n" \
        "Title: Surfer Rosa\nReleased: 1988\n" \
        "\n" \
        "Go to the Surfer Rosa page\n"])

def test_get_artist(page,test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text(["Pixies"])

def test_get_artists(page,test_web_address, db_connection):
    db_connection.seed("seeds/simplified_music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Name: Pixies\n" \
        "Go to the Pixies page\n" \
        "Name: ABBA\n" \
        "Go to the ABBA page"
        ])
    
def test_create_album(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/simplified_music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')
    
    page.fill('input[name=title]', 'Test Album')
    page.fill('input[name=release_year]', '1234')
    page.click('text="Add album"')

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Test Album")
    release_year_tag = page.locator("release_year")
    expect(release_year_tag).to_have_text("Released: 1234")