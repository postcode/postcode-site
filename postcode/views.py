"""Contains all functions that render templates/html for the app.
"""

from flask import render_template, url_for, redirect
from postcode import app
from jinja_filters import *
import os
import sys, traceback
from forms import signupForm

ga_tracking_code = os.getenv('GA_TRACKING_CODE', 'Not defined!')
remarketing_id = os.getenv('REMARKETING_ID', 'Not defined!')

# Submitting a new request
def index():
	return render_template('index.html', ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id)

def any_page(page):
	try:
		form = signupForm()
		return render_template('%s.html' %(page), ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id, form=form)
	except:
                app.logger.error(traceback.format_exception(*sys.exc_info()))
		return index()

def product_page(product):
	return redirect(url_for('static', filename='content/%s.pdf' %(product)))
