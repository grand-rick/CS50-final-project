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

Using cs50's login authorization functions as helper functions, I developed my own authorization and verification system. 

The user first logs into the web app in order to have access to the site. If they don't have an account, they create one, and the user's details are stored in a database. For the record, a hash of the password is stored, and not the actual password itself. The hashing algorithm used is the secure 256SHA algorithm that generates 256 bits of 

### Phase 2 -- **Home Page**
After successfully logging in, the user is directed to te homepage. This page gives a brief guide on what to expect ahead, and explains briefly the purpose of the website as well as a dive into it's future.

### Phase 3 -- **Encryption Page**
When the user heads to the encryption page, it renders the `encipher.html` file, which is simple and straight to the point.
![Encryption Page](https://github.com/grand-rick001/CS50-final-project/blob/master/static/images/enc.gif "Encryption Page")