"""Contains all functions that render templates/html for the app.
"""

from flask import render_template, url_for, redirect
from postcode import app
from jinja_filters import *

# Submitting a new request
def index():
	return render_template('index.html')


def any_page(page):
	try:
		return render_template('%s.html' %(page))
	except:
		return index()

def product_page(product):
	return redirect(url_for('static', filename='content/%s.pdf' %(product)))