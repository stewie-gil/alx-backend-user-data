#!/usr/bin/env python3
import requests

base_url = 'http://127.0.0.1:5000/{}'

def register_user(email: str, password: str) -> None:
    url = base_url.format('users')
    expected_status_code = 200
    expected_data = {"email":email, "message":"user created"}
    
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)
    actual_status_code = response.status_code
    actual_data = response.json()
   
    assert actual_status_code == expected_status_code
    

def log_in_wrong_password(email: str, password: str) -> None:
    url = base_url.format('sessions')
    expected_code = 401
    

    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=data)
    actual_status_code = response.status_code
    
    assert actual_status_code == expected_code
    

def log_in(email: str, password: str) -> str:
    url = base_url.format('sessions')
    expected_status_code = 200

    data = {
        "email" : email,
        "password": password
        }

    response = requests.post(url, data=data)
    expected_status_code = response.status_code

    assert actual_status_code == expected_stauts_code
    return response.cookies.get('session_id')

def profile_unlogged() -> None:
    url = base_url.format('profile')
    expected_status_code = 403

    response = requests.post(url)
    actual_status_code = response.status_code 
    assert actual_status_code == expected_status_code

def profile_logged(session_id: str) -> None:
    url = base_url.format('profile')
    expected_status_code = 200
    requests.set_cookies('session_id', session_id)

    response = requests.get(url)
    actual_status_code = response.status_code
    assert actual_status_code == expected_status_code

def log_out(session_id: str) -> None:
    url = base_url.format('sessions')
    expected_status_code = 200

    requests.set_cookies('session_id', session_id)

    response = request.delete(url)

    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code

def reset_password_token(email: str) -> str:
    url = base_url.format('reset_password')
    expected_status_code = 200

    data = {"email": email}
    response =  requests.post(url, data=data)
    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code
    return response["reset_token"]

def update_password(email: str, reset_token: str, new_password: str) -> None:
    url = base_url.format('reset_password')
    expected_status_code = 200

    data = {
        "email ": email,
        "reset_token": reset_token,
        "new_password": new_password
    }

    response = request.put(url, data=data)

    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code
    



EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
