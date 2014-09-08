"""A flask app to power postcode.io

.. moduleauthor:: Richa Agarwal <richa@postcode.io>

"""

from os import environ
from flask import Flask

# Initialize Flask app 
app = Flask(__name__)
app.debug = True
app.config.from_object('config')

