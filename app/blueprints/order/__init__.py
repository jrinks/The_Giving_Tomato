from flask import Blueprint

bp = Blueprint('order', __name__, url_prefix='/order')

from . import models, routes