import flask
from apps import echo, messages

app = flask.Flask(__name__)
app.register_blueprint(echo)
app.register_blueprint(messages)

if __name__ == '__main__':
    app.run()
