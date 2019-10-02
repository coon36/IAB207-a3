from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Listing
from . import db

bp = Blueprint('result', __name__, url_prefix='/results')

@bp.route('/<id>') 
def result(id): 
  listing = Listing.query.filter_by(id=id).first() 
  return render_template('result.html', listing=listing)

