from flask import Blueprint,render_template

#create a blueprint
mybp = Blueprint('main',__name__)

#register routes with the blueprint
@mybp.route('/')
def index():
    print('hello world')
    return render_template('index12.html')

