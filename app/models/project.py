from app.models.user import User
from app import db
from datetime import datetime

class Project(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30), nullable=False)
  description = db.Column(db.String(255), nullable=False)
  due_date = db.Column(db.DateTime, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey(User.id))
  users = db.relationship("User", backref="user_id")
  

  def __repr__(self):
    return '<Project {}>'.format(self.name)

  