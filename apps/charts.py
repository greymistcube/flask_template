import socket
import flask
from apps import nav

charts = flask.Blueprint(
    "charts",
    __name__,
)

class Chart:
    def __init__(self, label, name, data, options, line_smooth):
        self.label = label
        self.container = "#" + self.label
        self.name = name
        self.data = data
        self.options = options
        self.line_smooth = line_smooth
        return

@charts.route("/charts/", methods=["GET"])
def run():
    template = "charts.html"
    title = "Sample Charts"
    hostname = socket.gethostname()

    # generate charts
    labels = ["chart_one", "chart_two", "chart_three"]
    names = ["chart one", "chart two", "chart three"]
    data = {
        "labels": [1, 2, 3, 4, 5],
        "series": [[1, 5, 1, 5, 1]],
    }
    options = {
        "fullWidth": True,
        "axisY": {
            "onlyInteger": True,
        },
    }
    line_smooths = ["none", "step", "simple"]

    charts = [
        Chart(
            label=label,
            name=name,
            data=data,
            options=options,
            line_smooth=line_smooth,
        ) for label, name, line_smooth in zip(labels, names, line_smooths)
    ]

    return flask.render_template(
        template,
        title=title,
        hostname=hostname,
        nav=nav.NAV,
        charts=charts,
    )
