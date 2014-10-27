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

@app.route('/nextrequest', methods = ['GET', 'POST'])
def nextrequest():
	form = signupForm()
	try:
		if request.method == 'POST' and form.validate():
			user = Signup(form.email.data, form.name.data)
			db_session.add(user)
			db_session.commit()
			signup_email(user)
			return render_template('recordtrac-confirm.html', ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id)
		return render_template('nextrequest.html', ga_tracking_code = ga_tracking_code, remarketing_id=remarketing_id, form=form)
	except:
                app.logger.error(traceback.format_exception(*sys.exc_info()))
		return index()

def signup_email(user):
	sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])
	message_postcode = sendgrid.Mail()
	message_postcode.add_to('Postcode <info@postcode.io>')
	message_postcode.set_subject('NextRequest Sign Up')
	message_postcode.set_html('Hi, just wanted to let you know that someone just signed up for NextRequest with the email:<br/> %s' %user.email)
	message_postcode.set_from('nextrequest@postcode.io')
	status, msg_pc = sg.send(message_postcode)
	app.logger.debug(msg_pc)

	user_html = "<p style='margin-bottom: 20px;'><a href='http://www.postcode.io/nextrequest'><img src='http://pobox.herokuapp.com/images/NR_email_header.png'/></a></p><h4>Thanks for getting in touch with us about <a href='http://www.postcode.io/nextrequest'>NextRequest</a>!</h4><p>We're leading the way on public records requests and are excited you're interested in joining us. We'll follow up with you shortly to set up a customized pilot for your organization.</p>&nbsp;<p>If you have any questions don't hesitate to call or send us an email.<br><strong>tel:</strong> (844) 767-8263<br><strong>email:</strong> <a href='mailto:nextrequest@postcode.io'>nextrequest@postcode.io</a></p>"
	message_user = sendgrid.Mail()
	message_user.add_to('%s' %user.email)
	message_user.set_subject('NextRequest Sign Up')
	message_user.set_html(user_html)
	message_user.set_from('nextrequest@postcode.io')
	status, msg_user = sg.send(message_user)
	app.logger.debug(msg_user)
	return msg_user, msg_pc
