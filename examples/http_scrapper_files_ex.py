from typing import KeysView
import requests
import json
import os

def get_http_request_up(): 
    url = "https://www.datos.gov.co/resource/a8xr-en99.json?$limit=1"
    response = requests.get(url)
    #json_response = json.dumps(response.text, sort_keys=True, skipkeys=None, separators='cama:')
    return response.text

def save_json_labels(json_response):
    with open('/home/alev/personalProjects/WebScrapper/examples/personal.json', 'w') as json_file:
        json.dump(json_response,json_file)
        #json.dump(json_response, json_file)
         #json_file.writelines("%sn" % line for line in json_response)

def load_json_labels():
    with open('/home/alev/personalProjects/WebScrapper/examples/personal.json') as json_file: 
        data = json.load(json_file)
        jtopy=json.dumps(data, indent= 4) #json.dumps take a dictionary as input and returns a string as output.
        dict_json=json.loads(jtopy) # json.loads take a string as input and returns a dictionary as output.
    return dict_json

if __name__ == '__main__':
    response = get_http_request_up()
    save_json_labels(response)
    data_space = load_json_labels()
    print(data_space)
    