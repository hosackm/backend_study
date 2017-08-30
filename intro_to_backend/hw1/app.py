from flask import Flask, render_template, url_for, redirect, request
import codecs

app = Flask(__name__)


@app.route("/<text>")
def index(text):
	text = request.args.get("text", "")
	return render_template("rot13.html", text=text)


@app.route("/submit", methods=["POST"])
def submit():
	text = request.form.get("text", "")
	return redirect(url_for("index", text=text))

if __name__ == "__main__":
	app.run(debug=True)
