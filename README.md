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
> To run the program, run these commands on your terminal
1. To run it in a development server
```bash
    flask run
```
2. To run it in a production server
```bash
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

When the user enters their data and clicks the button to encrypt, the following processes occur:

1. The data is retrieved using the `POST` method and stored in a variable as a string.
2. It is then encrypted as illustrated below, to generate the cipher text and decryption key.
3. The cipher text and the decryption key are then stored in the database.

#### **THE ENCRYPTION LOGIC**
---
For the encryption, the algorithm is essentially a more complex innovation of the caesar cipher.

First of all, the program generates a random number between -32 and 36. If the number is even, it is negated. The number should fall within these bounds because when the first(a) and last(z) alphabets are added respectively with the upper and lower limits of the generated numbers, they will still be within the range of useable ASCII values. 

The random number then becomes the key. The program then shifts all characters of the plain text forwards by the key against the alphabet, to generate the cipher text.

Next, the key is encrypted using the following steps. 
* First, 8 random numbers are generated in the same way as stated before. The numbers have 90 added to them so that they can fall within the category of useable ASCII values.
* They algorithm ensures that no number is the same as the previous one. 
* The numbers are then converted to their respective ASCII values, with the fourth character being reassigned as the key.

The program then returns a list with the cipher text as the first element and the decryption key as the second.

>After encrypting, a new interface pops up that gives more details for the next step. A live alert emerges, informing the user that the encrypted data and decryption key are stored in the database, and that they should check the decryption page for more details.

![Encrypted Data and Decryption Key](./static/images/enc1.gif "Encrypted data and decryption key")

### Phase 4 - **Decryption Page**
After the user gotten the cipher data (*Encryption key and Decryption key*), the desired result can be retrieved from the decryption page.
In this page, the app renders a simple interface that shows:

* Two input fields for receiving the cipher data.
* Last 5 sets of cipher data that were stored, in order of the most recent.

![Decryption Page- default](./static/images/dec.gif)
![Decryption Page- stored](./static/images/dec1.gif)

When the user enters the cipher data and clicks the button to decrypt, 5 main processes occur:

1. The cipher text and decryption key are fetched using the `POST` method stored in variables as strings.
2. The sets of cipher data are then decrypted as explained below, to get the plain text that is then displayed.

#### **THE DECRYPTION LOGIC**
---

For the decryption, I've written a function that takes the cipher text and the decryption key as parameters. It then takes the fourth character of the decryption key, converts it back to a number and subtracts 90 from it to get the key.

Using that key, the function iterates over all the characters of the cipher text, shifting their position backwards against the alphabet to get the plain text.

The function then returns the plain text as a string.

![Decryption Page- decrypting](./static/images/dec2.gif)
![Decryption Page- result](./static/images/dec3.gif)

## Conclusion
---
The project revolved around juggling both the frontend and backend areas of a website. This is in turn boosted my understanding of the web space and narrowed my preferences (frontend or backend) when it comes to web development. All in all, I really enjoyed this wholesome experience and hyped to learn even more with the CS50's courses.