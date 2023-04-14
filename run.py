from flask import Flask

from src.app import gather_all_routes, imbue_app_with


def build_app():
    app = Flask(__name__)
    routes = gather_all_routes()
    app = imbue_app_with(routes, app)

    return app


if __name__ == "__main__":
    build_app().run()
