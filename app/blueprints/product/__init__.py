from flask import Blueprint

bp = Blueprint('product', __name__, url_prefix='/product')

from . import models, routes, forms