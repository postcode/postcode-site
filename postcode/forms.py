from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Email

class signupForm(Form):
    name = TextField('name')
    email = TextField('email', validators = [Required(), Email()])
