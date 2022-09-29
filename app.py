import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from random import random

from helpers import apology, login_required, usd, randomNumberGenerator, listToString, decryptionKey, encipher, decipher

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

# Global variables
symbols1 = "{|~}"
symbols2 = "[\]^_`"

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
    return render_template("index.html")

# HISTORY


@app.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    if request.method == "POST":
        text = request.form.get("plaintext").strip()
        text = str(text)
        cipher_data = encipher(text)
        cipher_data[1] = listToString(cipher_data[1])
        db.execute("INSERT INTO cipherData (user_id, cipher_text, d_key) VALUES(?, ?, ?)", session["user_id"], cipher_data[0], cipher_data[1])
        return render_template("encipher.html", txt=cipher_data)
    else:
        return render_template("encipher.html")

# QUOTE


@app.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():
    user_id = session["user_id"]
    valid_keys = []
    cipher_data = db.execute("SELECT id, cipher_text, d_key FROM cipherData WHERE user_id = ? ORDER BY id DESC LIMIT 5", user_id)
    if request.method == "POST":
        cipherText = request.form.get("ciphertext")
        d_key = request.form.get("key")

        # This is to ensure that the user is only able to decrypt the ciphertexts that they have
        # encrypted.
        db_keys = db.execute("SELECT d_key FROM cipherData WHERE user_id = ?", user_id)
        for key in db_keys:
            valid_keys.append(key['d_key'])
        if not d_key in valid_keys:
            return apology("Invalid decryption key")

        plainText = decipher(cipherText, d_key)
        return render_template("decipher.html", txt=plainText, cipher_data=cipher_data)
    else:
        return render_template("decipher.html", cipher_data=cipher_data)


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form.get("data_id")
    user_id = session["user_id"]
    db.execute("DELETE FROM cipherData WHERE id = ? AND user_id = ?", id, user_id)
    return redirect("/decrypt")


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

if __name__ == "__main__":
    app.run(debug=True)
