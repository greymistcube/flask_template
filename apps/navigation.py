import socket
import flask
from apps import sitemap

navigation = flask.Blueprint(
    "navigation",
    __name__,
)

@navigation.route("/navigation/", methods=["GET"])
def run():
    template = "links.html"
    title = "Navigation"
    hostname = socket.gethostname()
    links = sitemap.SITEMAP
    return flask.render_template(
        template,
        depth=1,
        title=title,
        hostname=hostname,
        links=links,
    )
