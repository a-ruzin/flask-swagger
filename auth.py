from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
import jwt

basic_auth = HTTPBasicAuth()
bearer_auth = HTTPTokenAuth(scheme='Bearer')

@basic_auth.verify_password
def verify_password(username, password):
    if username and username == "password":
        return username

@bearer_auth.verify_token
def verify_token(token):
    try:
        jwt.decode(token, "secret", algorithms=["HS256"])
        return 'hoho-user'
    except jwt.exceptions.DecodeError:
        pass
    except jwt.ExpiredSignatureError:
        pass