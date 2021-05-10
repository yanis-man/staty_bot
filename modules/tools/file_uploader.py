import base64
import requests
import os
import json

from modules.configs.config import FileConfig

cfg = FileConfig()

def upload_image(path):
    with open(path, "rb") as filee:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key" : cfg.API_KEY,
            "image": base64.b64encode(filee.read()),
        }
        res = requests.post(url, payload)
        parsed = json.loads(res.text)
        return parsed['data']['url']