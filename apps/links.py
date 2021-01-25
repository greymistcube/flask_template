import socket
import flask
from apps import sitemap

links = flask.Blueprint(
    "links",
    __name__,
)

@links.route("/links/", methods=["GET"])
def run():
    template = "links.html"
    title = "Sample Links"
    hostname = socket.gethostname()
    links = sitemap.SITEMAP
    return flask.render_template(
        template,
        depth=1,
        title=title,
        hostname=hostname,
        links=links,
    )
