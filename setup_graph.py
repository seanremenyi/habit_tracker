import requests

#Creates graph on pixela

USERNAME = "{created in user setup}"
TOKEN = "{created in user setup}"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "{id for graph}",
    "name": "{title of graph}",
    "unit": "{measurement unit}",
    "type": "float",
    "color": "{color, note it is with japanese names}"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
#Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID>.html API.