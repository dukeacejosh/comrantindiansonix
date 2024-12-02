import os
import json as jsond  # json
import time  # sleep before exit
import binascii  # hex encoding
from uuid import uuid4  # gen random guid
import platform  # check platform
import subprocess  # needed for mac device
import hmac  # signature checksum
import hashlib  # signature checksum

try:
    if os.name == 'nt':
        import win32security  # get sid (WIN only)
    import requests  # https requests
except ModuleNotFoundError:
    print("Exception when importing modules")
    print("Installing necessary modules....")
    if os.path.isfile("requirements.txt"):
        os.system("pip install -r requirements.txt")
    else:
        if os.name == 'nt':
            os.system("pip install pywin32")
        os.system("pip install requests")
    print("Modules installed!")
    time.sleep(1.5)
    os._exit(1)

class api:

    name = ownerid = secret = version = hash_to_check = ""

    def __init__(self, name, ownerid, secret, version, hash_to_check):
        # Bypass initialization check
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.hash_to_check = hash_to_check
        self.sessionid = "bypass_session_id"
        self.initialized = True
        print("Cracked by oldfriend2.0 - discord.gg/vertexai")

    sessionid = enckey = ""
    initialized = False

    def init(self):
        # Bypass actual server init
        print("Cracked by oldfriend2.0 - discord.gg/vertexai")
        self.sessionid = "bypass_session_id"
        self.initialized = True

    def register(self, user, password, license, hwid=None):
        self.checkinit()
        print(f"Bypassed registration for user: {user}")
        # Mock setting user data
        self.__mock_user_data(user)

    def login(self, user, password, hwid=None):
        self.checkinit()
        print(f"Bypassed login for user: {user}")
        # Mock setting user data
        self.__mock_user_data(user)

    def license(self, key, hwid=None):
        self.checkinit()
        print(f"License key valid: {key}")
        # Mock setting user data
        self.__mock_user_data("bypassed_user")

    def var(self, name):
        self.checkinit()
        print(f"Bypassed var retrieval for: {name}")
        return "bypassed_value"

    def getvar(self, var_name):
        self.checkinit()
        print(f"Bypassed getvar for: {var_name}")
        return "bypassed_value"

    def setvar(self, var_name, var_data):
        self.checkinit()
        print(f"Bypassed setvar for: {var_name} with data: {var_data}")
        return True

    def ban(self):
        self.checkinit()
        print("Bypassed ban")
        return True

    def file(self, fileid):
        self.checkinit()
        print(f"Bypassed file retrieval for: {fileid}")
        return binascii.unhexlify("bypassed_file_content")

    def check(self):
        self.checkinit()
        print("Bypassed check")
        return True

    def log(self, message):
        self.checkinit()
        print(f"Bypassed log for message: {message}")

    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            time.sleep(3)
            os._exit(1)

    def __do_request(self, post_data):
        # Mocking actual HTTP request
        print(f"Bypassed request for type: {post_data['type']}")
        return '{"success": true, "message": "Bypassed request"}'

    def __mock_user_data(self, user):
        # Mock user data for bypass
        self.user_data.username = user
        self.user_data.ip = "127.0.0.1"
        self.user_data.hwid = "bypass_hwid"
        self.user_data.expires = "9999999999"
        self.user_data.createdate = "9999999999"
        self.user_data.lastlogin = "9999999999"
        self.user_data.subscription = "Bypassed Subscription"
        self.user_data.subscriptions = [{"subscription": "Bypassed Subscription", "expiry": "9999999999", "timeleft": "Unlimited"}]

    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = subscriptions = ""

    user_data = user_data_class()

class others:
    @staticmethod
    def get_hwid():
        return "bypassed_hwid"