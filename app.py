import webapp2
import random


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

		get_weather(zip_code, handler=self)
		

	def get_weather(self, zip_code, handler):
		"""Gets weather for :zip_code: and writes to :handler:"""

		handler.response.write('Getting Weather!')


app = webapp2.WSGIApplication([
						(r'/', Home),
						(r'/weather', WeatherApp)
						],
						debug=True)