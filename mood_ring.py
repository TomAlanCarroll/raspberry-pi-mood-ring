import http.client
import json
import time

from config import AZURE_SUBSCRIPTION_KEY, REGION
from urllib.parse import urlencode
from colors import face_emotions_to_color, mood_ring_colors
from color_changer import color_changer
from camera import camera
from pprint import pprint

UPDATE_INTERVAL = 8  # Update every 8 seconds

if AZURE_SUBSCRIPTION_KEY == 'Add your key here':
    raise Exception('Add your Azure key to config.py. See README.md')

azure_api_base_uri = REGION + '.api.cognitive.microsoft.com'
# Request headers
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': AZURE_SUBSCRIPTION_KEY,
}
# Request parameters
params = urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,'
                            'accessories,blur,exposure,noise',
})

i = 1
while True:
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
        elif len(parsed_response) > 0:
            print('Response:')
            pprint(parsed_response[0]['faceAttributes']['emotion'])
            emotions = parsed_response[0]['faceAttributes']['emotion']
            emotion_color_name = face_emotions_to_color(emotions)
            if emotion_color_name is not None:
                color_changer.change(name=emotion_color_name, hex=mood_ring_colors[emotion_color_name])
            else:
                color_changer.turn_off()
        else:
            color_changer.turn_off()
        conn.close()
    time.sleep(UPDATE_INTERVAL)
    i += 1
