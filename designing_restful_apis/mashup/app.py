from flask import Flask, request, jsonify
from apis import lookup_meal

app = Flask(__name__)


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
