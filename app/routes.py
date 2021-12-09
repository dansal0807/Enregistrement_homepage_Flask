from flask import render_template, redirect, flash, url_for, request
from flask.templating import render_template_string
from werkzeug import datastructures
from wtforms.validators import Email
from app import app, db
from app.forms import LoginForm, FlaskForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from app.forms import RegistrationForm, LoginForm, EditForm
from validate_docbr import CPF

#renderização das rotas do formulário:
@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    login_entry = form.login.data
    if form.validate_on_submit():
        user = User.query.filter((User.email == login_entry) | (User.cpf == login_entry) | 
        (User.pis == login_entry)).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos.')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        return render_template('user.html')
    return render_template('login.html', title='Cadastre-se', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, 
                    email=form.email.data,
                    cpf=form.cpf.data,
                    pis=form.pis.data,
                    pais = form.pais.data,
                    cep = form.cep.data,
                    estado = form.estado.data,
                    cidade = form.cidade.data,
                    rua = form.rua.data,
                    numero = form.numero.data,
                    complemento = form.complemento.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Agora você está registrado!')
        return redirect(url_for('login'))
    else:
        logged()
    return render_template('register.html', title='Register', form=form)

@login_required
def logged():
    return flash('O cadastro não foi bem sucedido.')

@app.route('/user', methods=['GET'])
@login_required
def user_template():
    return render_template('user.html')

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    user = User.query.filter_by(username=current_user.username).first()
    if request.method == "GET":
        form.username.data = user.username
        form.email.data = user.email
        form.cpf.data = user.cpf
        form.pis.data = user.pis
        form.pais.data = user.pais
        form.cep.data = user.cep
        form.estado.data = user.estado
        form.cidade.data = user.cidade
        form.rua.data = user.rua
        form.numero.data = user.numero
        form.complemento.data = user.complemento
    if request.method == "POST":
        edited_user = User.query.filter_by(username=current_user.username).update(dict(email=form.email.data,
                                                                                        cpf=form.cpf.data,
                                                                                        pis=form.pis.data,
                                                                                        pais = form.pais.data,
                                                                                        cep = form.cep.data,
                                                                                        estado = form.estado.data,
                                                                                        cidade = form.cidade.data,
                                                                                        rua = form.rua.data,
                                                                                        numero = form.numero.data,
                                                                                        complemento = form.complemento.data))
        db.session.commit()
        return render_template('user.html')
    return render_template('edit.html', user=user, form=form)

#Func. Delete: exclusão lógica ou exclusão do db.





