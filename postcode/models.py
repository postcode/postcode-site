from sqlalchemy import Column, Integer, String
from postcode import app
from database import Base

class Signup(Base):
	__tablename__ = 'signup'
	id = Column(Integer, primary_key=True)
	email = Column(String(120), unique=True)
	name = Column(String(50))

	def __init__(self, email, name=None):
		self.email = email
		self.name = name