import logging

from flask import Flask, jsonify, make_response
from flask.wrappers import Response

from testrepo import __version__


def load() -> Flask:
    app = Flask(__name__, static_folder=None)
    app.config.from_prefixed_env("TEST")
    app.logger.info("starting web application version %s", __version__)

    @app.route("/")
    def health() -> Response:
        return make_response(
            jsonify({
                "status": "pass",
                "message": "flux capacitor is fluxing",
                "version": __version__,
            }), 200)

    # tell ourselves what we've mapped
    if app.logger.isEnabledFor(logging.DEBUG):
        for url in app.url_map.iter_rules():
            app.logger.debug(repr(url))

    return app
