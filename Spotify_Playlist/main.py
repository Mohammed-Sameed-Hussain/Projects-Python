import requests
from bs4 import BeautifulSoup
from Spotify import spAPI


# Target URL: Billboard Hot 100 Chart
URL = "https://www.billboard.com/charts/hot-100/"


# Headers are required to mimic a real browser request. 
# Without this 'User-Agent', Billboard might block the scraper (403 Forbidden).
headers = {
    "USER-AGENT" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}


# --- Step 1: Scrape Billboard Website ---

# Fetch the webpage content
response = requests.get(url=URL, headers=headers)
web_response = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(web_response, 'html.parser') 

# Find all container divs for the chart rows.
# Note: These class names are specific to Billboard's website structure.
song_tags = soup.find_all(name='div', class_='o-chart-results-list-row-container')

# Iterate through each row to extract the song title
top_100_songs = []


for tag in song_tags:
    # Locate the H3 tag containing the song title (identified by id 'title-of-a-story')
    title_tag = tag.find(name='h3', id="title-of-a-story")

    # Strip whitespace (newlines/tabs) and add to list
    top_100_songs.append(title_tag.getText().strip())



# --- Step 2: Interact with Spotify API ---

# Initialize the Spotify API client (authenticates automatically on init)
sp_client = spAPI()

# Iterate through the scraped song titles to find their Spotify URIs
for song in top_100_songs:
    # Search for the song on Spotify. 'track:' limits search to tracks only.
    result = sp_client.sp.search(q=f'track:{song}', type="track")

    try:
        # Extract the URI of the first result (most likely match)
        uri = result["tracks"]["items"][0]["uri"]
        sp_client.song_uris.append(uri)
    except IndexError:
        # Handle cases where the song isn't found on Spotify
        print(f"{song} doesn't exist in Spotify. Skipped.") 


# --- Step 3: Create Playlist ---

# Create the playlist and add the found songs
sp_client.create_playlist()

