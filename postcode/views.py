"""Contains all functions that render templates/html for the app.
"""

from flask import render_template, url_for, redirect, flash, request
from postcode import app
from models import Signup
from jinja_filters import *
import os
import sys, traceback
from forms import signupForm
import logging
from logging.handlers import RotatingFileHandler
from postcode.database import db_session
import sendgrid

ga_tracking_code = os.getenv('GA_TRACKING_CODE', 'Not defined!')
remarketing_id = os.getenv('REMARKETING_ID', 'Not defined!')


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
# Submitting a new request
def index():
	return render_template('index.html', ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id)

def any_page(page):
	try:
		return render_template('%s.html' %(page), ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id)
	except:
                app.logger.error(traceback.format_exception(*sys.exc_info()))
		return index()

def product_page(product):
	return redirect(url_for('static', filename='content/%s.pdf' %(product)))

@app.route('/recordtrac', methods = ['GET', 'POST'])
def recordtrac():
	form = signupForm()
	try:
		if request.method == 'POST' and form.validate():
			user = Signup(form.email.data, form.name.data)
			db_session.add(user)
			db_session.commit()
			signup_email(user)
			return redirect(url_for('/'))
		return render_template('recordtrac.html', ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id, form=form)
	except:
                app.logger.error(traceback.format_exception(*sys.exc_info()))
		return index()

def signup_email(user):
	sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])
	message_postcode = sendgrid.Mail()
	message_postcode.add_to('Postcode <info@postcode.io>')
	message_postcode.set_subject('RecordTrac Sign Up')
	message_postcode.set_html('Hi, just wanted to let you know that someone just signed up for RecordTrac with the email:<br/> %s' %user.email)
	message_postcode.set_from('admin@postcode.io')
	status, msg_pc = sg.send(message_postcode)
	app.logger.debug(msg_pc)

	message_user = sendgrid.Mail()
	message_user.add_to('%s' %user.email)
	message_user.set_subject('RecordTrac Sign Up')
	message_user.set_html("Thanks for signing up for RecordTrac! We'll be in touch soon. Look for updates at <a href='http://www.postcode.io/recordtrac'>http://www.postcode.io/recordtrac</a>")
	message_user.set_from('admin@postcode.io')
	status, msg_user = sg.send(message_user)
	app.logger.debug(msg_user)
	return msg_user, msg_pc
