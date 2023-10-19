import requests
import json

def get_show_data(user_list):
  ids = ""
  ids+=f'{user_list[0]["id"]}'

  for entry in range(len(user_list)-1):
    ids+=f',{user_list[entry+1]["id"]}'
  show_data = query_name(ids) 

  return show_data

def query_name(ids):
  list_data = {"anime": []}

  url = f'https://api.animethemes.moe/anime'
  
  params = {

    "include":
      "animethemes.song.artists,animethemes.animethemeentries.videos,resources",

    "filter[site]":
      "MyAnimeList",
    
    "filter[external_id]":
      ids,

    "filter[has]":
      "resources",

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

    "page[number]":
      1
  }

  response = requests.get(url, params=params).json()
  i=1
  print(f'Reading page {i}...')
  i+=1
  next = response["links"]["next"]
  list_data["anime"].extend(response["anime"])

  while next:
    response = requests.get(next).json()
    next = response["links"]["next"]
    list_data["anime"].extend(response["anime"])
    print(f'Reading page {i}...')
    i+=1

  # with open(f'../lists/users/{user}/show_data.json', 'w') as outfile:
  #     json.dump(list_data, outfile, indent=2)

  return list_data