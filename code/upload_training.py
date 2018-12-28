import requests 
import json
import os
import random

BASE_URL = 'https://app.nanonets.com/api/v2/ImageCategorization/UploadFile/'
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')


categories = ["nsfw","sfw"]
image_folder_path = "./data"

import requests

def upload():
    for c in categories:
        for filename in os.listdir(image_folder_path + "/" + c):
            data = {'file' :open(image_folder_path + "/" + c + "/" + filename, 'rb'),'category' :('', c), 'modelId' :('', MODEL_ID)}

            response = requests.post(BASE_URL, auth= requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
            print response.text


if __name__=="__main__":
    upload()
    print("\n\nNEXT RUN: python ./code/train_model.py")