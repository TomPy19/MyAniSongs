import requests
import json

def get_user_list(access_token: str, url, result, it):
  response = requests.get(url, headers = {
        'X-MAL-CLIENT-ID': access_token
        })
  response.raise_for_status()
  list = response.json()
  response.close()

  try:
    data = list["data"]
    for i in range(len(data)):
      result[i+(it*10)] = {"id": data[i]["node"]["id"], "title": data[i]["node"]["title"]}
  except:
    result = result

  try:
    next_url = list["paging"]["next"]
  except KeyError:
    next_url = 0

  if next_url:
    it+=1
    get_user_list(access_token, next_url, result, it)

  with open('lists/user_list.json', 'w') as outfile:
    json.dump(result, outfile, indent=2)
  outfile.close()
  
  return result