# Save internet data into a file
import json
import requests

url = "http://citibikenyc.com/stations/json"

# Make the request
response = requests.get(url)

# Check if response code is successful
if response.status_code == 200:
    # open write header details to external file
    with open('headers.json', 'w') as header_file:
        if header_file.writable():
            header_data = json.dumps(response.headers.__dict__['_store'])
            header_file.write(header_data)

    # open and write data to external file: data.json
    with open('data.json', 'w') as data_file:
        if data_file.writable():
            json_data = json.dumps(response.json())
            data_file.write(json_data)


