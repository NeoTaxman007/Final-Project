from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

#Creating a flask object & rendering the templates folder.
app = Flask(__name__, template_folder="templates")

#Sets up the database via SQLAlchemy sqlite or creating enviroment variable to secure the data.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
#app.config['SECRET_KEY'] = 'Secrets'


db = SQLAlchemy(app)

# imports the routes.py from via the application folder. 
from application import routes
