from flask import Blueprint, render_template, abort
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('listings', __name__, url_prefix='/listings')


@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first_or_404()
    return render_template('ViewListing.html', listing=listing)
