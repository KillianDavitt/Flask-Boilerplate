""" Main views for the stats application
"""
import bcrypt

from flask_login import login_user, login_required
from flask import render_template, redirect, url_for, request

from app import app, db, lm
from .models import User


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("index.html")
                 


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@lm.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))
