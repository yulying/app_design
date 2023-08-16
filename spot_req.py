import requests
import pandas as pd
import base64

CLIENT_ID = "7042a087713a469ea4b01d562b2df63b"
CLIENT_SECRET = "123d1f1b01f545168d6a5ddff83c491c"

TOKEN_URL = "https://accounts.spotify.com/api/token"
AUTH_URL = "https://accounts.spotify.com/authorize"
BASE_URL = "https://api.spotify.com/v1/"

# POST
# auth_response = requests.post(
#     AUTH_URL,
#     {
#         "grant_type": "client_credentials",
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#     },
# )

# auth_response_data = auth_response.json()
# access_token = auth_response_data["access_token"]

# headers = {"Authorization": "Bearer {token}".format(token=access_token)}

auth_code = requests.get(
    AUTH_URL,
    {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": "http://localhost:8888/callback",
        "scope": "user-read-recently-played",
    },
)

print(auth_code)

auth_header = base64.urlsafe_b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode())
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic %s" % auth_header.decode(),
}

payload = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": "https://open.spotify.com/collection/playlists",
    #'client_id': CLIENT_ID,
    #'client_secret': CLIENT_SECRET,
}

# Make a request to the /token endpoint to get an access token
access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

# convert the response to JSON
access_token_response_data = access_token_request.json()

print(access_token_response_data)

# save the access token
access_token = access_token_response_data["access_token"]

# track_id = "1b5oGPaIeGNS7lSHkWwx2L"

# r = requests.get(BASE_URL + "audio-features/" + track_id, headers=headers)

# artist_id = "2YvlK6lKiKVjXxsjvNbnqg"

# r = requests.get(
#     BASE_URL + "artists/" + artist_id + "/albums",
#     headers=headers,
#     params={"include_groups": "album", "limit": 30},
# )
# d = r.json()

# # for album in d["items"]:
# #     try:
# #         print(album["name"], "---", album["release_date"])
# #     except UnicodeEncodeError:
# #         print(album["name"].encode("utf-8"), "---", album["release_date"])

# data = []
# albums = []

# for album in d["items"]:
#     album_name = album["name"]

#     trim_name = album_name.split("(")[0].strip()
#     # if trim_name.upper() in albums or int(album['release_date'][:4]) > 1983:
#     #     continue
#     albums.append(trim_name.upper())

#     # print(album_name)

#     r = requests.get(BASE_URL + "albums/" + album["id"] + "/tracks", headers=headers)
#     tracks = r.json()["items"]

#     for track in tracks:
#         f = requests.get(BASE_URL + "audio-features/" + track["id"], headers=headers)
#         f = f.json()

#         f.update(
#             {
#                 "track_name": track["name"],
#                 "album_name": album_name,
#                 "short_album_name": trim_name,
#                 "release_date": album["release_date"],
#                 "album_id": album["id"],
#             }
#         )

#         data.append(f)

# df = pd.DataFrame(data)

# df["release_date"] = pd.to_datetime(df["release_date"])
# df = df.sort_values(by="release_date")

# print(df.head())
