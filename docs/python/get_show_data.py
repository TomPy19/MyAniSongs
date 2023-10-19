import requests

def get_show_data(user_list):
  ids = ""
  ids+=user_list[0]["id"]

  for entry in range(len(user_list)-1):
    ids+=","+user_list[entry+1]["id"]
  shows = query_name(ids) 

  return shows
  # with open('lists/show_data.json', 'w') as outfile:
  #   json.dump(shows, outfile, indent=2)

def query_name(ids):
  list_data = {"anime": []}

  url = f'https://api.animethemes.moe/anime'
  
  params = {

    "include":
      "animethemes.song.artists,animethemes.animethemeentries.videos,resources",
    
    "fields[search]":
      "anime",

    "fields[anime]":
      "year,name",

    "fields[song]":
      "title",

    "fields[artist]" :
      "name",

    "fields[animetheme]":
      "type,sequence",

    "fields[video]":
      "resolution,link",

    "fields[animethemeentry]":
      "id",

    "fields[resource]":
      "external_id,site",

    "filter[external_id]":
      ids,

    "filter[site]":
      "MyAnimeList",

    "page[number]":
      1
  }



  return requests.get(url, params=params).json()