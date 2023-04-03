import requests
from datetime import datetime

USER_TOKEN = "Your Pixela Token"
USERNAME = "umutbasaran"
GRAPH_ID = "Your Pixela Graph ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_header = {
    "X-USER-TOKEN": USER_TOKEN
}

graph_body = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_body, headers=graph_header)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

add_pixel_body = {
    "date": formatted_today,
    "quantity": "5.30"
}

# response = requests.post(url=add_pixel_endpoint, json=add_pixel_body, headers=graph_header)
# print(response.text)

put_delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"

put_pixel_body = {
    "quantity": "6"
}

# response = requests.put(url=put_delete_pixel_endpoint, json=put_pixel_body, headers=graph_header)
# print(response.text)

response = requests.delete(url=put_delete_pixel_endpoint, headers=graph_header)
print(response.text)
