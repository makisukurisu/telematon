import datetime
import logging

from flask import Flask

from .views import CreateContactView

logging.basicConfig(
    filename=f"{datetime.datetime.utcnow()}.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)

app = Flask(__name__)

app.add_url_rule(
    "/create_contact/",
    view_func=CreateContactView.as_view("create_contact"),
    methods=["POST"],
)
