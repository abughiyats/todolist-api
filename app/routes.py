from app import app, db
from flask import request
from app.models.revokedToken import RevokedToken
from app.controllers import UsersController, ProjectsController, TasksController, RevokeTokensController
from flask_jwt_extended import *

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db.session.query(RevokedToken.id).filter_by(jti=jti).scalar()
    return token is not None

@app.route('/')
def index():
  return "hello world!"

@app.route('/register', methods=['POST'])
def auth_register():
  return UsersController.registration()

@app.route('/login', methods=['POST'])
def auth_login():
  return UsersController.login()

@app.route('/users', methods=['GET'])
def users():
  return UsersController.index()

@app.route('/projects', methods=['GET', 'POST'])
def projects():
  if request.method == 'GET':
    return ProjectsController.index()
  else:
    return ProjectsController.store()

@app.route('/project/<id>', methods=['GET', 'PUT', 'DELETE'])
def project(id):
  if request.method == 'GET':
    return ProjectsController.show(id)
  elif request.method == 'PUT':
    return ProjectsController.update(id)
  elif request.method == 'DELETE':
    return ProjectsController.delete(id)

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
  if request.method == 'GET':
    return TasksController.index()
  else:
    return TasksController.store()

@app.route('/task/<id>', methods=['PUT', 'DELETE'])
def task(id):
  if request.method == 'PUT':
    return TasksController.update(id)
  else:
    return TasksController.delete(id)

@app.route('/logout/access', methods=['DELETE'])
def logout_access():
    return RevokeTokensController.userLogoutAccess()

@app.route('/logout/refresh', methods=['DELETE'])
def logout_refresh():
    return RevokeTokensController.userLogoutRefresh()

@app.route('/token/refresh', methods=['DELETE'])
def token_refresh():
    return RevokeTokensController.tokenRefresh()
