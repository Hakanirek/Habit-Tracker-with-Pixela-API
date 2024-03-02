import requests
from datetime import datetime
import os

USER_NAME = os.environ.get("USER_NAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# Creating a account in pixela
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

# Creating a new Graph in pixela
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling  Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Add a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you cycle today?")
}

pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)

# Updating the particular date  pixel
date = datetime(year=2023, month=11, day=5)
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
pixel_update_data = {
    "quantity": "4.5"
}
# update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(update_response.text)


# Updating the particular date pixel
# pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
# pixel_delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(pixel_delete_response.text)
