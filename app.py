import pickle
import random
import webapp2

from weather import weather


class Home(webapp2.RequestHandler):
	"""A GET Request Handler"""

	def get(self):
		"""Receives a GET request"""

		self.response.write('Slack Weather Command')


class WeatherApp(webapp2.RequestHandler):
	"""A POST Request Handler for the weather command"""

	def post(self):
		"""Receives a POST request"""

		zip_code = self.request.get('text')
		user_id = self.request.get('user_id')

		if not zip_code:
			zip_code = self._get_saved_zip_code(user_id)

		self.get_weather(str(zip_code))
		self._save_user_zip_code(user_id, zip_code)

	def get_weather(self, zip_code):
		"""Gets weather for :zip_code: and writes to :handler:"""

		if zip_code:
			_weather = weather(str(zip_code))
			self.response.write(_weather)
		else:
			self.response.write('No zip code entered...')

	def _get_saved_zip_code(self, user_id):
		"""Attempts to return saved zip code for :user_id:"""

		with open('saved_user_zips.p', 'rb') as f:
			user_zips = pickle.load(f)
			return user_zips.get(user_id)

	def _save_user_zip_code(self, user_id, zip_code):
		"""Saves dict[user_id] = zip_code to 'saved_user_zips.p'"""

		with open('saved_user_zips.p', 'rb') as f:
			user_zips = pickle.load(f)
			user_zips[user_id] = zip_code 

		with open('saved_user_zips.p', 'wb') as f:
			pickle.dump(user_zips, f)




app = webapp2.WSGIApplication([
						(r'/', Home),
						(r'/weather', WeatherApp)
						],
						debug=True)