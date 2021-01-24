import flask
from apps import echo, messages, status

app = flask.Flask(__name__)
app.register_blueprint(echo)
app.register_blueprint(messages)
app.register_blueprint(status)

if __name__ == '__main__':
    app.run()
