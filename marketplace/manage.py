from flask_login import login_required
from .models import Listing, Bid, User, Transaction
from . import db
from datetime import datetime, date

bp = Blueprint('manage', __name__, url_prefix='/manage')


# @bp.route('/<id>')
# @login_required
# def manage(id):
#     listing = Listing.query.filter_by(id=id).first_or_404()
#     bids = Bid.query.filter_by(listing_id=id).join(User, Bid.user_id==User.id).\
#     add_columns(User.id, User.user_name, Bid.listing_id, Bid.contact_number,
#     Bid.date_of_bid).all()
#     return render_template('ManageListing.html', listing=listing, bids=bids)

@bp.route('/<id>', methods=['GET', 'POST'])
@login_required
def manage(id):
    listing = Listing.query.filter_by(id=id).first_or_404()

    bids = Bid.query.filter_by(listing_id=id).join(User, Bid.user_id==User.id).\
    add_columns(User.id, User.user_name, Bid.listing_id, Bid.contact_number,
    Bid.date_of_bid).all()

    purchase = Transaction.query.filter_by(listing_id=id).join(User,
    Transaction.user_id==User.id).add_columns(User.id, User.user_name,
    Transaction.id, Transaction.purchase_date).first()

    selected = Transaction(purchase_date = date.today(), user_id = request.args.get('user_id'), listing_id = request.args.get('listing_id'))
    db.session.add(selected)
    db.session.commit()

    return render_template('ManageListing.html', listing=listing, bids=bids, purchase=purchase, selected=selected)
