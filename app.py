import flask
from apps import echo, messages, status, charts, password, links, navigation

app = flask.Flask(__name__)
app.register_blueprint(echo)
app.register_blueprint(messages)
app.register_blueprint(status)
app.register_blueprint(charts)
app.register_blueprint(password)
app.register_blueprint(links)
app.register_blueprint(navigation)

if __name__ == '__main__':
    app.run()
