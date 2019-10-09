from flask import Blueprint, render_template
from .models import Listing
from . import db


bp = Blueprint('result', __name__, url_prefix='/results')

# @bp.route('/<id>') 
# def result(id): 
#     listing = Listing.query.filter_by(id=id)
#     return render_template('result.html', listing=listing)


@bp.route('/<game_genre>') 
def result(game_genre): 
  listing = Listing.query.filter_by(game_genre=game_genre).all() 
  return render_template('result.html', listing=listing)

# @bp.route('/<game_platform>') 
# def result(game_platform): 
#   listing = Listing.query.filter_by(game_platform=game_platform).all() 
#   return render_template('result.html', listing=listing)

