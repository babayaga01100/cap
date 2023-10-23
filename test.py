import requests

url = 'http://127.0.0.1:8000/auth'

# response = requests.get(url)
response = requests.post(url, data={'username': 'admin', 'password': '123123'})

print(response.text)