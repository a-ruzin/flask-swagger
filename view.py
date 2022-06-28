from flasgger import Schema, SwaggerView
from marshmallow import fields
from auth import basic_auth, bearer_auth
import jwt


class IndexView(SwaggerView):
    parameters = []
    security = {"basicAuth": []}
    decorators = [basic_auth.login_required]
    responses = {
        200: {
            "description": "Login into account. Get access and refresh JWT-tokens",
        },
        401: {
            "description": "Could not verify login or password"
        }
    }

    def get(self):
        return "index"


class JWTokens(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


class LoginView(SwaggerView):
    parameters = []
    responses = {
        200: {
            "description": "Login into account. Get access and refresh JWT-tokens",
            "schema": JWTokens
        },
        401: {
            "description": "Could not verify login or password"
        }
    }

    def post(self):
        return {
            "access_token": jwt.encode({"some": "payload"}, "secret", algorithm="HS256"),
            "refresh_token": jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        }


class ResourceView(SwaggerView):
    parameters = []
    security = [{"bearerAuth": []}]
    responses = {
        200: {
            "description": "Login into account. Get access and refresh JWT-tokens",
            "schema": JWTokens
        },
        401: {
            "description": "Could not verify login or password"
        }
    }

    @bearer_auth.login_required
    def get(self):
        return "resource"
