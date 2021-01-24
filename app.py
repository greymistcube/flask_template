import flask
from apps import echo, messages, status, charts

app = flask.Flask(__name__)
app.register_blueprint(echo)
app.register_blueprint(messages)
app.register_blueprint(status)
app.register_blueprint(charts)

if __name__ == '__main__':
    app.run()
