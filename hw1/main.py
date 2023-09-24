import requests

import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def get_notMe(token):
    resource = requests.get(data["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return resource.json()

def get_Me(token):
    resource = requests.get(data["url_posts"],
                            headers={"X-Auth-Token": token},
                           )
    return resource.json()
