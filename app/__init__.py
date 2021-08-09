from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
#from flask_mail import Mail
#from flask_cors import CORS
from config import Config


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
#mail = Mail()
#cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    #mail.init_app(app)
    #cors.init_app(app)

    login.login_view = 'user.login'
    #login.login_message_category = 'danger'

    with app.app_context():
        from app.blueprints.cart import bp as cart
        app.register_blueprint(cart)

        from app.blueprints.user import bp as user
        app.register_blueprint(user)

        from app.blueprints.product import bp as product
        app.register_blueprint(product)

        from app.blueprints.seller import bp as seller
        app.register_blueprint(seller)

        from app.blueprints.main import bp as main
        app.register_blueprint(main)

        from app.blueprints.order import bp as order
        app.register_blueprint(order)

        from app.blueprints.text import bp as text
        app.register_blueprint(text)
        

    return app