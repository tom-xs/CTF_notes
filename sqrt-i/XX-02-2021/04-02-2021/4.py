import requests

response = requests.get("http://oreos.ctfchallenge.ga/")

s = []

for i in response.history:
    s.append(i.headers)

for i in s:
    print(i)
