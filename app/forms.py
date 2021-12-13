from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, Form, validators
from wtforms.validators import DataRequired, ValidationError, Email, InputRequired, EqualTo
from app.models import User

#Formulário de login:
class LoginForm(FlaskForm):
    #Primeiro variável será uma string que será filtrada no routes.py
    login = StringField(validators=[validators.DataRequired()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    submit = SubmitField('Entre')
    submit2 = SubmitField('Registre-se')

#Formulário de registro:
class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário:', validators=[DataRequired()])
    cpf = StringField('CPF:', validators=[DataRequired(), validators.Length(min=11, max=14)])
    pis = StringField('PIS:', validators=[DataRequired(), validators.Length(min=11, max=11)])
    email = EmailField('E-mail:', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Enviar')
    pais = StringField('País:',validators=[DataRequired()])
    cep = StringField('CEP:', validators=[DataRequired(), validators.Length(min=8, max=9)])
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

#Formulário de edição, sem a necessidade de preencher os campos obrigatoriamente:
class EditForm(FlaskForm):
    #Transformado o usarname em um campo fixo para funcionar como uma baliza para os outros campos de edição.
    username = StringField('Nome de usuário:', render_kw={'readonly': True}, validators=[DataRequired()])
    cpf = StringField('CPF:')
    pis = StringField('PIS:')
    email = EmailField('E-mail:', validators=[validators.DataRequired(), validators.Email()])
    pais = StringField('País:')
    cep = StringField('CEP:')
    estado = StringField('UF;')
    cidade = StringField('Cidade:')
    rua = StringField('Rua:')
    numero = StringField('Número:')
    complemento = StringField('Complemento:')
    submit = SubmitField('Atualizar')
    delete = SubmitField('Deletar')
    password = PasswordField('Senha:', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha:', validators=[DataRequired(), EqualTo('password')])
    
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


        
        