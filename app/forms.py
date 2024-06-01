from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email

class FormLogin(FlaskForm):
  nome= StringField('Nome', validators=[DataRequired()])
  senha= PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
  btn_login = SubmitField('Entrar')

class FormSobre(FlaskForm):
  nome = StringField('Nome', validators=[DataRequired()])
  data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()])
  naturalidade = StringField('Naturalidade', validators=[DataRequired()])
  cidade = StringField('Cidade', validators=[DataRequired()])
  estado = StringField('Estado', validators=[DataRequired()])
  endereco = StringField('Endereço', validators=[DataRequired()])
  email = StringField('E-mail', validators=[DataRequired()])
  profile = FileField('Imagem')
  btn_sobre = SubmitField('Salvar')

class FormEducacao(FlaskForm):
  nome_curso = StringField('Curso', validators=[DataRequired()])
  instituicao = StringField('Instituição', validators=[DataRequired()])
  data_nascimento = DateField('Data de Início', validators=[DataRequired()])
  data_fim = DateField('Data Fim')

class FormProjetos(FlaskForm):
  resumo = StringField('Resumo', validators=[DataRequired()])
  descricao = StringField('Descrição', validators=[DataRequired()])
  capa = FileField('Capa')

class FormExperiencias(FlaskForm):
   cargo = StringField('Cargo', validators=[DataRequired()])
   empresa = StringField('Empresa', validators=[DataRequired()])
   descricao = StringField('Descrição', validators=[DataRequired()])
   data_inicio = DateField('Data Início', validators=[DataRequired()])
   data_fim = DateField('Data Fim', validators=[DataRequired()])

class FormSkills(FlaskForm):
  nome = StringField('Nome', validators=[DataRequired()])
  resumo = StringField('Resumo', validators=[DataRequired()])
  icone = FileField('Icone')


 