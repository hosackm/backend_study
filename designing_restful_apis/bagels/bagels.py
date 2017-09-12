from flask import Flask, g, request, jsonify
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base


auth = HTTPBasicAuth()
app = Flask(__name__)
engine = create_engine('sqlite:///bagelusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@auth.verify_password
def verify_password(username, password):
    ...


@app.route("/users", methods=["POST"])
def users():
    # get username and password from request arguments
    username = request.args.get("username")
    password = request.args.get("password")

    # make sure username and password were provided
    if not username or not password:
        return jsonify({"error": "Must provide a username and password"})

    # Create User
    user = User(username=username)
    user.hash_password(password)

    # Add to database
    session.add(user)
    session.commit()

    return (jsonify({"username": username}), 201)


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    ...


@app.route("/bagels", methods=["GET"])
@auth.login_required
def bagels():
    ...


if __name__ == "__main__":
    app.run(debug=True)
