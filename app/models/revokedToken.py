from app import db
from datetime import datetime

class RevokedToken(db.Model):
  __tablename__ = 'revoked_tokens'
  id  = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(255))
