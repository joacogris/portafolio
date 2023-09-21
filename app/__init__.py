from flask import Flask, app

import os 


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE_PORT=os.environ.get('FLASK_DATABASE_PORT'),
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app