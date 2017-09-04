import bleach
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant  # , MenuItem

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants")
def restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template("index.html", restaurants=restaurants)


@app.route("/new", methods=["GET", "POST"])
def new_restaurant():
    if request.method == "GET":
        return render_template("new.html")

    restaurant_name = request.form.get("restaurant_name")
    if restaurant_name:
        session.add(Restaurant(name=restaurant_name))
        session.commit()

    return redirect(url_for("restaurants"))


@app.route("/edit/<int:restaurant_id>", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if request.method == "GET":
        return render_template("edit.html", restaurant=restaurant)

    # update db entry
    newname = request.form.get("restaurant_name")
    restaurant.name = newname
    session.add(restaurant)
    session.commit()

    return redirect(url_for("restaurants"))


@app.route("/delete/<int:restaurant_id>", methods=["GET", "POST"])
def delete_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if request.method == "GET":
        return render_template("delete.html", restaurant=restaurant)

    # remove from database
    session.delete(restaurant)
    session.commit()

    return redirect(url_for("restaurants"))


if __name__ == "__main__":
    app.run(debug=True)
