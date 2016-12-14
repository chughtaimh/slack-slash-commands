import json
import requests
import mypy

APIKEY = '0f02e726e5ba577af096f8d3a2efc18b'
BASEURL = 'http://api.openweathermap.org/data/2.5/weather'

def weather(zip_code):
	"""
	Returns the a dict containing weather for :zip_code:.
	:params:
		zip_code : str -- zip code to search
	:return:
		weather : dict -- weather for :zip_code:
	"""

	r = requests.post(BASEURL, params=dict(APPID=APIKEY, zip=zip_code))
	content = json.loads(r.content)
	return content['main']