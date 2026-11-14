import requests

response = requests.get("https://api.github.com/users/MaksimFomenko")
print(response.status_code)
print(response.json())

data = response.json()
print(data["public_repos"])
print(data["created_at"])