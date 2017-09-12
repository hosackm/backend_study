from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "a simple secret key"
WTF_CSRF_SECRET_KEY = "a simple secret key"


class SimpleForm(FlaskForm):
    name = StringField("name", validators=[DataRequired("Please enter a name")])
    email = StringField("email", validators=[Email("Please enter a valid email")])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = SimpleForm()
    if request.method == "GET":
        return render_template("form.html", form=form)

    if form.validate():
        return render_template("success.html")

    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
