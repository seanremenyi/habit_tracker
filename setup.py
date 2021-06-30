import requests
#this will create a new user for pixela https://docs.pixe.la/
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "{enter a custom password here}",
    "username": "{enter a username here}",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
