"""A flask app to power postcode.io

.. moduleauthor:: Richa Agarwal <richa@postcode.io>

"""

from os import environ
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from database import init_db, db_session

# Initialize Flask app 
app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
app.config['SECRET_KEY'] = environ['SECRET_KEY']


init_db()
