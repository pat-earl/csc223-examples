from urllib.request import urlopen
import json
import csv
import pprint

api_url = 'https://acnhapi.com/v1/'

api_request = urlopen(api_url + 'bugs')

api_request = api_request.read()

data = json.loads(api_request)

with open('bug_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    headers = ['Name', 'ID', 'Rarity']

    writer.writerow(headers)

    for bug in data:
        b = [
            data[bug]['name']['name-USen'], 
            data[bug]['id'], 
            data[bug]['availability']['rarity']
        ]
        writer.writerow(b)