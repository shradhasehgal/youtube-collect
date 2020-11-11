import requests
from googleapiclient.discovery import build

query = "https://www.googleapis.com/youtube/v3/search?key={your_key_here}&channelId={channel_id_here}&part=snippet,id&order=date&maxResults=20"

try:
    response = requests.get(query)
except Exception as e: 
    response = none
    print(e)

if response:
    details = json.loads(response.content)
    for vid in details["items"]:
        print(vid["id"]["videoId"]) 
        print(vid["snippet"]["title"])
        print(vid["snippet"]["description"])