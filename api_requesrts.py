import requests

url = "https://stats.pika-network.net/api/profile/HannahHaven"
response = requests.get(url)
data = response.json()
level = data["rank"]["level"]
print(level)