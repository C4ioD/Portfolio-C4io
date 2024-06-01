from app import app, db , bcrypt
from app.models import Usuario, Sobre
from flask import render_template, url_for, redirect, flash
from app.forms import FormLogin, FormSobre
import datetime


@app.route("/")
def index():
  inf_sobre = Sobre.query.filter_by(id='1').first()
  idade = (datetime.date.today() - inf_sobre.data_nascimento)/365
  return render_template('index.html', inf_sobre=inf_sobre, idade=idade.days)

@app.route('/erro')
def erro():
  return  render_template('erro.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
  form_login = FormLogin()
  if form_login.validate_on_submit():
    usuario= Usuario.query.filter_by(username=form_login.nome.data).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
      return redirect(url_for('index'))
    else:
      return redirect(url_for('erro'))

  return render_template('login.html', form_login=form_login)


@app.route('/edit')
def edit():
  return  render_template('edit.html')

@app.route('/edit/sobre', methods=['GET','POST'])
def sobre():
  form_sobre = FormSobre()
  if form_sobre.validate_on_submit():

    if not Sobre.query.filter_by(id='1').first():
      sobre = Sobre(
        nome=form_sobre.nome.data,
        data_nascimento=datetime.strptime(form_sobre.data_nascimento.data,'%d-%m-%Y'),
        naturalidade=form_sobre.naturalidade.data,
        cidade=form_sobre.cidade.data,
        estado=form_sobre.estado.data,
        email=form_sobre.email.data,
        imagem=form_sobre.profile.data,
        endereco= form_sobre.endereco.data
        )
      db.session.add(sobre)
      db.session.commit()
    
    else:
      sobre = Sobre.query.filter_by(id='1').first()
      sobre.nome = form_sobre.nome.data
      sobre.data_nascimento= form_sobre.data_nascimento.data
      sobre.naturalidade= form_sobre.naturalidade.data
      sobre.cidade= form_sobre.cidade.data
      sobre.estado= form_sobre.estado.data
      sobre.email= form_sobre.email.data
      sobre.imagem= form_sobre.profile.data
      sobre.endereco= form_sobre.endereco.data
      db.session.commit()

  return render_template('sobre.html', form_sobre=form_sobre, inf_sobre=sobre)