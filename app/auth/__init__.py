#create a Blueprint instance auth and we import the auth views module.

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views