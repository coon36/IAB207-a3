from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('listings', __name__, url_prefix='/listings')


@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first_or_404()
    bids = Bid.query.filter_by(listing_id=id).first()
    return render_template('ViewListing.html', listing=listing, bids = bids)
    return render_template('ViewListing.html', listing=listing)
