from flask import Blueprint, render_template


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return '<h1>Starter code for the assessment<h1>'

@bp.route('/manageitems')
def manage():
    return render_template('manage.html')

@bp.route('/results')
def result():
    return render_template('result.html')


@bp.route('/sellerhistory')
def history():
    return render_template('sellerhistory.html')
