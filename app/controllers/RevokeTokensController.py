from app.controllers import UsersController
from app.models.revokedToken import RevokedToken
from app import response, app, db
from flask_jwt_extended import *
import pdb

@jwt_required()
def userLogoutAccess():
  jti = get_jwt()['jti']
  try:
    revoked_token = RevokedToken(jti=jti)
    db.session.add(revoked_token)
    db.session.commit()
    return response.success('Logout', 'User has been Logged Out')

  except Exception as e:
    print(e)

@jwt_required(refresh=True)
def userLogoutRefresh():
  jti = get_jwt()['jti']
  try:
    revoked_token = RevokedToken(jti=jti)
    db.session.add(revoked_token)
    pdb.set_trace()
    return response.success('Logout', 'Refresh token has been revoked')

  except Exception as e:
    print(e)

@jwt_required(refresh=True)
def tokenRefresh():
  current_user = get_jwt_identity()
  access_token = create_access_token(identity=current_user)
  return {'access_token': access_token}

