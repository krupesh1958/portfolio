"""Environment Connenction File."""
from settings.config import ProductionConfig, StagingConfig
import os


env: str = os.getenv("ENV", "staging")


auto_config = StagingConfig
if env.lower() == "production":
    auto_config = ProductionConfig
