from app import app

def main():
	"""Runs webservice"""

	from paste import httpserver
	httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
	main()
