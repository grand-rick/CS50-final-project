import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from random import randint, shuffle, random

# Global variables
symbols1 = "{|~}"
symbols2 = "[\]^_`"

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

def encipher(text):
    """
    It takes a string, and returns a list of two strings, the first being the encrypted string, and the
    second being the decryption key.

    :param text: The text to be encrypted
    :return: A list of the encrypted text and the decryption key.
    """
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
        elif character in symbols1:
            tmp -= 123 # {
            tmp = (tmp + key) % 4
            tmp += 123
        elif character in symbols2:
            tmp -= 91 # [
            tmp = (tmp + key) % 6
            tmp += 91
        else:
            tmp -= 32 # SPACE BAR
            tmp = (tmp + key) % 33
            tmp += 32
        char = chr(tmp)
        newText += char
    values.append(newText)
    values.append(decryptionKey(key))
    return values


def decipher(cipherText, d_key):
    """
    The function takes the ciphertext and the decryption key as parameters. It then uses the fourth
    character in the decryption key to determine the decryption key. It then uses list comprehension to
    iterate through the ciphertext and decrypt it.

    :param cipherText: The text that is to be decrypted
    :param d_key: The decryption key
    :return: The decrypted text.
    """
    d_num = 90

    # Getting the fourth character in the decryption key and subtracting 90 from it.
    for i in range(len(d_key)):
        if i == 3:
            d_key = (ord(d_key[i]) - d_num)

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
        elif character in symbols1:
            tmp -= 123 # {
            tmp = (tmp - d_key) % 4
            tmp += 123
            if tmp < 0:
                tmp += 4
        elif character in symbols2:
            tmp -= 91 # [
            tmp = (tmp - d_key) % 6
            tmp += 91
            if tmp < 0:
                tmp += 6
        else:
            tmp -= 32 # SPACE BAR
            tmp = (tmp - d_key) % 33
            tmp += 32
            if tmp < 0:
                tmp += 33
        newText += chr(tmp)

    return newText

def randomNumberGenerator():
    """
    It generates a random number between -32 and 36, and if the number is even, it is negated.
    :return: A random number between -32 and 36 that is odd.
    """
    num = 0

    while num == 0:
        num = randint(-32, 36)
        if num % 2 == 0:
            num = -num

    return num

def decryptionKey(key):
    # Global variable d_num
    d_num = 90
    """
    It generates 8 random numbers, adds 90 to them, converts them to characters, and then inserts the
    key into the fourth character

    :param key: The key that the user inputs
    :return: A list of 10 characters
    """
    SIZE = 8
    random_numbers = []
    random_characters = []
    random = randomNumberGenerator()

    # Getting 8 random numbers and adding 90 to them for later character conversion
    for i in range(SIZE):
        copy = random
        flag = 1
        # Ensuring a number is not the same as the previous
        while flag == True:
            if copy != random:
                tmp = random + d_num
                random_numbers.append(tmp)
                flag = 0
            else:
                random = randomNumberGenerator()

    # Converting the 8 random numbers to characters
    for i in range(SIZE):
        if i == 3:
            # Reassigning the fourth character as the key
            key += d_num
            random_characters.append(chr(key))
            continue
        char = chr(random_numbers[i])
        random_characters.insert(i, char)

    return random_characters

# Function to convert a list to a string
def listToString(s):

    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
