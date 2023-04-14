from flask import Flask

from src.routes.download import download_bp
from src.routes.upload import upload_bp


def gather_all_routes() -> list:
    return [
        upload_bp,
        download_bp,
    ]


def imbue_app_with(blueprints: list, app: Flask):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    return app
