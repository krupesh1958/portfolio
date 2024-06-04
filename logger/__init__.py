"""This module contains loggin information of all users."""
import logging
import logging.config


logging.config.fileConfig(
    "logger/logging.ini",
    defaults={
        "logfilename": "/var/log/porfolio.log"
    },
    disable_existing_loggers=True,
    encoding=None
)
