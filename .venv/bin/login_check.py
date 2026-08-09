def login(username, password):
    username = input('enter your username: ')
    password = input('enter your password: ')

    if username == "admin" and password == "1234":
        return "200 login successful"
    elif username != "admin" and password == "1234":
        return " 401 username not found "
    elif username == "admin" and password != "1234":
        return "401 wrong password "
    else:
        return " invaild credentials "
print(login(username="admin",   password="1234"))