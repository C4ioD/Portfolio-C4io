from app import app, db , bcrypt
from app.models import Usuario
from flask import render_template, url_for, redirect, flash
from app.forms import FormLogin


@app.route("/")
def index():
  return render_template('index.html')

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


