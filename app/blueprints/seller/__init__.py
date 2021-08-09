from flask import Blueprint

bp = Blueprint('seller', __name__, url_prefix='/seller')

from . import models, routes, forms