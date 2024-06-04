"""This script contains all endpoints with logics."""
import os
import requests

from dotenv import load_dotenv
from flask import (
    Blueprint,
    render_template,
)
from logger import logging

from apps import contact as con

# Configuration Settings
basedir = os.path.abspath(path=os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))


# Blueprint configuration
bp = Blueprint(
    name="portfolio_bp",
    import_name="apps/views.py",
    template_folder="apps/templates",
    static_folder="apps/static"
)


@bp.route("/", methods=["GET"])
def landing_page():
    """For landing page directly redirect this page."""
    return render_template("index.html")


@bp.route("/projects", methods=["GET"])
def projects():
    """This function load all project from the Github and load lineary on
    frontend page."""
    github_url: str = "https://api.github.com/users/krupeshgithub/repos?per_page=100&page=1"

    # Fetch all repository from the github
    headers = {"Authorization": "token " + os.getenv("GOTOKEN", "")}
    resp = requests.get(github_url, headers=headers)

    return render_template(
        template_name_or_list="projects.html",
        projects=resp.json()
    )


@bp.route("/contact", methods=["GET"])
def contact():
    """This function load the contact from the database."""
    resp = con.find_one()
    resp.pop("_id")

    return render_template(
        template_name_or_list="contact.html",
        user=resp
    )
