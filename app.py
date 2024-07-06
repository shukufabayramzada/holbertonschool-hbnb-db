from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from config.config import get_config
from api.user_controller import user_bp

load_dotenv()

app = Flask(__name__)
app.config.from_object(get_config())
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

app.register_blueprint(user_bp, url_prefix='/api')

@app.route('/')
def hello():
    return "Welcome to 2nd part of HBNB"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)