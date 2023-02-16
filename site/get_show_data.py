import requests
import json

def get_show_data(user_list):
  op_list = {}
  i=0

  for entry in range(len(user_list)):
    show_data = query_name(user_list[entry]["title"], user_list[entry]["id"])
    if show_data:
      op_list[i] = show_data
      print(show_data["anime"]["name"])
      i+=1

  with open('lists/show_data.json', 'w') as outfile:
    json.dump(op_list, outfile, indent=2)

def query_name(name, id):
  url = "https://api.animethemes.moe/search?q=" + name.replace(" ", "+")
  response = requests.get(url).json()
  show_data = get_show_data(response["search"]["anime"][0]["slug"], id)
  if show_data:
    return show_data
  return

def get_show_data(slug, id):
  # includes = 'include=animethemes.song,animethemes.animethemeentries.videos,series,resources'
  # fields = 'fields[anime]=name,year&fields[song]=title,artist&fields[animetheme]=type&fields[video]=resolution,source,tags,link'
  # fields = fields + '&fields[animethemeentry]=id&fields[resource]=external_id,site&fields[series]=name'
  url = f'https://api.animethemes.moe/anime/{slug}'
  
  params = {
    "include": [
      "animethemes.song",
      "animethemes.animethemeentries.videos",
      "series",
      "resources"
    ],
    "fields[anime]": [
      "year",
      "name"
    ],
    "fields[song]": [
      "title",
      "artist"
    ],
    "fields[animetheme]": [
      "type"
    ],
    "fields[video]": [
      "resolution",
      "source",
      "tags",
      "link"
    ],
    "fields[animethemeentry]": [
      "id"
    ],
    "fields[resource]": [
      "external_id",
      "site"
    ],
    "fields[series]": [
      "name"
    ]
  }
  
  show_data = requests.get(url, params).json()
  
  if show_data["anime"]["resources"][0]["site"] == 'MyAnimeList':
    mal_id = show_data["anime"]["resources"][0]["external_id"]
  else:
    mal_id = 0
  
  if mal_id == id:
    return show_data
  return