from urllib.request import urlopen
import json
import csv

api_url = 'https://acnhapi.com/v1/'

api_data = urlopen(api_url + 'bugs')

api_data = api_data.read()

data = json.loads(api_data)

with open('bug_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    headers = ['Name', 'ID', 'Time']

    writer.writerow(headers)

    for bug in data:
        b = [
            data[bug]['name']['name-USen'], 
            data[bug]['id'], 
            data[bug]['availability']['time']
        ]
        writer.writerow(b)

