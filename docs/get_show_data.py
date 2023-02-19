import requests

def get_show_data(user_list):
  shows = {}
  i=0

  for entry in range(len(user_list)):
    show_data = query_name(user_list[entry]["title"], user_list[entry]["id"])
    if show_data:
      shows[i] = show_data["search"]
      print(show_data["search"]["anime"][0]["name"])
      i+=1

  return shows
  # with open('lists/show_data.json', 'w') as outfile:
  #   json.dump(shows, outfile, indent=2)

def query_name(name, id):
  url = f'https://api.animethemes.moe/search'
  
  params = {
    "q":
      name,

    "page[limit]":
      1,

    "include[anime]":
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
      "external_id,site"

  }

  show_data = requests.get(url, params=params)
  # limit = show_data.request.headers
  # print(f'RateLimit Remaining: {limit}')
  # print (show_data.request.url)
  show_data = show_data.json()

  if show_data["search"]["anime"][0]["resources"][0]["site"] == 'MyAnimeList':
    mal_id = show_data["search"]["anime"][0]["resources"][0]["external_id"]
  else:
    mal_id = 0
  
  if mal_id == id:
    return show_data
  return