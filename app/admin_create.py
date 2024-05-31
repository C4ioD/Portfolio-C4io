from app import app, db, bcrypt
from app.models import Usuario
from dotenv import load_dotenv
load_dotenv()
import os 


def create_admin():
    with app.app_context():
        db.create_all()
        if not Usuario.query.filter_by(username='admin').first():
          senha_admin = bcrypt.generate_password_hash(str(os.environ['SENHA_ADMIN']))
          admin_user=(Usuario(
            username='admin',
            email='envioemailautomacoes@gmail.com',
            senha= senha_admin,
            is_admin=True
          ))
          db.session.add(admin_user)
          db.session.commit()
          print('Usuario admin criado.')
        else:
          print('Usuario admin já existe.')

if __name__ == '__main__':
    create_admin()