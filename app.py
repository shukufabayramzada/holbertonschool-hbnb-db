from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to 2nd part of HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)