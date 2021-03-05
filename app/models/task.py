from app.models.project import Project
from app import db
from datetime import datetime

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  project_id = db.Column(db.Integer, db.ForeignKey(Project.id, ondelete='CASCADE'))
  name = db.Column(db.String(30), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  due_date = db.Column(db.DateTime, default=datetime.utcnow)
  

  def __repr__(self):
    return '<Task {}>'.format(self.name)

  