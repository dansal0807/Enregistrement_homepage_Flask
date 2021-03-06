import os
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#Modelo principal do usuário:
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    cpf = db.Column(db.String(14))
    pis = db.Column(db.String(128))
    pais = db.Column(db.String(128))
    cep = db.Column(db.String(100))
    estado = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    rua = db.Column(db.String(80))
    numero = db.Column(db.String(100))
    complemento = db.Column(db.String(40))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#Função de retorno do usuário enquanto objeto:
@login.user_loader
def load_user(id):
    return User.query.get(int(id))