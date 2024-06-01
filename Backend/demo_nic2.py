import sys
import time
import schedule
import json
from datetime import datetime
import base64
import requests
import hashlib
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import urllib.request

DEVICE_ID = "SENDEV-00048-1"



# # Save console output to a file
# class Logger(object):
#     def __init__(self, filename='console_output2.txt'):
#         self.terminal = sys.stdout
#         self.log = open(filename, 'a')
#
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
#         self.flush()
#
#     def flush(self):
#         self.terminal.flush()
#         self.log.flush()

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = None
        self.filename = None
        self.update_log_file()

    def update_log_file(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"log_{current_date}.txt"

        if self.filename != filename:
            if self.log is not None:
                self.log.close()
            self.filename = filename
            self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger()


def is_internet_available():
    try:
        urllib.request.urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError:
        return False


def third_request():
    with open('demo_auth.txt', 'r') as file:
        auth_details = eval(file.read())
        print(auth_details)

    auth_key = auth_details['key']
    current_datetime = datetime.now()
    my_datetime = current_datetime.strftime("%Y-%m-%d,%H:%M:%S")

    with open('flow.txt','r') as file2:
        flow = file2.read()
        file2.close()

    with open('qty.txt','r') as file3:
        qty = file3.read()
        file3.close()

    # define the data
    data = {
        "id": DEVICE_ID,
        "loc": "85.0818,21.0930",
        "ts": my_datetime,
        "flow": flow,
        "qty": qty,
        "roll": 0,
        "key": auth_key,
    }
    print(data)

    data_str = json.dumps(data)
    print(data_str)

    # calculate the SHA256 hash of the JSON package
    sha_value = hashlib.sha256(json.dumps(data_str).encode()).hexdigest()

    data2 = {
        "payload": data_str,
        "hash": sha_value,
    }
    print('json_payload:', data2)

    with open('data.json', 'w') as f:
        json.dump(data2, f)


def encrypt():
    with open('data.json', 'r') as f:
        data = json.load(f)
        json_data = json.dumps(data).encode('utf-8')

        public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhaquLhBuXpql1jS5OC5dxDuUgc8EwllLpry3onbFBCllAKFgPomtmmy45sIq30pIq1sEpYbLqxRyx7/JWxp8P/m1GgL6zNicub/V15GpIf7vTrZ0vUjl+gKCF/MowLQMzevU2jTEKwG9ptyUaBwmDOhczjpOEbAxKB48ZuakXte4Ly0kdBW9k+uouQliDGxIjdF/YeDqNpsN8u5h7W2t6V0M/SGr1fCCKGE9HcArTDK+rtIAWdDfe7ialmB8p7e4MwGCdratSvOciksJTNgZm/jyuPMAlxlAD105k56pNwaFCjTa9T7A19z1KpNBQrFqpXNpbxjfqbh4nzqRms5gvwIDAQAB'
        public_key_decode = base64.b64decode(public_key)
        public_key_obj = RSA.import_key(public_key_decode)

        cipher = PKCS1_OAEP.new(public_key_obj)
        block_size = 190
        plaintext_blocks = [json_data[i:i + block_size] for i in range(0, len(json_data), block_size)]

        encrypted_blocks = []
        for block in plaintext_blocks:
            encrypted_block = cipher.encrypt(block)
            encrypted_blocks.append(encrypted_block)

        encrypted_payload = b''.join(encrypted_blocks)
        encrypted_payload_base64 = base64.b64encode(encrypted_payload).decode()
        print('Encrypted value is...........................:', encrypted_payload_base64)

        # send the encrypted data to the server
        url = "https://api.industrialwaterod.nic.in/main"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=encrypted_payload_base64, headers=headers)
        print(response)



def execute_main_logic():
    third_request()
    try:
        encrypt()
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)


schedule.every(15).minutes.do(execute_main_logic)

if __name__ == '__main__':
   # Run the scheduled tasks indefinitely
   while True:
    schedule.run_pending()
    time.sleep(900)
