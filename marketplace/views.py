from flask import Blueprint, render_template


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('Homepage.html')

@bp.route('/manageitems')
def manage():
    return render_template('ManageListing.html')

@bp.route('/results')
def result():
    return render_template('result.html')


@bp.route('/sellerhistory')
def history():
    return render_template('sellerhistory.html')

@bp.route('/create')
def create():
    return render_template('CreateListing.html')
