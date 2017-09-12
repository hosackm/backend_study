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
    user = session.query(User).filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return True


@app.route("/users", methods=["POST"])
def users():
    # get username and password from request arguments
    username = request.args.get("username")
    password = request.args.get("password")

    # make sure username and password were provided
    if not username or not password:
        return jsonify({"error": "Must provide a username and password"})

    # check if user already exists
    existent_user = session.query(User).filter_by(username=username).first()
    if existent_user:
        return jsonify({"error": "That username already exists."})

    # Create User
    user = User(username=username)
    user.hash_password(password)

    # Add to database
    session.add(user)
    session.commit()

    return (jsonify({"username": username}), 201)


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = session.query(User).filter_by(id=id).first()
    if not user:
        return jsonify({"error": "That user doesn't exist"})

    return jsonify(user.serialize())


@app.route("/bagels", methods=["GET"])
@auth.login_required
def bagels():
    return jsonify({"bagels": ["onion", "asiago", "jalapeno", "everything"]})


if __name__ == "__main__":
    app.run(debug=True)
