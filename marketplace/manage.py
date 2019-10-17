from flask import Blueprint, render_template, abort
from flask_login import login_required
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('manage', __name__, url_prefix='/manage')


@bp.route('/<id>')
@login_required
def manage(id):
    listing = Listing.query.filter_by(id=id).first_or_404()
    bids = Bid.query.filter_by(listing_id=id).join(User, Bid.user_id==User.id).\
    add_columns(User.id, User.user_name, Bid.listing_id, Bid.contact_number,
    Bid.date_of_bid, bid.purchase_price).all()
    return render_template('ManageListing.html', listing=listing, bids=bids)
