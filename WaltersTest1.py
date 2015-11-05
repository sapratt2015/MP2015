import requests, json

r = requests.get('http://api.thewalters.org/v1/collections/3/objects?orderBy=ObjectID&apikey=NpMwnjS9mYjQZNihW2t3m3ORtONhOHWndHFTJXArEd4Kt70i8HQIlY5JQv3OLlkU')

print(r.status_code)

print(r.text)

#turn it into dictionary

data = json.loads(r.text)

print(data)

json_string = json.dumps(data)

print (json_string)

json_string = json.dumps(data, indent=4)

print (json_string)


