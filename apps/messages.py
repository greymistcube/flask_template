import socket
import flask

messages = flask.Blueprint(
    "messages",
    __name__,
)

@messages.route("/messages/", methods=["GET"])
def run():
    template = "messages.html"
    title = "Messages"
    hostname = socket.gethostname().upper()
    messages = [
        "message one",
        "message two",
        "message three",
    ]
    return flask.render_template(
        template,
        title=title,
        hostname=hostname,
        messages=messages,
    )
