import  requests

url = "https://example.com/login"

payload = {
    "username": "test_user",
    "password": "12345"
}

response = requests.post(url, json=payload)

data = response.json()

assert response.status.code == 200
assert " token" in data
assert data["user_id"] == 15
