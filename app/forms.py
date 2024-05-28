from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class FormLogin(FlaskForm):
  nome= StringField('nome', validators=[DataRequired()])
  senha= PasswordField('senha', validators=[DataRequired(), Length(min=6, max=20)])
  btn_login = SubmitField('Entrar')