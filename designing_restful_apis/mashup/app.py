from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from apis import lookup_meal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(250))

    def __init__(self, name, address, image):
        self.name = name
        self.address = address
        self.image = image

    def __repr__(self):
        return "<Restaurant {}>".format(self.name)


@app.route("/restaurants", methods=["POST"])
def restaurants_post():
    location = request.args.get("location")
    meal_type = request.args.get("mealType")

    # check that location and meal type were provided
    if any([not p for p in (location, meal_type)]):
        return jsonify({"error": "Must provide location and meal_type in url."})

    # lookup meal
    restaurant_info = lookup_meal(location, meal_type)

    # store in db
    db.session.add(Restaurant())

    # send JSON response
    return jsonify(restaurant_info)


@app.route("/restaurants", methods=["GET"])
def restaurants_get():
    # lookup all restaurants

    return jsonify({})


@app.route("/restaurant/<int:id>", methods=["GET"])
def restaurant_lookup(id):
    # lookup restaurant by id

    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
