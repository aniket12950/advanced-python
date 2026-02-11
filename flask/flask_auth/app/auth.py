# flask_auth/app/auth.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db, bcrypt

auth = Blueprint('auth', __name__)


# ---------------- REGISTER ----------------
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already exists ❌", "danger")
            return render_template("register.html", email=email)

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful 🎉 Please login.", "success")
        return redirect(url_for('auth.login'))

    return render_template("register.html")


# ---------------- LOGIN ----------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful ✅", "success")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid email or password ❌", "danger")
            return render_template("login.html", email=email)

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully 👋", "success")
    return redirect(url_for('auth.login'))
