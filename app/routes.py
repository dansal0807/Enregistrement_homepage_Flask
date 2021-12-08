from flask import render_template, redirect, flash, url_for, request
from wtforms.validators import Email
from app import app, db
from app.forms import LoginForm, FlaskForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from app.forms import RegistrationForm, LoginForm
from validate_docbr import CPF

#renderização das rotas do formulário:
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = LoginForm()
    return render_template('login.html', title='Cadastre-se', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_entry = form.username.data
    if form.validate_on_submit():
        user = User.query.filter((User.email == login_entry) | (User.cpf == login_entry) | 
        (User.pis == login_entry)).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos.')
            return redirect(url_for('login'))
        else:
            return render_template('user.html', username=user.username)
    return render_template('login.html', title='Cadastre-se', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, 
                    email=form.email.data,
                    cpf=form.cpf.data,
                    pis=form.pis.data)
                    
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Agora você está registrado!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)