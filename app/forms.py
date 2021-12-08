from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, Form, validators
from wtforms.validators import DataRequired, ValidationError, Email, InputRequired
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('E-mail, CPF, PIS', [validators.DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entre')
    submit2 = SubmitField('Registre-se')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    cpf = StringField('CPF', [validators.DataRequired()])
    pis = StringField('PIS', [validators.DataRequired()])
    email = EmailField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

