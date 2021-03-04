from app import app
from app.controllers import UsersController

@app.route('/')
def index():
  return "hello world!"

@app.route('/register', methods=['POST'])
def auth_register():
  return UsersController.registration()

@app.route('/login', methods=['POST'])
def auth_login():
  return UsersController.login()