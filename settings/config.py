"""Application Environment Base Configuration File."""
import os
from dotenv import load_dotenv

# Configuration Settings
basedir = os.path.abspath(path=os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "../.env"))


class ProductionConfig:
    """This file contains production configurations."""
    connection_str: str = os.getenv("PROD_MONGO")
    database_name: str = os.getenv("PROD_DATABASE_NAME")
    rate_limit: bool = True
    port: int = 7861


class StagingConfig:
    """This file contains staging configurations."""
    connection_str: str = os.getenv("STAGING_MONGO")
    database_name: str = os.getenv("STAGING_DATABASE_NAME")
    rate_limit: bool = False
    port: int = 6187
