import socket
import flask

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
        depth=1,
        title=title,
        hostname=hostname,
        messages=messages,
    )
