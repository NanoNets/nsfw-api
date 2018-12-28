<div align="center">
  <a href="https://nanonets.com/objectdetection/">
    <img src="https://nanonets.com/logo.png" alt="NanoNets Object Detection Python Sample" width="100"/>
    </a>
</div>

<h1 align="center">Nanonets NSFW API</h1>

<a href="https://nanonets.com/content-moderation-api/"> <h3>Live demo</h3> </a>

| [Golang Sample](https://repl.it/@RushabhNagda/go-example-url) | [Python Sample](https://repl.it/@RushabhNagda/go-example-url)| [Node.js Sample](https://repl.it/@RushabhNagda/go-example-url) |
| -------------------------- |--------------------------|--------------------------|
| [![](https://www.hugopicado.com/assets/golang.png)](https://github.com/NanoNets/object-detection-sample-golang) | [![](http://kata.coderdojo.com/images/thumb/e/ea/Python_logo.png/100px-Python_logo.png)](https://github.com/NanoNets/object-detection-sample-python) | [![](https://s3.amazonaws.com/openshift-hub/production/quickstarts/243/nodejs_custom.png?1456926624)](https://github.com/NanoNets/object-detection-sample-nodejs) |

** **

## Usage



We're classifying images into NSFW and SFW categories.

Following are the image categories we classify into NSFW categories.
* Porn
* Explicit Nudity
* Animated Porn
* Suggestive Nudity
* Gore

### Query pretrained model.

You can query our pretrained model which should work for most use cases. If you want to build your own custom model tailored to your use case, skip ahead to the next section.

Few integration code samples are provided below.

## Model ID : 7390a500-9fe1-483b-8123-750b96fc660

* Get your API key by signing up on <a href="app.nanonets.com">app.nanonets.com</a>

#### curl

```bash
curl --request POST --url 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/' --header 'accept: application/x-www-form-urlencoded' -d 'modelId=7390a500-9fe1-483b-8123-750b96fc660c&urls=https://goo.gl/ICoiHc' -u '-REPLCAE_YOUR_API_KEY:'
```

#### python

```python
#REPLACE YOUR API KEY
 
import requests
 
url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/'
 
headers = {
  'accept': 'application/x-www-form-urlencoded'
}
 
data = {'modelId': '7390a500-9fe1-483b-8123-750b96fc660c', 'urls' : ['https://goo.gl/ICoiHc']}
 
response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('REPLACE_YOUR_API_KEY', ''), data=data)
 
print(response.text)

```

#### node

```javascript
var request = require("request");
  
var options = { method: 'POST',
  url: 'http://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/',
  headers:
  { 'cache-control': 'no-cache',
    Authorization: 'Basic ' + new Buffer('REPLACE YOUR API KEY' + ":" + '').toString("base64"),
    'Content-Type': 'application/x-www-form-urlencoded' },
  form:
  { urls: 'https://goo.gl/ICoiHc',
    modelId: '7390a500-9fe1-483b-8123-750b96fc660c' } };

request(options, function (error, response,body) {
  if (error) throw new Error(error);

  console.log(body);
});
```
** **

## Train your own NSFW model

 
### Step 1: Clone the Repo
```bash
git clone https://github.com/NanoNets/nsfw-api
cd nsfw-api
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/#/keys

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create_model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in ```data```
```bash
python ./code/upload_training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train_model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model_state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./data/nsfw/2795.jpg
```



