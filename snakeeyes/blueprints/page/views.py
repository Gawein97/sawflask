from flask import Blueprint

page = Blueprint("page", __name__, template_folder="templates")


@page.route("/")
@page.route("/home")
def home():
    return "<h1>Home page</h1>"


@page.route("/about")
def about():
    return "<h1>About page</h1>"


@page.route("/terms")
def terms():
    return "<h1>Terms and conditions</h1>"


@page.route("/privacy")
def privacy():
    return "<h1>Privacy page</h1>"
