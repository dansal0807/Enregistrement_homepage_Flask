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

#Condição para as rotas entre o usuário estar logado ou ser um visitante:
@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    else:
        return render_template('user.html')

#Rota de Login:        
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    #Esta variável abaixo é fornecida no login.html:
    login_entry = form.login.data
    if form.validate_on_submit():
        #Aqui será aceito somente email, cpf ou pis, visto que o login entry é igualado ao
        #user.email, user.cpf e user.pis:
        user = User.query.filter((User.email == login_entry) | (User.cpf == login_entry) | 
        (User.pis == login_entry)).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos.')
            return redirect(url_for('login'))
        #Login_user é necessário para o flask_login compreender "quem" é o atual usuário
        #importante para usarmos os current_usar.
        login_user(user)
        next_page = request.args.get('next')
        return render_template('user.html')
    return render_template('login.html', title='Cadastre-se', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #Aqui instanciamos o usuário de acordo com o modelo providenciado em models.
        #Atribuímos os campos do modelo de acordo com as informações fornecidas no formulário
        #pelo usuário.
        cpf = CPF()
        if cpf.validate(form.cpf.data):
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
        else:
            flash("CPF errado. Tente novamente")
            return redirect(url_for('register'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #Após comitarmos, a confirmação é vinda:
        flash('Agora você está registrado!')
        return redirect(url_for('login'))
    else:
        logged()
    return render_template('register.html', title='Register', form=form)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    #O nome do usuário é a referência para a query feita no db.
    user = User.query.filter_by(username=current_user.username).first()
    #Após a query ser feita, podemos atribuir os valores adequados:
    if request.method == "GET":
    #Aqui será informado os valores de "pré-preenchimento" do formulário.
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
        #Nesta parte, encontra-se as atribuições dos valores informados pelo usuário para serem
        #atribuídos aos valores do modelo.
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

        if form.delete.data:
            db.session.delete(user)
            db.session.commit()
            logout()
            return redirect(url_for('login'))
    return render_template('edit.html', title="Edição", user=user, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
def logged():
    return flash('O cadastro não foi bem sucedido.')

#dificilmente o usuário irá buscar seu endereço por /user, no entanto, caso o faça
#o @login_required garante que ele esteja logado e, portanto, garante que todos os
#dados estejam adequados para a amostragem.
@app.route('/user', methods=['GET'])
@login_required
def user_template():
    return render_template('user.html')





    








