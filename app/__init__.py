# from flask import Flask
# from dotenv import load_dotenv
# load_dotenv()
# import os 
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt


# app  = Flask(__name__)

# base_dir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(base_dir, 'data.db')



# app.config['SECRET_KEY'] = os.environ['SECRET_KEY_APP']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path  # o banco de dados sera criado na mesma pasta em que estiver o arquivo __init__.py

# db = SQLAlchemy(app)
# bcrypt= Bcrypt(app)

# from app import routes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'data.db')

app.config['SECRET_KEY'] = os.environ['SECRET_KEY_APP']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path  # o banco de dados sera criado na mesma pasta em que estiver o arquivo __init__.py


db= SQLAlchemy(app)
bcrypt = Bcrypt(app)



from app import routes