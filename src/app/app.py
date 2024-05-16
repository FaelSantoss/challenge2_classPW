from flask import Flask

from infra.views import init_views
from infra.database import init_database


def create_app():
    app = Flask(
        __name__, template_folder="../ui/templates", static_folder="../ui/static"
    )

    app.config["UPLOAD_FOLDER"] = "static/"
    app.config["SECRET_KEY"] = "1234"
    init_views(app)
    init_database()

    return app
