from flask import Flask

app = Flask(__name__)


def create_app():
    app.config["SECRET_KEY"] = "your-secret-key"
    return app
