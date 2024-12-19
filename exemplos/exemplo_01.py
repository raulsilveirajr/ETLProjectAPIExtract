import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response, "\n\n")
print(response.text, "\n\n")
print(response.headers, "\n\n")
print(response.json(), "\n\n")

print(response.status_code)
print(response.status_code == requests.codes.ok)
