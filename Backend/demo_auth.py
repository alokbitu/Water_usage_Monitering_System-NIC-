import time
import requests

DEVICE_ID = "SENDEV-00069-1"


# Step 1: Request a new key from the server
def first_request():
    auth_url = "https://api.industrialwaterod.nic.in/auth"
    auth_body = {
        "id": DEVICE_ID,
        "new": True
    }

    response = requests.post(auth_url, json=auth_body)

    if response.status_code == 200:
        return response.json()
    else:
        print("Authentication failed:", response.status_code)
        exit()


# JavaScript Code converted to Python code
def get_value():
    exp = first_request()
    data = exp['auth']
    check_string = data
    for index in range(len(check_string)):
        if check_string[index] in "3860043055":
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
        if check_string[index] in "7044822358":
            temp = check_string[int(check_string[index]):]
            temp2 = check_string[:int(check_string[index])]
            check_string = temp + temp2

    return check_string


# Step 2: verify new key from the server
def second_request():
    try:
        exp = first_request()
        chck_str = get_value()

        auth_url = "https://api.industrialwaterod.nic.in/auth"
        auth_body = {
            "id": DEVICE_ID,
            "Key_Type": "Auth",
            "Dt_Expire": exp['expire'],
            "auth": chck_str
        }

        response = requests.post(auth_url, json=auth_body)
        response.raise_for_status()
        data = response.json()

        with open('demo_auth.txt', 'w') as file2:
            file2.write(str(data))

        return True

    except requests.exceptions.RequestException as err:
        print("An error occurred:", err)
        return False


if __name__ == '__main__':
    while True:
        success = second_request()
        if success:
            time.sleep(30)  # If successful, sleep for 15 minutes
        else:
            time.sleep(60)  # If there's an error, restart within 1 minute
