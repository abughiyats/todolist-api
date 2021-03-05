from app.models.user import User
from app import response, app, db
from flask import request
from flask_jwt_extended import *
import datetime

def index():
  try:
    users = User.query.all()
    data = allUser(users)
    return response.success(data, "success")

  except Exception as e:
    print(e)

def allUser(users):
  array = []

  for i in users:
    array.append(singleUser(i))
  return array

def singleUser(users, withProject=True):
  data = {
    'id' : users.id,
    'name' : users.name,
    'email' : users.email
  }
  if withProject:
    projects = []
    for i in users.projects:
      projects.append({
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'due_date': i.due_date,
      })
    data['projects'] = projects
  return data

def registration():
  try:
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    users = User(name=name, email=email)
    users.hashPassword(password)
    db.session.add(users)
    db.session.commit()

    return response.success('User', 'User succesfully registered!')
  except Exception as e:
    print(e)

def login():
  try:
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
      return response.badRequest([], 'email unavailble!')

    if not user.checkPassword(password):
      return response.badRequest([], 'wrong password')

    data = model_user(user)
    expires = datetime.timedelta(hours=1)
    expires_refresh = datetime.timedelta(hours=3)
    access_token = create_access_token(data, fresh=True, expires_delta=expires)
    refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

    return response.success({
      "user" : data,
      "access_token" : access_token,
      "refresh_token" : refresh_token
    }, "Success!")

  except Exception as e:
    print(e)