import requests
import time

"""r = requests.get("https://api.kanye.rest/")
print(r.text)"""

while True:
    r = requests.get("https://api.kanye.rest/")
    if r.status_code == 200:
        print(r.json())
    time.sleep(2)


