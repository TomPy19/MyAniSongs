from get_user_list import get_user_list
from get_show_data import get_show_data
from parse_data import parse_data
import json

access_token = "32ef86fd993671eb0a7281d3031f0be4"

user = 'TomPy'
url = f'https://api.myanimelist.net/v2/users/{user}/animelist'
user_list = get_user_list(access_token, url, {}, 0)

show_data = get_show_data(user_list)
print("User list obtained successfully.")

data = json.dump(show_data, open('lists/show_data.json', 'w'), indent=2)
# print(show_data[0])


parse_data(show_data)
print("Data parsed successfully")

# print("Opening list obtained successfully.")