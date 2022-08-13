import requests

x=requests.get(url='https://api.sampleapis.com/futurama/characters')
print(x.json())