from flask import Flask, request, render_template, make_response, redirect, url_for
import hmac
import re
from db import db

app = Flask(__name__)

# THIS OBVIOUSLY SHOULDN'T BE ADDED TO A PUBLIC REPO BUT THIS IS JUST A HOMEWORK ASSIGNMENT
SECRET = b"SUPERSECRETSECRETSTUFF"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Render template if we aren't here for a POST
    if request.method == "GET":
        return render_template("signup.html", errors=None, values=None)

    # validate entries that were POSTed in form
    errors = validate_form(request.form)
    if any(errors.values()):
        # get back the values that were entered to populate the form
        values = dict(username=request.form.get("username"),
                      email=request.form.get("email"))
        return render_template("signup.html", errors=errors, values=values)

    # add user to database
    username = request.form.get("username")
    password = request.form.get("password")
    user_id = add_user_to_db(username, password)

    # user user_id and password generate a cookie
    cookie = generate_cookie(user_id)

    # create response and add cookie to it
    response = make_response(redirect(url_for("welcome")))
    response.set_cookie("user_id", cookie)

    return response


@app.route("/welcome")
def welcome():
    cookie = request.cookies.get("user_id")

    if valid_cookie(cookie):
        # lookup user name in db from info in cookie
        user_id = cookie.split("|")[0]
        username = db.get_username_by_user_id(user_id)
        return render_template("welcome.html", username=username)
    else:
        # invalid cookie redirect to signup page
        return redirect(url_for("signup"))


def generate_cookie(user_id):
    """
    Look up hashed pass in database by user_id and create a string
    """
    hashed_password = db.get_hashed_pass_by_user_id(user_id)
    return "{}|{}".format(user_id, hashed_password)


def valid_cookie(cookie):
    """
    Lookup hashed password stored in database by user_id and see if it matches what's in the cookie
    """
    user_id, hashpass = cookie.split("|")
    dbhash = db.get_hashed_pass_by_user_id(user_id)
    return hashpass == db.get_hashed_pass_by_user_id(user_id)


def add_user_to_db(username, password):
    """
    Store username and hash/salted password in db
    """
    hashed_password = hmac.new(SECRET, bytes(password, encoding="utf8")).hexdigest()
    user_id = db.add_user(username, hashed_password)
    return user_id


def validate_form(form):
    """
    Take the form and validate every entry by calling the corresponding validate function
    """
    username = form.get("username")
    password = form.get("password")
    verify = form.get("verify")
    email = form.get("email")

    return {
        "username": not username_is_valid(username),
        "password": not password_is_valid(password),
        "verify": not verify_is_match(verify, password),
        "email": not email_is_valid(email)
    }


def username_is_valid(username):
    """
    Return True if it is a valid username else False
    """
    user_re = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(username) is not None


def password_is_valid(password):
    """
    Return True if valid password else False
    """
    pass_re = re.compile("^.{3,20}$")
    return pass_re.match(password) is not None


def verify_is_match(verify, password):
    """
    Return True if verify matches password
    """
    print("matching", verify, password)
    return password == verify


def email_is_valid(email):
    """
    Return True if valid email or no email
    """
    if email:
        email_re = re.compile("^[\S]+@[\S]+.[\S]+$")
        return email_re.match(email) is not None
    return True


if __name__ == "__main__":
    app.run(debug=True)
