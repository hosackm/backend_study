from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)


@app.route("/")
def index():
    """
    Attempt to read validation flags from request and render the form template.
    """
    errors = {
        "username": request.args.get("username"),
        "password": request.args.get("password"),
        "verification_password": request.args.get("verification_password"),
        "email": request.args.get("email")
    }

    return render_template("form.html", errors=errors)


@app.route("/success/<string:username>")
def success(username):
    return "Welcome, {}".format(username)


@app.route("/", methods=["POST"])
def submit():
    """
    Validate the input from the form.
    Redirect back to "/" if invalid entries.
    Otherwise forward to successful signup page
    """
    # get the values from the form
    username = request.form["username"]
    password = request.form["password"]
    verification_password = request.form["verification_password"]
    email = request.form["email"]

    # validate each entry. REFACTOR ME PLEASE!
    validations = {}
    if not validate_username(username):
        validations["username"] = username
    if not validate_password(password):
        validations["password"] = verification_password
    if not validate_verification_password(password, verification_password):
        validations["verification_password"] = verification_password
    if not validate_email(email):
        validations["email"] = email

    if validations:
        return redirect(url_for("index", **validations))
    else:
        print("redirecting with:", username)
        return redirect(url_for("success", username=username))


def validate_username(user):
    """
    Return True if it is a valid username else False
    """
    user_re = re.compile("^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(user) is not None


def validate_password(passwd):
    """
    Return True if valid password else False
    """
    pass_re = re.compile("^.{3,20}$")
    return pass_re.match(passwd) is not None


def validate_verification_password(passwd, verifypasswd):
    """
    Return True if passwd matches verifypasswd
    """
    return passwd == verifypasswd


def validate_email(email=""):
    """
    Return True if valid email
    """
    if email:
        email_re = re.compile("^[\S]+@[\S]+.[\S]+$")
        return email_re.match(email) is not None
    else:
        return True


if __name__ == "__main__":
    app.run(debug=True)
