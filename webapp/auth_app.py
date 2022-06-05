from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask




app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/flask_jwt_auth"
POSTGRES = {
    'user': 'postgres',
    'pw': 'asdr',
    'db': 'flask_jwt_auth',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


db = SQLAlchemy(app)
migrate = Migrate(app, db)


if __name__ == '__mian__':
    app.run()