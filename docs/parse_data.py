import json

def hq(videos):
  h_res = 0
  hq = None
  for video in videos:
    if video["resolution"] > h_res:
      h_res = video["resolution"]
      hq = video["link"]
	
  return hq

def format_data(current_show, theme):
  artist = "N/A"
  sequence = 1
  if len(theme["song"]["artists"]) > 0:
    artist = theme["song"]["artists"][0]["name"]
  if not theme["sequence"] == None:
    sequence = theme["sequence"]

  return {
		"show_title": current_show["name"],
		"year": current_show["year"],
		"song_title": theme["song"]["title"],
		"artist": artist,
		"sequence": sequence,
		"hq_link": hq(theme["animethemeentries"][0]["videos"])
	}

def parse_data(data):
  # with open(path) as file:
  #   data = json.load(file)
  
  parsed_data = {}
  i=0
  
  for anime in range(len(data)):
    seq = []
    current_show = data[anime]["anime"][0]
    for theme in current_show["animethemes"]:
      if theme["type"] == "OP":
        if theme["sequence"] == "null":
          parsed_data[i] = format_data(current_show, theme)
          i+=1
        else:
          if not theme["sequence"] in seq:
            seq.append(theme["sequence"])
            parsed_data[i] = format_data(current_show, theme)
            i+=1
            
  with open('lists/parsed_data.json', 'w') as outfile:
    json.dump(parsed_data, outfile, indent=2)
    