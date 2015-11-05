import requests, json

r = requests.get('http://www.brooklynmuseum.org/opencollection/api/?method=collection.search&version=1&api_key=31dg56cAuk&keyword=manuscripts')

print(r.status_code)

print(r.text)

#turn it into dictionary

data = json.loads(r.text)

print(data)

#prints up til here

json_string = json.dumps(data)

print (json_string)

json_string = json.dumps(data, indent=4)

print (json_string)






