from flask import Flask
from view import LoginView, IndexView, ResourceView
from flasgger import Swagger

app = Flask(__name__)
# app.secret_key = 'some secret key'

swagger_template = {
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            },
            "basicAuth": {
                "type": "http",
                "scheme": "Basic",
            },
        }
    },
    # 'security': [{"bearerAuth": []}],
}
swagger = Swagger(app, template=swagger_template)
app.add_url_rule('/', methods=["GET"], view_func=IndexView.as_view('index'))
app.add_url_rule('/login', methods=["POST"], view_func=LoginView.as_view('login'))
app.add_url_rule('/resource', methods=["GET"], view_func=ResourceView.as_view('resource'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
