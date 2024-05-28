from flask import Flask
from dotenv import load_dotenv
load_dotenv()

import os 


app  = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'data.db')

app.config['SECRET_KEY'] = os.environ['SECRET_KEY_APP']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path  # o banco de dados sera criado na mesma pasta em que estiver o arquivo __init__.py


from app import routes