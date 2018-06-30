import requests
import json

# Project using Open Notify API to find the position of the
# Internationals Space Station - iss
api_base_url = "http://api.open-notify.org"
current_position_url = "http://api.open-notify.org/iss-now.json"
false_url = "http://api.open-notify.org/iss-pass"
iss_pass = "http://api.open-notify.org/iss-pass.json"

# How many people are in space?
astronomers_in_space = "http://api.open-notify.org/astros.json"

# Nairobi coordinates
parameters = {
    'lat':'-1.28333',
    'lon': '36.81667'
}

response = requests.get(iss_pass, params=parameters)
data = response.json()
print(type(data))
print(data)

print(response.headers)
print(response.headers["content-type"])

# How many people are in space
response_peeps = requests.get(astronomers_in_space)
data = response_peeps.json()
print(f" The number of people in space: {data['number']}")

# Names of people in space
for n in range(0, len(data['people'])):
    print(data['people'][n]['name'])

# #latest position of the isp
# response = requests.get(current_position_url)
# print(response.status_code)
#
# #Error 404 - file not found
# falseurl_response = requests.get(false_url)
# print(falseurl_response.status_code)
#
# #Bad Request
# response2 = requests.get(url2)
# print(response2.status_code)

