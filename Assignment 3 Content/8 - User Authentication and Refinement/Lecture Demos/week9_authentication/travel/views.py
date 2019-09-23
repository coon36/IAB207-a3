from flask import Blueprint, render_template, request, session
from flask_login import login_required

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')  # this is a decorator used in flask
@login_required
def index():
    #if 'email' in session:
    #    str='<h1>hello world ---' + session['email'] + '</h1>'
    #else:
    #    str='<h1>hello world</h1>'
    #return str
    return render_template('index.html')
