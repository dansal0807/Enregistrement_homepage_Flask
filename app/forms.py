from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, Form, validators
from wtforms.validators import DataRequired, ValidationError, Email, InputRequired, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    login = StringField(' ', [validators.DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    submit = SubmitField('Entre:')
    submit2 = SubmitField('Registre-se:')

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    cpf = StringField('CPF:', validators=[DataRequired()])
    pis = StringField('PIS:', validators=[DataRequired()])
    email = EmailField('E-mail:', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Enviar')
    pais = StringField('País:',validators=[DataRequired()])
    cep = StringField('CEP:', validators=[DataRequired()])
    estado = StringField('UF;', validators=[DataRequired()])
    cidade = StringField('Cidade:', validators=[DataRequired()])
    rua = StringField('Rua:', validators=[DataRequired()])
    numero = StringField('Número:', validators=[DataRequired()])
    complemento = StringField('Complemento:')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, utilize um nome de usuário diferente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor, utilize um endereço de e-mail diferente.')

class EditForm(FlaskForm):
    username = StringField('Nome de usuário:', render_kw={'readonly': True}, validators=[DataRequired()])
    cpf = StringField('CPF:')
    pis = StringField('PIS:')
    email = EmailField('E-mail:', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Atualizar')
    pais = StringField('País:')
    cep = StringField('CEP:')
    estado = StringField('UF;')
    cidade = StringField('Cidade:')
    rua = StringField('Rua:')
    numero = StringField('Número:')
    complemento = StringField('Complemento:')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Por favor, utilize um nome de usuário diferente.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Por favor, utilize um nome de usuário diferente.')