"""Initialize the mongodb collection."""
import os

import logging
from pymongo import MongoClient, errors

from settings import auto_config as cfg
from logger import logging


connection_string = cfg.connection_str

# Connection
try:
    mongo_chat = MongoClient(host=connection_string)
except errors.ConnectionFailure as error:
    logging.error(error)

database_name: str = cfg.database_name
database = mongo_chat[database_name]

# Fetch collection
contact = database["contact"]
