import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()



class spAPI:
    """
    A class to handle Spotify Web API authentication and playlist operations.
    """
    def __init__(self):
        """
        Initialize the client with credentials and authorization scope.
        """

        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

        # Scope defines what permissions the app needs (creating private playlists)
        self.scope = "playlist-modify-private"

        # Authenticate and set up the client
        self.clientAutharization()
        
        # List to store Spotify URIs of the songs found
        self.song_uris = []
    
    def clientAutharization(self):
        """
        Authenticates the user using SpotifyOAuth and retrieves the current User ID.
        """
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,client_secret=self.client_secret,redirect_uri=self.redirect_uri,scope=self.scope))

        # Fetch current user details to get the User ID required for playlist creation
        results = self.sp.current_user()
        self.user_id = results['id']
    
    def create_playlist(self):
        """
        Creates a new private playlist and adds the collected songs to it.
        """
        # Create a new playlist for the authenticated user

        self.playlist = self.sp.user_playlist_create(user=self.user_id, name='Billboard 100', public=False, collaborative=False,description="Created Using Python")
        
        # Add the list of song URIs to the newly created playlist
        self.sp.playlist_add_items(playlist_id=self.playlist["id"],items=self.song_uris)

