#!/usr/bin/env python3
"""Inialitation project to run this module."""
from __future__ import annotations

from typing import Dict
from flask import Flask
from flask_cors import CORS

from middleware.fix_window import FixWindowRateLimit as RateLimit
from settings import auto_config as cfg
from apps.views import bp as blueprint

JsonType = Dict[str, int]

app = Flask(__name__)

if cfg.rate_limit:
    app.wsgi_app = RateLimit(app.wsgi_app)

CORS(app)


# Register blueprint
app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=cfg.port, debug=True)
