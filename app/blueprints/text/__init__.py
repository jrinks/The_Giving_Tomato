from flask import Blueprint

bp = Blueprint('text', __name__, url_prefix='/text')

from . import routes, forms