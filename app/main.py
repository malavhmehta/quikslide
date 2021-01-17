from flask import Flask, render_template, send_from_directory, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_required

from app.models.user import User
from app.models.project import Project
from app.db import db
from app.process.process import Process
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(os.path.join(project_dir, "dev.db"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = '60082fe3ed9f865221cd3696'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app.views import login


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        script = request.form["script"]
        title = request.form.get("title")

        if title.strip() == "":
            title = None

        slides = Process(script)
        slides.process(current_user.email, current_user.username, title)
        
        new_project = Project(owner=current_user.id, name=slides.name, link=slides.link)
        db.session.add(new_project)
        db.session.commit()

        return render_template("create.html", link=slides.link)
        
    return render_template("create.html")

@app.route("/dashboard")
@login_required
def dashboard():
    projects = Project.query.filter_by(owner=current_user.id).all()
    return render_template("dashboard.html", projects=projects)
