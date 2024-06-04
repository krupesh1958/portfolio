import pprint
import requests
import json

github_url = "https://api.github.com/users/krupeshgithub/repos?per_page=100&page=1"

resp = requests.get(github_url).json()
with open("./temp.json", "w") as file:
    json.dump(resp, file)
