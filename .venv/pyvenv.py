responses = [
    {
"status_code": 200,
 "body": {
  "username": "alice",
   "token": "abc123"
   }

    },
    {
        "status_code": 401,
        "body": {
            "error": "invalid credentials"
        }
        },
        {
            "status_code" : 200,
            "body": {
                "username": "bod",
                "token": ""
            }

        },
        {


            "status_code": 500,
            "body": {
                "error":"internal server error"
            }

        }
    ]

def validate_response(response):
    if response.get("status_code") == 200:
     body = response.get("body", {})
     if "username" in body and "token" in body and body["token"] != "":
      return "PASS"
    else:
      return "FAIL"
for response in responses:
 print(validate_response(response))