
import requests
from requests.auth import HTTPBasicAuth
import json 
import simplejson
import base64
import time

url = "https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/"
headers = {
    'Content-Type': "application/json"
    }

time.sleep(3)
response = requests.get("https://mobile.bestdoctorsinsurance.com/spiritapi/api/claim/policymembers/019000014", headers=headers,auth=("BD17603-01","N85FZRFSZC11RTSJOJQE40QQN3IGDT1J"))

print(response.text)
