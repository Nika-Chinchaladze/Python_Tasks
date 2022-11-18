import requests
from datetime import datetime
import os


my_api = os.environ.get("MY_API")
my_name = "chincho"
my_header = {
    "X-USER-TOKEN": my_api
}
my_graph = "graph1"
my_endpoint = "https://pixe.la/v1/users"

# =========================== Create Account =========================== #
my_account = {
    "token": my_api,
    "username": my_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=my_endpoint, json=my_account)
# print(response.text)

# =========================== Create Graph =========================== #
graph_endpoint = f"{my_endpoint}/{my_name}/graphs"
graph_parameters = {
    "id": my_graph,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=my_header)
# print(response.text)

# =========================== Add Data as Pixel =========================== #
today = datetime.now()
current_date = today.strftime("%Y%m%d")

pixel_endpoint = f"{my_endpoint}/{my_name}/graphs/{my_graph}"
pixel_parameters = {
    "date": current_date,
    "quantity": "9.83"
}
# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=my_header)
# print(response.text)

# =========================== Update Yesterday's Data =========================== #
yesterday = datetime(year=2022, month=11, day=17)
yesterday = yesterday.strftime("%Y%m%d")
put_endpoint = f"{my_endpoint}/{my_name}/graphs/{my_graph}/{yesterday}"
put_parameters = {
    "quantity": "2.78"
}
# response = requests.put(url=put_endpoint, json=put_parameters, headers=my_header)
# print(response.status_code)
# print(response.text)

# =========================== Delete Data =========================== #
delete_endpoint = f"{my_endpoint}/{my_name}/graphs/{my_graph}/{yesterday}"
response = requests.delete(url=delete_endpoint, headers=my_header)
print(response.status_code)
print(response.text)
