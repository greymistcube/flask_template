import socket
import flask
from apps import nav

messages = flask.Blueprint(
    "messages",
    __name__,
)

@messages.route("/messages/", methods=["GET"])
def run():
    template = "messages.html"
    title = "Sample Messages"
    hostname = socket.gethostname()
    messages = [
        "message one",
        "message two",
        "message three",
    ]
    return flask.render_template(
        template,
        title=title,
        hostname=hostname,
        nav=nav.NAV,
        messages=messages,
    )
