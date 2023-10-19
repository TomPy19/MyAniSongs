from get_user_list import get_user_list
from get_show_data import get_show_data
from parse_data import parse_data
from flask import Flask
from os import mkdir, listdir
import json

app = Flask(__name__)

users = listdir('../lists/users')

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route("/users")
def get_users():
  return users

@app.route("/user/<user>")
def get_user_mas_list(user):
  if user in users:
    return json.load(open(f'../lists/users/{user}/parsed_data.json', 'r'))
  else:
    return {"message": "User not found."}, 404

@app.route("/add/<user>") # type: ignore
def add_user(user):
  if user in users:
    return {"message": "User already exists."}, 500
  else:
    mkdir(f'../lists/users/{user}')
    access_token = "32ef86fd993671eb0a7281d3031f0be4"
    
    url = f'https://api.myanimelist.net/v2/users/{user}/animelist'
    user_list = get_user_list(access_token, url, {}, 0)

    show_data = get_show_data(user_list)
    print("User list obtained successfully.")

    data = json.dump(show_data, open('lists/show_data.json', 'w'), indent=2)
    # print(show_data[0])


    parse_data(show_data)
    print("Data parsed successfully")

    # print("Opening list obtained successfully.")
    return {"message": "User added successfully."}, 200

if __name__ == "__main__":
  app.run(debug=True, host='172.17.0.4', port=5020)




