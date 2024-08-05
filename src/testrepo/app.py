import logging

from quart import Quart, jsonify, make_response
from quart.typing import ResponseTypes

from testrepo import __version__


def load() -> Quart:
    app = Quart(__name__, static_folder=None)
    app.config.from_prefixed_env("TEST")
    app.logger.info("starting web application version %s", __version__)

    @app.route("/")
    async def health() -> ResponseTypes:
        return await make_response(
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
