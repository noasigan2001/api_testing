import requests
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)
assert response.status_code == 200
data = response.json()
print(data["name"])
print(data["email"])
print(data["username"])
print(data["id"])

assert data["id"] == 1
assert data["username"] == "Bret"

print(data["address"]["city"])

data ={
    "status": "success",
    "user": {
    "name": "sarah",
    "age": 25,
    "premium": True
  }
 }
print(data["status"])
print(data["user"]["name"])
print(data["user"]["premium"])


