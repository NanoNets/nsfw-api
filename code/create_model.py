import requests 
import json
import os

BASE_URL = 'http://app.nanonets.com/api/v2/ImageCategorization/Model/'
AUTH_KEY = os.environ.get('NANONETS_API_KEY')


categories = ["nsfw", "sfw"]
ext = ['.jpeg', '.jpg', ".JPG", ".JPEG"]


def create_new_model(categories):
    try:

        headers = {
            'accept': 'application/x-www-form-urlencoded'
        }

        data = {'categories' : ['nsfw', 'sfw']}

        response = requests.request("POST", BASE_URL, headers=headers, auth=requests.auth.HTTPBasicAuth(AUTH_KEY, ''), data=data)

        return json.loads(response.text)["model_id"]
    except:
        raise ValueError("Error in creating model")

if __name__=="__main__":
    model_id = create_new_model(categories)
    print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
    print("THEN RUN: python ./code/upload_training.py")
