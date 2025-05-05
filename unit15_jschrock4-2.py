import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers)
print(f"Status Code: {response.status_code}")
response_dict = response.json()

print(response_dict["items"])
