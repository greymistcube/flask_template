# this is mainly for form testing

import socket, hashlib
import flask
from apps import cred, util

password = flask.Blueprint(
    "password",
    __name__,
)

@password.route("/password/", methods=["GET", "POST"])
def run():
    template_password = "password.html"
    template_messages = "messages.html"
    title = "Password"
    hostname = socket.gethostname()
    try:
        if flask.request.method == "GET":
            message = "Enter Password"
            return flask.render_template(
                template_password,
                depth=1,
                title=title,
                hostname=hostname,
                message=message,
            )
        else:
            password = util.hash(flask.request.form["password"])
            if password == cred.PASSWORD:
                messages = ["Password Confirmed"]
            else:
                messages = ["Password Denied"]
            return flask.render_template(
                template_messages,
                title=title,
                hostname=hostname,
                messages=messages,
            )
    except:
        message = "bad request"
        return flask.make_response(
            flask.jsonify(message),
            400,
        )
