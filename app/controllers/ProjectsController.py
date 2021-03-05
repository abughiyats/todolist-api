from app.controllers import UsersController
from app.models.task import Task
from app.models.project import Project
from app import response, app, db
from flask import request

def index():
  try:
    projects = Project.query.all()
    data = allProject(projects)
    return response.success(data, "success")

  except Exception as e:
    print(e)

def allProject(projects):
  array = []

  for i in projects:
    array.append(singleProject(i))
  
  return array

def singleProject(data):
  data = {
    'id' : data.id,
    'name' : data.name,
    'description' : data.description,
    'due_date' : data.due_date,
    'user_id' : data.user_id,
    'user' : UsersController.singleUser(data.users, withProject=False)
  }

  return data

def show(id):
  try:
    project = Project.query.filter_by(id=id).first()
    task_project = Task.query.filter(Task.project_id == id)

    if not project:
      return response.badRequest([], 'Unavailable data project')
  
    dataTask = allTask(task_project)
    data = detailProject(project, dataTask)
    return response.success(data, "success")
  except Exception as e:
    print(e)

def detailProject(project, dataTask):
  data = {
    'id' : project.id,
    'name' : project.name,
    'description' : project.description,
    'due_date' : project.due_date,
    'task' : dataTask
  }
  return data

def singleTask(tasks):
  data = {
    'id': tasks.id,
    'name': tasks.name,
    'description': tasks.description,
    'due_date': tasks.due_date
  }
  return data

def allTask(data):
  array = []
  for i in data:
    array.append(singleTask(i))
  return array

def store():
  try:
    name = request.form.get('name')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    project = Project(name=name, description=description, due_date=due_date)
    db.session.add(project)
    db.session.commit()
    return response.success('', 'Project successfully created')
  
  except Exception as e:
    print(e)

def update(id):
  try:
    name = request.form.get('name')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    input = [
      {
        'name' : name,
        'description' : description,
        'due_date' : due_date
      }
    ]

    project = Project.query.filter_by(id=id).first()
    project.name = name
    project.description = description
    project.due_date = due_date

    db.session.commit()

    return response.success(input, 'Project has been updated')
  except Exception as e:
    print(e)

def delete(id):
  try:
    project = Project.query.filter_by(id=id).first()
    if not project:
      return response.badRequest([], 'Project unavailable!')
    
    db.session.delete(project)
    db.session.commit()
    return response.success('', 'Project has been deleted')

  except Exception as e:
    print(e)