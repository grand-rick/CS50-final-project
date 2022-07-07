import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from random import randint, shuffle, random


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# This script enciphers a string of text using a Caesar cipher with the given number.
def encipher(text):
    values = []
    newText = ""
    key = randomNumberGenerator()
    for character in text:
        tmp = ord(character)
        if character.isupper():
            tmp -= ord("A")
            tmp = (tmp + key) % 26
            tmp += ord("A")
        elif character.islower():
            tmp -= ord("a")
            tmp = (tmp + key) % 26
            tmp += ord("a")
        else:
            tmp += key
        newText += chr(tmp)

    values.append(newText)
    values.append(key)
    return values


# This function takes in a cipher text and a decryption key,
#  and returns the decrypted text. It does this by
#  looping through each character in the cipher text and shifting it by the decryption key.
def decipher(cipherText, d_key):
    # Using list comprehension and join
    newText = ""
    for character in cipherText:
        tmp = ord(character)
        if character.isupper():
            tmp -= ord("A")
            tmp = (tmp - d_key) % 26
            if tmp < 0:
                tmp += 26
            tmp += ord("A")
        elif character.islower():
            tmp -= ord("a")
            tmp = (tmp - d_key) % 26
            tmp += ord("a")
            if tmp < 0:
                tmp += 26
        else:
            tmp -= d_key
        newText += chr(tmp)

    return newText

# This function generates a random number between -32 and 36, inclusive.
#  If the number is even, it is negated.
def randomNumberGenerator():
    num = 0

    while num < -32 or num > 36 or num == 0:
        num = randint(-100, 100)
        if num % 2 == 0:
            num = -num

    return num


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
