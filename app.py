import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from random import random

from helpers import apology, login_required, usd, cipher, decipher, randomNumberGenerator

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///cipher.db")

# # Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# HOMEPAGE


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # print("\t\t\tGRAND RICK PRODUCTIONS.")
    # print("Hello there, type 'e' to encrypt or 'd' to decrypt.")
    # while True:
    #     user_input = input("What would you like to do? ").strip()
    #     if user_input == "e":
    #         text = input("Enter data to encrypt: ").strip()
    #         results = encipher(text)
    #         print("Your encrypted data is %s "%(results[0]))
    #         print("Your decryption key is %d "%(results[1]))
    #         break
    #     elif user_input == "d":
    #         text = input("Enter data to decrypt: ").strip()
    #         d_key = int(input("Enter the encryption key: ").strip())
    #         plainText = decipher(text, d_key)
    #         print("Your decrypted data is %s "%(plainText))
    #         break
    return render_template("index.html")

# HISTORY


@app.route("/encipher", methods=["GET", "POST"])
# @login_required
def encipher():
    if request.method == "POST":
        plaintext = request.form.get("plaintext")
        return render_template("encipher.html", txt=plaintext)
    else:
        return render_template("encipher.html")

# QUOTE


@app.route("/decipher", methods=["GET", "POST"])
# @login_required
def decipher():
    if request.method == "POST":
        ciphertext = request.form.get("ciphertext")
        key = request.form.get("key")
    return render_template("decipher.html")

# STORE DATA


@app.route("/store", methods=["GET", "POST"])
@login_required
def store():
    return render_template("store.html")
# LOGIN


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# LOG OUT


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# REGISTER


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensuring the fields are not blank
        if not username:
            return apology("Missing username")

        # Ensuring there is a password
        if not password or not confirmation:
            return apology("Missing password")

        # If password and apology don't match return error
        if password != confirmation:
            return apology("Passwords do not match")

        # Ensure password is atleast 6 characters
        if len(password) < 6:
            return apology("Password Length must be at least 6 characters long")

        # If username is already taken, return error
        name_check = db.execute("SELECT username FROM users WHERE username = ?", username)

        if not name_check:
            # Encrypt the password
            wordpass = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, wordpass)

            # Query database for username
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)

            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]

            # Redirect user to home page
            return redirect("/")
        else:
            return apology("Username already taken, please try another one")
    else:
        return render_template("register.html")



