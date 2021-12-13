from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login = LoginManager(app)
login.login_view = 'login'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=port)
    
from app import routes, models