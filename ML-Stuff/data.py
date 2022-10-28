import requests

url = "http://192.168.43.181/"

data = requests.get(url).text

with open("data.txt","a") as f:
    f.write(data)