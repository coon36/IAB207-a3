from flask import Blueprint, render_template
from flask_login import login_required
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('listings', __name__, url_prefix='/listings')

@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first()
    return render_template('ViewListing.html', listing=listing)

@bp.route('/manage-<id>')
@login_required
def manage(id):
    listing = Listing.query.filter_by(id=id).first()
    return render_template('ManageListing.html', listing=listing)
