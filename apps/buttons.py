import socket
import flask

buttons = flask.Blueprint(
    "buttons",
    __name__,
)

BUTTONS = {
    "button_one": "button one",
    "button_two": "button two",
    "button_three": "button three",
}

@buttons.route("/buttons/submit/", methods=["POST"])
def submit():
    template = "messages.html"
    depth = 2
    title = "Button Submit"
    hostname = socket.gethostname()

    for key in BUTTONS:
        if key in flask.request.form:
            button = BUTTONS[key]
            break

    messages = [f"button pressed: {button}"]
    return flask.render_template(
        template,
        depth=depth,
        title=title,
        hostname=hostname,
        messages=messages,
    )

@buttons.route("/buttons/", methods=["GET"])
def run():
    template = "buttons.html"
    depth = 1
    title = "Sample Buttons"
    hostname = socket.gethostname()
    return flask.render_template(
        template,
        depth=depth,
        title=title,
        hostname=hostname,
        buttons=BUTTONS,
    )
    return
