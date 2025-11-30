# 🎵 Billboard Hot 100 to Spotify Playlist

A Python automation tool that scrapes the top 100 trending songs from the [Billboard Hot 100](https://www.billboard.com/charts/hot-100/) chart and automatically creates a private Spotify playlist with them.

## 🚀 Features

- **Web Scraping:** Fetches real-time data from Billboard.com using `BeautifulSoup` to identify the top 100 songs.
- **Spotify Integration:** Uses the `Spotipy` library and Spotify Web API to authenticate users securely.
- **Playlist Creation:** Automatically generates a new playlist (e.g., "Billboard 100") and populates it with the found tracks.
- **Error Handling:** Gracefully handles cases where a Billboard song might not be available or found on Spotify.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:**
  - `requests` (HTTP requests)
  - `bs4` (BeautifulSoup for HTML parsing)
  - `spotipy` (Spotify Web API wrapper)
  - `python-dotenv` (Environment variable management)

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/billboard-spotify-automator.git](https://github.com/yourusername/billboard-spotify-automator.git)
cd billboard-spotify-automator
```
### 2. Install Dependencies
You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4 spotipy python-dotenv
```

## 3. Spotify Developer Setup

To use this script, you need credentials from Spotify:

1. Go to the **Spotify Developer Dashboard**.
2. Log in and **create a new App**.
3. In the app settings, locate your **Client ID** and **Client Secret**.
4. Click **“Edit Settings”** and add a Redirect URI.  
   You can use one of the following (must match your `.env` file):

   ````text
   http://example.com
   http://localhost:8888/callback
   ````

 ## 4. Configure Environment Variables

Create a file named `.env` in the project root directory and add your credentials:

````env
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://example.com
````

## 🏃‍♂️ Usage

Run the main script:

````bash
python main.py
````

### What happens next?

- The script will scrape the song titles from Billboard.
- It will open a browser window asking you to authorize the Spotify app (only the first time).
- Once authorized, it creates a playlist titled **"Billboard 100"** in your Spotify account and adds the songs!

## ⚠️ Notes

- **Matching Accuracy:**  
  The script searches Spotify using the song title. Occasionally, if a song title is very generic or formatted differently on Billboard, Spotify might return a different version or fail to find it. The script prints a message to the console if a song is skipped.

- **Web Scraping:**  
  Billboard's website structure can change occasionally. If the scraper stops finding songs, the HTML class selectors in `main.py` may need updating.
