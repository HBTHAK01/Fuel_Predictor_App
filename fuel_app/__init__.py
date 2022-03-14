# import statements
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create db object
db = SQLAlchemy()

# Using pymysql connector to use for SQLALCHEMY
conn = 'mysql+pymysql://root:****@localhost/Fuel_Database'

def create_app():
    # Flask constructor
    app = Flask(__name__)

    # Configuring session cookies
    app.config['SECRET_KEY'] = 'ABC123'

    # Importing and registering blueprint "views" to our flask app
    from .views import views
    app.register_blueprint(views)

    # Importing models
    from .models import Usercredentials, Clientinformation, Fuelquote
    # Connecting SQLALCHEMY to pymysql
    app.config['SQLALCHEMY_DATABASE_URI'] = conn

    # Binding db to app
    db.init_app(app)
    
    login_manager = LoginManager()

    # Default url
    login_manager.login_view = 'views.index'
    login_manager.init_app(app)

    # Reload the user object from the user ID stored in the session
    @login_manager.user_loader   
    def load_user(id):
        return Usercredentials.query.get(int(id))

    return app