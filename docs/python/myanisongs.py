from get_user_list import get_user_list
from get_show_data import get_show_data
from parse_data import parse_data
from flask import Flask
from threading import Thread
from os import mkdir, listdir
import json

app = Flask(__name__)

users = listdir('../lists')

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route("/users")
def get_users():
  return users

@app.route("/user/<user>")
def get_user_mas_list(user):
  if user in users:
    return json.load(open(f'../lists/{user}/parsed_data.json', 'r'))
  else:
    return {"message": "User not found."}, 404

@app.route("/add/<user>")
def add_user(user):
  def obtain_mas_list():
    access_token = "32ef86fd993671eb0a7281d3031f0be4"

    url = f'https://api.myanimelist.net/v2/users/{user}/animelist'
    user_list = get_user_list(access_token, url, {}, 0)

    show_data = get_show_data(user_list)
    print("User list obtained successfully.")

    parse_data(show_data, user)
    print("Data parsed successfully")
  if user not in users:
    mkdir(f'../lists/{user}')
    Thread(target=obtain_mas_list).start()
    return {"message": "Obtaining user list..."}, 200
  else:
    if len(listdir(f'../lists/{user}')) == 0:
      Thread(target=obtain_mas_list).start()
      return {"message": "Obtaining user list..."}, 200
    else: return {"message": "User already exists."}, 500

@app.route("/refresh/<user>")
def refresh_user(user):
  def obtain_mas_list():
    access_token = "32ef86fd993671eb0a7281d3031f0be4"

    url = f'https://api.myanimelist.net/v2/users/{user}/animelist'
    user_list = get_user_list(access_token, url, {}, 0)

    show_data = get_show_data(user_list)
    print("User list obtained successfully.")

    parse_data(show_data, user)
    print("Data parsed successfully")
  if user in users:
    Thread(target=obtain_mas_list).start()
    return {"message": "User Found. Refreshing..."}, 200
  else:
    return {"message": "User not found."}, 404

@app.route("/get/<user>")
def get_user_data(user):
  if user in users:
    return json.load(open(f'../lists/{user}/parsed_data.json', 'r'))
  else:
    return {"message": "User not found."}, 404

if __name__ == "__main__":
  app.run(debug=True, host='172.17.0.4', port=5020)




