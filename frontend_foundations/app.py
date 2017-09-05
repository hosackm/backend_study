from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import bleach

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route("/")
@app.route("/restaurants")
def restaurants():
    # get all restaurants in the database and render
    restaurants = session.query(Restaurant).all()
    return render_template("index.html", restaurants=restaurants)


@app.route("/restaurant/new", methods=["GET", "POST"])
def new_restaurant():
    # if we were linked here render the form
    if request.method == "GET":
        return render_template("new.html")

    # get from the form
    restaurant_name = request.form.get("restaurant_name")
    if restaurant_name:
        session.add(Restaurant(name=bleach.clean(restaurant_name)))
        session.commit()

    # back to homepage
    return redirect(url_for("restaurants"))


@app.route("/restaurant/<int:restaurant_id>/edit", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    # check if this restaurant exists
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return abort(404)

    # if we were linked here render the form
    if request.method == "GET":
        return render_template("edit.html", restaurant=restaurant)

    # update db entry
    newname = request.form.get("restaurant_name")
    restaurant.name = bleach.clean(newname)
    session.add(restaurant)
    session.commit()

    # back to homepage
    return redirect(url_for("restaurants"))


@app.route("/restaurant/<int:restaurant_id>/delete", methods=["GET", "POST"])
def delete_restaurant(restaurant_id):
    # check if this restaurant exists
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return abort(404)

    # if we were linked here render the form
    if request.method == "GET":
        return render_template("delete.html", restaurant=restaurant)

    # remove from database
    session.delete(restaurant)
    session.commit()

    # back to homepage
    return redirect(url_for("restaurants"))


@app.route("/restaurant/<int:restaurant_id>/menu")
def menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return abort(404)

    menuitems = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template("menu.html", restaurant=restaurant, menuitems=menuitems)


@app.route("/restaurant/<int:restaurant_id>/menu/new", methods=["POST", "GET"])
def new_menu_item(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    if not restaurant:
        return abort(404)

    if request.method == "GET":
        return render_template("newitem.html", restaurant=restaurant)

    # get from the form
    menu_item_name = bleach.clean(request.form.get("menu_item_name"))
    menu_item_price = bleach.clean(request.form.get("menu_item_price"))
    menu_item_course = bleach.clean(request.form.get("menu_item_course"))
    menu_item_description = bleach.clean(request.form.get("menu_item_description"))

    # create menu item and add to db
    menu_item = MenuItem(name=menu_item_name,
                         description=menu_item_description,
                         price=menu_item_price,
                         course=menu_item_course,
                         restaurant_id=restaurant_id)
    session.add(menu_item)
    session.commit()

    return redirect(url_for("menu", restaurant_id=restaurant_id))


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/edit", methods=["POST", "GET"])
def edit_menu_item(restaurant_id, menu_item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).first()
    if not restaurant or not menu_item:
        return abort(404)

    if request.method == "GET":
        return render_template("edititem.html", restaurant=restaurant, menu_item=menu_item)

    # get from the form
    menu_item_name = bleach.clean(request.form.get("menu_item_name"))
    menu_item_price = bleach.clean(request.form.get("menu_item_price"))
    menu_item_course = bleach.clean(request.form.get("menu_item_course"))
    menu_item_description = bleach.clean(request.form.get("menu_item_description"))

    # set the values in the db entry
    menu_item.name = menu_item_name
    menu_item.price = menu_item_price
    menu_item.course = menu_item_course
    menu_item.description = menu_item_description

    # add to the session and commit
    session.add(menu_item)
    session.commit()

    return redirect(url_for("menu", restaurant_id=restaurant_id))


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/delete", methods=["POST", "GET"])
def delete_menu_item(restaurant_id, menu_item_id):
    # get restaurant and menu item from db
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    menu_item = session.query(MenuItem).filter_by(id=menu_item_id).first()
    if not restaurant or not menu_item:
        return abort(404)

    # delete the menu item from the db if it exists
    session.delete(menu_item)
    session.commit()

    return redirect(url_for("menu", restaurant_id=restaurant_id))


# JSON API methods
@app.route("/restaurants/json")
def get_restaurants_json():
    restaurants = [r.serialize() for r in session.query(Restaurant).all()]
    if not restaurants:
        abort(404)

    return jsonify({"restaurants": restaurants})


@app.route("/restaurant/<int:restaurant_id>/menu/json")
def get_menu_json(restaurant_id):
    menuitems = [mi.serialize() for mi in session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()]
    if not menuitems:
        abort(404)

    return jsonify({"menuitems": menuitems})


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_item_id>/json")
def get_menu_item_json(restaurant_id, menu_item_id):
    menuitem = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_item_id).first()
    if not menuitem:
        abort(404)

    return jsonify({"menuitem": menuitem.serialize()})

if __name__ == "__main__":
    app.run(debug=True)
