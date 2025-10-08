import requests
import json

API_KEY = '87de8f40889f46bd84c115027251205'
BASE_URL = 'http://api.weatherapi.com/v1'

LATITUDE = 16.516192
LONGITUDE = 81.732444

CURRENT_WEATHER = f"{BASE_URL}/current.json?key={API_KEY}&q={LATITUDE},{LONGITUDE}"

info = requests.get(CURRENT_WEATHER)
print(json.dumps(info.json(), indent=4))
