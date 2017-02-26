from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object('superrental.config')
mongo = PyMongo(app)


from superrental.views import *
from superrental.api import *
