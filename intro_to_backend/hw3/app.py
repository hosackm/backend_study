from flask import Flask, render_template, request, redirect, url_for
from db import db

app = Flask(__name__)


@app.route("/")
def welcome():
    # fetch the 10 most recent posts
    posts = db.get_most_recent_posts()
    return render_template("welcome.html", posts=posts)


@app.route("/newpost", methods=["GET", "POST"])
def submit():
    # render form if they're here from GET
    if request.method == "GET":
        return render_template("submit.html", errors={}, params={})

    # validate params and display error messages
    title, content = request.form["subject"], request.form["content"]
    errors = validate_form(title, content)
    if any(errors.values()):
        params = dict(title=title, content=content)
        return render_template("submit.html", errors=errors, params=params)

    # add post to db and redirect to post page
    id = db.add_post(title, content)
    return redirect(url_for("posts", post_id=id))


@app.route("/posts/<int:post_id>")
def posts(post_id):
    # get the post from the database using id instead of this hardcoded one
    post = db.get_post_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return redirect(url_for("notfound"))


@app.route("/notfound")
def notfound():
    return render_template("404.html")


def validate_form(title, content):
    errors = dict(title=False, content=False)
    if not title:
        errors["title"] = True
    if not content:
        errors["content"] = True
    return errors


if __name__ == "__main__":
    app.run(debug=True)
