import socket
import flask

status = flask.Blueprint(
    "status",
    __name__,
)

@status.route("/status/", methods=["GET"])
def run():
    template = "messages.html"
    title = "Server Status"
    hostname = socket.gethostname()
    messages = [f"{hostname} is up and running"]
    return flask.render_template(
        template,
        title=title,
        hostname=hostname,
        messages=messages,
    )
