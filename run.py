from app import app
from app.admin_create import create_admin



if __name__ == "__main__":
  create_admin()
  app.run(debug=True)