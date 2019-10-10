from flask import Blueprint, render_template, abort
from flask_login import login_required
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('listings', __name__, url_prefix='/listings')


@bp.route('/<id>')
def show(id):
    listing = Listing.query.filter_by(id=id).first()
    if listing is None:
        abort(404)
        return render_template('404.html')
    else:
        return render_template('ViewListing.html', listing=listing)
