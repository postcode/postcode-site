"""Contains all functions that render templates/html for the app.
"""

from flask import render_template, url_for, redirect
from postcode import app
from jinja_filters import *
import os

ga_tracking_code = os.getenv('GA_TRACKING_CODE', 'Not defined!')

# Submitting a new request
def index():
	return render_template('index.html', ga_tracking_code = ga_tracking_code)

def any_page(page):
	try:
		return render_template('%s.html' %(page), ga_tracking_code = ga_tracking_code)
	except:
		return index()

def product_page(product):
	return redirect(url_for('static', filename='content/%s.pdf' %(product)))
