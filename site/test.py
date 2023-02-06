import requests
import json

data = requests.get("https://api.animethemes.moe/anime/akiba_maid_sensou?fields[anime]=slug,year&fields[song]=title&fields[animetheme]=type&fields[video]=resolution,source,tags,link&fields[animethemeentry]=id&fields[resource]=external_id,site&include=animethemes.song,animethemes.animethemeentries.videos,series,resources").json()

with open('test.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)