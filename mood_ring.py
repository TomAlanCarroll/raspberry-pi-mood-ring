import os
import http.client
import json

from urllib.parse import urlencode
from colors import face_emotions_to_color
from color_changer import color_changer
from camera import camera
from pprint import pprint


# Replace the subscription_key string value with your valid subscription key.
subscription_key = os.environ['AZURE_SUBSCRIPTION_KEY']
region = os.environ['REGION']

if subscription_key == 'Add your key here':
    raise Exception('Add your Azure key to config.properties. See README.md')

azure_api_base_uri = region + '.api.cognitive.microsoft.com'
# Request headers
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}
# Request parameters
params = urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,'
                            'accessories,blur,exposure,noise',
})

i = 1
file_name = camera.capture(i)
with open(file_name, 'rb') as image_file:
    image_bytes = image_file.read()
    conn = http.client.HTTPSConnection(azure_api_base_uri)
    conn.request('POST', '/face/v1.0/detect?%s' % params, image_bytes, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    parsed_response = json.loads(data)

    if not parsed_response:
        print('Picture could not be detected.')
    else:
        print('Response:')
        pprint(parsed_response)
        color_changer.change(color=face_emotions_to_color({}))
    conn.close()
i += 1
