from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class FormLogin(FlaskForm):
  nome= StringField('Nome', validators=[DataRequired()])
  senha= PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
  btn_login = SubmitField('Entrar')