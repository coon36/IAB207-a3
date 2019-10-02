from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from .models import Listing
from .forms import ItemCreationForm
from datetime import datetime
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    listing = Listing.query.filter_by(date=date_posted).all()
    return render_template('Homepage.html', listing=listing)

@bp.route('/results')
def result():
    return render_template('result.html')

@bp.route('/sellerhistory')
# @login_required
def history():
    return render_template('sellerhistory.html')


def check_upload_file(form):
    fp = form.listing_img_url.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(BASE_PATH, 'static/Images', secure_filename(filename))
    db_upload_path = '/static/Images/'+ secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path


@bp.route('/create', methods = ['GET', 'POST'])
def create():
    print('In create item')
    form = ItemCreationForm()
    if form.validate_on_submit():
        print("Form has been submitted successfully")
        db_file_path = check_upload_file(form)

        item = Listing(listing_title = form.listing_title.data,
        purchase_price = form.purchase_price.data,
        description = form.description.data,
        game_condition = form.game_condition.data,
        game_release_date = form.game_release_date.data,
        game_genre = form.game_genre.data,
        game_classification = form.game_classification.data,
        game_platform = form.game_platform.data,
        listing_img_url = db_file_path)



        db.session.add(item)

        db.session.commit()

    return render_template('CreateListing.html', form = form)
