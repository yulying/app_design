from spotipy.oauth2 import SpotifyClientCredentials

# CLIENT_ID = "7042a087713a469ea4b01d562b2df63b"
# CLIENT_SECRET = "123d1f1b01f545168d6a5ddff83c491c"

# # Authentication - Without User
# client_credentials_manager = SpotifyClientCredentials(
#     client_id=CLIENT_ID, client_secret=CLIENT_SECRET
# )
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# playlist_link = "https://open.spotify.com/playlist/0OhexwRXjdNkZfV5J41JeC"
# playlist_URI = playlist_link.split("/")[-1].split("?")[0]
# track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     # URI
#     track_uri = track["track"]["uri"]

#     # Track name
#     track_name = track["track"]["name"]

#     # Main Artist
#     artist_uri = track["track"]["artists"][0]["uri"]
#     artist_info = sp.artist(artist_uri)

#     # Name, popularity, genre
#     artist_name = track["track"]["artists"][0]["name"]
#     artist_pop = artist_info["popularity"]
#     artist_genres = artist_info["genres"]

#     # Album
#     album = track["track"]["album"]["name"]

#     # Popularity of the track
#     track_pop = track["track"]["popularity"]

#     sp.audio_features(track_uri)[0]
