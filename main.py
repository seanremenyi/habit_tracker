import requests
from datetime import datetime

USERNAME = "{Your Username}"
TOKEN = "{The token you created}"
GRAPH_ID = "{Your graph id}"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "{title of graph}",
    "unit": "{measurement unit}",
    "type": "float",
    "color": "{color, note it is with japanese names}"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "{quantity of the habit you are tracking}",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

