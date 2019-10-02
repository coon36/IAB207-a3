from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    listing = Listing.query.filter_by(date=date_posted).all()
    return render_template('Homepage.html', listing=listing)

@bp.route('/manageitems')
# @login_required
def manage():
    return render_template('ManageListing.html')

@bp.route('/results')
def result():
    return render_template('result.html')

@bp.route('/sellerhistory')
# @login_required
def history():
    return render_template('sellerhistory.html')

@bp.route('/create')
# @login_required
def create():
    return render_template('CreateListing.html')
