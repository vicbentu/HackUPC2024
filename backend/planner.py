import requests

"""
https://api.opentripmap.com/0.1/en/places/geoname?name=barcelona&apikey=5ae2e3f221c38a28845f05b6242e1ccfbd613b5fd4353bdb4029212d


"""

api_key = "5ae2e3f221c38a28845f05b6242e1ccfbd613b5fd4353bdb4029212d"
url = 'https://api.opentripmap.com/0.1/en/places/geoname'
parameters = {
    'apikey': api_key,
    'name': "barcelona"
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Failed to retrieve data:', response.status_code)


# response = (requests.get("http://api.opentripmap.com/0.1/en/places/xid/Q372040?apikey=5ae2e3f221c38a28845f05b6242e1ccfbd613b5fd4353bdb4029212d"))
# if response.status_code == 200:
#     data = response.json()
#     print(data)