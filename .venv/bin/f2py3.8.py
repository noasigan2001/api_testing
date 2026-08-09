import  requests

url = "https://example.com/login"

payload = {
    "username": "test_user",
    "password": "correct_password"
}
response = requests.post(url, json=playload)

assert response.status_code == 200
data = response.json()

assert "token" in data