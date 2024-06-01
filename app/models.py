from app import db
from datetime import datetime 


# class Usuario(db.Model):
#   id = db.Column(db.Integer,primary_key = True)
#   username = db.Column(db.String, nullable = False, unique=True)
#   email = db.Column(db.String, nullable = False, unique=True)
#   senha = db.Column(db.String, nullable=False)
#   foto_perfil = db.Column(db.String, default='default.jpg')
#   posts = db.relationship('Post', backref='autor', lazy= True)
#   cursos = db.Column(db.String, nullable = False, default='Não informado')

#   def contar_posts(self):
#     return len(self.posts)

# class Post(db.Model):
#   id = db.Column(db.Integer, primary_key = True)
#   user_id = db.Column(db.Integer , db.ForeignKey('usuario.id'), nullable= False)
#   titulo = db.Column(db.String, nullable = False)
#   descricao = db.Column(db.String, nullable = False)
#   data_criacao = db.Column(db.DateTime, nullable= False , default= datetime.utcnow)



class Usuario(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String, nullable=False, unique=True)
  email = db.Column(db.String, nullable=False, unique=True)
  senha = db.Column(db.String, nullable=False)
  is_admin = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f"User('{self.username}', {'Admin' if self.is_admin else 'User'})"
 

class Sobre(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=True, default='Caio Dias Evangelista')
  data_nascimento = db.Column(db.Date, nullable=True, default=datetime.strptime('29-09-1998', '%d-%m-%Y'))
  naturalidade = db.Column(db.String, nullable=True, default='Brasileiro')
  cidade = db.Column(db.String, nullable=True, default='Timóteo')
  estado = db.Column(db.String, nullable=True, default='Minas Gerais')
  email= db.Column(db.String, nullable=True, default='caiodias29091@gmail.com')
  imagem= db.Column(db.String, default='default.jpg')


class Educacao(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome_curso= db.Column(db.String, nullable=False)
  data_inicio = db.Column(db.Date, nullable=False)
  data_fim = db.Column(db.Date, nullable=True)
  instituicao = db.Column(db.String, nullable=False)

class Projetos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  resumo = db.Column(db.String, nullable=False)
  descricao = db.Column(db.String, nullable=False)
  capa = db.Column(db.String, default='default_projetos.jpg')

class Experiencias(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  cargo = db.Column(db.String, nullable=False)
  empresa = db.Column(db.String, nullable=False)
  data_inicio = db.Column(db.Date, nullable=False)
  data_fim = db.Column(db.Date, nullable=True)
  descricao= db.Column(db.String, nullable=False)

class skills(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  resumo = db.Column(db.String, nullable=False)
  icone = db.Column(db.String, default='default_ico.svg')
  

