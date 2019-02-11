Mood ring that illuminates a blinkstick using facial emotion recognition.

To install:

Copy config.properties.template to config.properties and replace AZURE_SUBSCRIPTION_KEY with your key. Then run:

```bash
virtualenv --no-site-packages venv
source venv/bin/activate
sudo pip3 install blinkstick termcolor
source config.properties
export AZURE_SUBSCRIPTION_KEY
export REGION
sudo python3 mood_ring.py
```
