from typing import KeysView
import requests
import json
import os

def get_http_request_up(): 
    url = "https://www.datos.gov.co/resource/a8xr-en99.json?$limit=1"
    response = requests.get(url)
    json_response = json.dumps(response.json(), sort_keys=True, skipkeys=False, indent=4)
    return json_response

def save_json_labels(json_response):
    with open('/home/alev/personalProjects/WebScrapper/examples/personal.json', 'w') as json_file:
        json.dump(json_response, json_file)
        #json_file.writelines("%sn" % line for line in json_response)

def load_json_labels():
    with open('/home/alev/personalProjects/WebScrapper/examples/personal.json') as json_file: 
        data = json.load(json_file) 
    return data

if __name__ == '__main__':
    response = get_http_request_up()
    print(response)
    