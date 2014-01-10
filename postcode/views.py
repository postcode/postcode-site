"""Contains all functions that render templates/html for the app.
"""

from flask import render_template
from postcode import app

# Submitting a new request
def index():
	return render_template('index.html')


def any_page(page):
	try:
		return render_template('%s.html' %(page))
	except:
		return index()