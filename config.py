import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  USERNAME = str(os.environ.get("DB_USERNAME"))
  PASSWORD = str(os.environ.get("DB_PASSWORD"))
  HOST = str(os.environ.get("DB_HOST"))
  DB = str(os.environ.get("DB_DATABASE"))

  JWT_SECRET_KEY = str(os.environ.get("SECRET_KEY"))
  JWT_BLACKLIST_ENABLED = True
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
  

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True