import json
import flask

echo = flask.Blueprint(
    "echo",
    __name__,
)

@echo.route("/echo/", methods=["POST"])
def run():
    try:
        data = json.loads(flask.request.data)
        return flask.make_response(
            flask.jsonify(data),
            200,
        )
    except:
        message = "bad request"
        return flask.make_response(
            flask.jsonify(message),
            400,
        )
