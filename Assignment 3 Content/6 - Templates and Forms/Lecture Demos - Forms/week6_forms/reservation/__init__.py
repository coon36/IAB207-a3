from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app=Flask(__name__)
    app.debug=True
    app.secret_key='thisisasecretkey122'

    boostrap = Bootstrap(app)

    from .views import mainbp
    app.register_blueprint(mainbp)

    
    return app
