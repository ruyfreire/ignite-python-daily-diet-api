from dotenv import load_dotenv
import os
from flask import Flask
from database import db

from routes import diet_routes

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app)

app.register_blueprint(diet_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
