from flask import Flask, render_template, request
from flask import abort, redirect, url_for, make_response


app = Flask(__name__)


@app.route('/')
def index():
 return redirect("/about")


@app.route('/about')
def about():
 return render_template("about.html")


@app.route('/contact')
def contact():
 return render_template("contact.html")


@app.route('/gallery')
def gallery():
 return render_template("gallery.html")


@app.route('/error_denied')
def error_denied():
 abort(401)


if __name__ == '__main__':
 app.run(debug=False, port=8000)