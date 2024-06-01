import time
from time import sleep

import requests

DEVICE_ID = "SENDEV-00048-1"

# Step 1: Request a new key from the server

def first_request():

    auth_url = "https://api.industrialwaterod.nic.in/auth"
    auth_body = {
        "id": DEVICE_ID,
        "new": True
    }

    response = requests.post(auth_url, json=auth_body)
    # print(response)


    if response.status_code == 200:
        return response.json()
        print(response.json())
        exit()
    else:
        print("Authentication failed:", response.status_code)
        exit()
################################JavaScript Code converted to Python code ##############################

def get_value():
    exp = first_request()
    data = exp['auth']
    check_string = data
    for index in range(len(check_string)):
        if check_string[index] in "1773946841":
            check_string = check_string[:index] + chr(ord(check_string[index]) + 1) + check_string[index + 1:]
        elif check_string[index] == '9':
            check_string = check_string[:index] + '0' + check_string[index + 1:]
        elif check_string[index] == 'a':
            check_string = check_string[:index] + 'z' + check_string[index + 1:]
        elif check_string[index] == 'A':
            check_string = check_string[:index] + 'Z' + check_string[index + 1:]
        else:
            check_string = check_string[:index] + chr(ord(check_string[index]) - 1) + check_string[index + 1:]
    for index in range(len(check_string)):
        if check_string[index] in "5070316844":
            temp = check_string[int(check_string[index]):]
            temp2 = check_string[:int(check_string[index])]
            check_string = temp + temp2

    return check_string


# Step 2: verify new key from the server

def second_request():
    exp = first_request()
    chck_str = get_value()
    print(chck_str)
    print(exp)

    auth_url = "https://api.industrialwaterod.nic.in/auth"
    auth_body = {
        "id": DEVICE_ID,
        "Key_Type": "Auth",
        "Dt_Expire": exp['expire'],
        "auth": chck_str}

    try:
        response = requests.post(auth_url, json=auth_body)
        print(response)
        response.raise_for_status()
        print(response.json())
        data = response.json()
        print(data)

        with open('demo_auth.txt', 'w') as file2:
            file2.write(str(data))
            return data

    except requests.exceptions.HTTPError as err:
        print(err)
        print(err.response.text)
        exit()


# def update_auth_txt():
#     while True:
#         # Perform the second request and update auth.txt
#         data = second_request()
#         #Wait for one hour before the next update
#         sleep(3600)
#
# update_auth_txt()

if __name__ == '__main__':
    while True:
      second_request()
      time.sleep(600)
