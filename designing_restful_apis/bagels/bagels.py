from flask import Flask, g, request
from flask_httpauth import HTTPBasicAuth


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
    ...


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    ...


@app.route("/bagels", methods=["GET"])
@auth.login_required
def bagels():
    ...


if __name__ == "__main__":
    app.run(debug=True)
