import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}
headers = {"Accept": "application/json"}
response = requests.get(url, params=params, headers=headers)
print(response, "\n\n")
print(response.text, "\n\n")
print(response.headers, "\n\n")
print(response.json(), "\n\n")

print(f"Foram encontrados {len(response.json())} comentários\n\n")

print(response.status_code)
print(response.status_code == requests.codes.ok)
