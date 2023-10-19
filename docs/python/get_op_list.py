import json
from get_urls import get_urls

def get_op_list(show_data):
  op_list = {}
  for i in range(len(show_data)):
    op_list[i] = {
      "name": show_data[i]["anime"]["title"]
    }
