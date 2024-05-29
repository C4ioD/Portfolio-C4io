from app import app
from flask import render_template, url_for, redirect
from app.forms import FormLogin


@app.route("/")
def index():
  return render_template('index.html')

@app.route("/login")
def login():
  form_login = FormLogin()
  return render_template('login.html', form_login=form_login)