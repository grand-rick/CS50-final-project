# CIPHER WEB APP
### Video Demo:  <https://youtu.be/nFcABpXPPqw>
## Summary:
  > I created a cipher web app, (*an innovation of the caesar cipher*), that enciphers and deciphers data using a randomly generated key that is encrypted and decrypted as well.
  > The algorithm produces safe cipher text, that can only be deciphered using my deciphering algorithm.

___

|**File / Folder**| Functionality                                        |
| :---------------| :--------------------------------------------------- |
| static folder   |Contains a css, javascript, images and favicon files             |
| templates folder| contains template (`.html`) files that are rendered  |
| flask_session and \__pycache\__ | collaborate to manage login sessions |
| app.py          | contains the logic for running the web app           |
| cipher.db       | databases that stores data as required               |
| helpers.py      | contains helper functions that are used in `app.py`  |
| requirements.txt| contains all the project dependencies used           | |
| `.html` files   | are files that are rendered and displayed by the app |

---
> To run the program, in two ways:
1. To run it in a development server
```python
    flask run
```
2. To run it in a production server
```python
    python3 app.py
```

*In both above cases, a link will be generated, where upon clicking, the web app will be running*

## **In-depth project description**
---

### Phase 1 -- **Logging in**
The user is welcomed by an enticing user interface design. The wavy animation gives the website more feeling and liveliness.

Using cs50's login authorization helper functions, I developed my own authorization and verification system. 

The user first logs into the web app in order to have access to the site. If they don't have an account, they create one, and the user's details are stored in a database. For the record, a hash of the password is stored, and not the actual password itself.

### Phase 2 -- **Home Page**
After successfully logging in, the user is directed to te homepage. This page gives a brief guide on what to expect ahead, and explains briefly the purpose of the website as well as a dive into it's future.

### Phase 3 -- **Encryption Page**
When the user heads to the encryption page, it renders the `encipher.html` file, which is simple and straight to the point.
![Encryption Page](./static/images/enc.gif "Encryption Page")

When the user enters their data and clicks the button to encrypt, 5 main processes occur. 

1. The data is retrieved using the `POST` method and stored in a variable as a string.
2. It is then encrypted using the caesar cipher by use of a random key.
3. The characters are shifted forwards in the ASCII table, by the random key to become cipher text.
4. The random key is then encrypted into an eight-character ASCII text with the key within., now referred to as the decryption key.
5. The cipher text and the decryption key are then stored in the database.

>After encrypting, a new interface pops up that gives more details for the next step. A live alert emerges, informing the user that the encrypted data and decryption key are stored in the database, and that they should check the decryption page for more details.

