import requests
import pprint

BASE = "http://127.0.0.1:5000/"


response = requests.post(BASE + "url", json={"url": "https://www.google.com/"})
pprint.pprint(response.json())

input()
response = requests.get(BASE + "url/0OGWoM")
print(response.url)
