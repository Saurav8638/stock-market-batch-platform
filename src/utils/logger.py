import logging
import logging.config
from pathlib import Path
import yaml


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.
    """

    config_path = Path("configs/logging.yaml")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    logging.config.dictConfig(config)

    return logging.getLogger(name)