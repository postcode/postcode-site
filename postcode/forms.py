from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required, Email
from flask.ext.wtf.recaptcha import RecaptchaField


class signupForm(Form):
    name = TextField('name')
    email = TextField('email', validators = [Required(), Email()])
    recaptcha = RecaptchaField()
