# Homework 4

This homework is a combination of the topics we covered in this chapter on user authentication.  It involves cookies for persisting a user's login, hashing user passwords, and salting hashed passwords.

## Database

The database has one table called users.  The columns are user_id, username, and password.  The password that is stored is hashed using the hmac module.  The default encryption algorithm is sha256.

## Routes

The following routes are made available by the application:

    * /signup
    * /welcome
    * /login
    * /logout

### /signup
This route displays a form with username, pass, verify pass, and optional email. This route validates the entries and if they look good it adds a user to the database and stores their hashed password.

### /login
This route displays a form with username and password. Once the form is posted it checks that the entered password matches the hashed password in the database after using the same hashing algo. If it does it sets `{"user_id": "<user_id>|<hashed_password>"}` as a cookie.

### /logout

## Cookie

The cookie consists of one key/value pair:

    `{"user_id": <user_id>|<hashed_password>}`

where `<user_id>` is the integer in the database associated with this user and `<hashed_password>` is the hashed password stored in the database


## Limitations

The app doesn't check if a user exists before it creates a new one.  This means that two matching usernames can be added.  Whatever username comes back first in our database queries is the one we will compare passwords on.

The SECRET used to hash the passwords is hardcoded in app.py.  This is terrible practice but this is just a homework assignment.  Plus the algorithm we're using is also in the same file so basically we aren't securing the passwords at all `¯\_(ツ)_/¯`
