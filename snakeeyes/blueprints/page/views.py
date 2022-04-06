from flask import Blueprint, render_template

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
@page.route("/home")
def home():
    return render_template("home.html")


@page.route("/about")
def about():
    return "<h1>About page</h1>"


@page.route("/terms")
def terms():
    return render_template("terms.html")


@page.route("/privacy")
def privacy():
    return render_template("privacy.html")
