from app.models.task import Task
from app.models.project import Project
from app import response, app, db
from flask import request

def index():
  try:
    tasks = Task.query.all()
    data = allTask(tasks)
    return response.success(data, "success")

  except Exception as e:
    print(e)


def allTask(tasks):
  array = []
  for i in tasks:
    array.append(singleTask(i))
  
  return array

def singleTask(data):
  data = {
    'id' : data.id,
    'project_id' : data.project_id,
    'name' : data.name,
    'description' : data.description,
    'due_date' : data.due_date
  }
  return data

# def show(id):
#   try:
#     task = Task.query.filter_by(id=id).first()
#     project = Project.query.filter_by(id=id).first()
#     task_project = Task.query.filter(Task.project_id == id)

#     if not project:
#       return response.badRequest([], 'Unavailable data project')
  
#     dataTask = allTask(task_project)
#     data = detailProject(project, dataTask)
#     return response.success(data, "success")
#   except Exception as e:
#     print(e)

# def detailProject(project, dataTask):
#   data = {
#     'id' : project.id,
#     'name' : project.name,
#     'description' : project.description,
#     'due_date' : project.due_date,
#     'task' : dataTask
#   }
#   return data

# def singleTask(tasks):
#   data = {
#     'id': tasks.id,
#     'name': tasks.name,
#     'description': tasks.description,
#     'due_date': tasks.due_date
#   }
#   return data

# def allTask(data):
#   array = []
#   for i in data:
#     array.append(singleTask(i))
#   return array


def store():
  try:
    project_id = request.form.get('project_id')
    name = request.form.get('name')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    task = Task(project_id=project_id ,name=name, description=description, due_date=due_date)
    db.session.add(task)
    db.session.commit()
    return response.success('', 'Task successfully created')
  
  except Exception as e:
    print(e)

def update(id):
  try:
    project_id = request.form.get('project_id')
    name = request.form.get('name')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    input = [
      {
        'project_id' : project_id,
        'name' : name,
        'description' : description,
        'due_date' : due_date
      }
    ]

    task = Task.query.filter_by(id=id).first()
    task.name = project_id
    task.name = name
    task.description = description
    task.due_date = due_date

    db.session.commit()

    return response.success(input, 'Task has been updated')
  except Exception as e:
    print(e)

def delete(id):
  try:
    task = Task.query.filter_by(id=id).first()
    if not task:
      return response.badRequest([], 'Task unavailable!')
    
    db.session.delete(task)
    db.session.commit()
    return response.success('', 'Task has been deleted')

  except Exception as e:
    print(e)