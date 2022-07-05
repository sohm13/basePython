from flask import Blueprint, render_template



about_app = Blueprint('about_app', __name__)

@about_app.route("/")
def about():
    return render_template("about.html")
