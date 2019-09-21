from flask import Blueprint, render_template, request, session

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')  # this is a decorator used in flask
def index():
    #if 'email' in session:
    #    str='<h1>hello world ---' + session['email'] + '</h1>'
    #else:
    #    str='<h1>hello world</h1>'
    #return str
    return render_template('index.html')

@mainbp.route('/login', methods=['GET','POST'])
def login():
    print(request.args.get('email'))
    print(request.args.get('pwd'))

    print(request.form.get('email'))
    
    session['email']=request.args.get('email')
    return render_template('login.html')

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
    return 'Session has been cleared'