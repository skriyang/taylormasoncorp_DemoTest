
import requests
import json
import time
import jsonpath

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

json_response = json.loads(response.text)
print(json_response)
#print(response.content)
print(response.headers)

print(response.status_code)

print(response.cookies)

print(response.url)
print(response.history)
print(response.raw)
print(response.request)

print(response.reason)
Request=response.reason
assert Request=='OK'

print(response.__attrs__)
print(response.__doc__)
print(json_response)

Encodings=response.encoding
assert Encodings=='utf-8'

cods=response.status_code
assert cods==200

#pages = jsonpath.JSONPath(json_response, 'title')
#print(pages)

print('Ene test')


