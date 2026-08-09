import requests

def test_login_success():
    response = requests.post(
                "https://api.example.com/login",
                 json={
                     username: "admin",
                     password: "1234"

                 }
    )
    assert response.status_code == 200
