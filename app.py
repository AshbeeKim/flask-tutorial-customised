from logging.config import valid_ident
from flask import (
    Flask, 
    abort,
    url_for, 
    request, 
    redirect, 
    session,
    render_template, 
)
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

################################################## home
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects/")
def projects():
    pass

################################################## login
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    valid_login, log_the_user_in은 따로 작성해야 함.
    """
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"],
                        request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    return render_template("login.html", error=error)

################################################## upload

################################################## search
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    
    if request.method == "POST":
        """
        search할 때 필요한 값들
        """
        return render_template("result.html")


################################################## error
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

