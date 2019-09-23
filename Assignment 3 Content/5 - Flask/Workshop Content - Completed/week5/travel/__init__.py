#import flask - from the package import class
from flask import Flask 


#create a function that creates a web application
# a web server will run this web application
def create_app():
    print(__name__)  #let us be curious - what is this __name__ 
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    app.secret_key='utroutoru'
    
    #importing views module here to avoid circular references
    # a commonly used practice.
    from . import views
    app.register_blueprint(views.mainbp)
    
    return app



