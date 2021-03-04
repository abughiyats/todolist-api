from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30), nullable=False)
  email = db.Column(db.String(30), nullable=False, index=True, unique=True)
  password = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime(30), default=datetime.utcnow)
  updated_at = db.Column(db.DateTime(30), default=datetime.utcnow)

  def __repr__(self):
    return '<User {}>'.format(self.name)

  def hashPassword(self, password):
    self.password = generate_password_hash(password)

  def checkPassword(self, password):
    return check_password_hash(self.password, password)
