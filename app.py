import webapp2

from weather import weather, WeatherHandler


class Home(webapp2.RequestHandler):

	"""A GET Request Handler"""

	def get(self):
		"""Receives a GET request"""

		self.response.write('Moe Slack Commands')


app = webapp2.WSGIApplication([(r'/', Home), (r'/weather', WeatherHandler)],
	debug=True)
