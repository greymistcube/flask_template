import socket
import flask

charts = flask.Blueprint(
    "charts",
    __name__,
)

class Chart:
    def __init__(
        self,
        label: str,
        name: str,
        data: dict,
        options: dict,
        line_smooth: str,
    ):
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
    xs = [1, 2, 3, 4, 5]
    ys = [1, 5, 1, 5, 1]
    data = {
        "series": [
            {
                "data": [
                    {"x": x, "y": y} for x, y in zip(xs, ys)
                ],
            },
        ],
    }
    options = {
        "axisX": {
            "low": 1,
            "high": 5,
            "ticks": [1, 2, 3, 4, 5],
            "labels": ["a", "b", "c", "d", "e"],
        },
        "axisY": {
            "low": 1,
            "high": 5,
            "ticks": [1, 2, 3, 4, 5],
            "labels": [1, 2, 3, 3, 5],
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
        depth=1,
        title=title,
        hostname=hostname,
        charts=charts,
    )
