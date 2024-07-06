from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config.config import get_config

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    db.init_app(app)

    @app.route('/')
    def hello():
        return "Welcome to 2nd part of HBNB"

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)

