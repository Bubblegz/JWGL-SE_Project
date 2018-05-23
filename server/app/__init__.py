from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from.student import student as student_blueprint
    app.register_blueprint(student_blueprint)

    from .teacher import teacher as teacher_blueprint
    app.register_blueprint(teacher_blueprint)

    from .root import root as root_blueprint
    app.register_blueprint(root_blueprint)

    return app