from app import app
from app.controllers import UsersController, ProjectsController, TasksController
from flask import request

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
