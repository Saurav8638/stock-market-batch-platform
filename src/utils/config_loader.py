from pathlib import Path
import yaml
from dotenv import load_dotenv


class ConfigLoader:
    """
    Loads application configuration from YAML
    and environment variables from .env.
    """

    def __init__(self):
        load_dotenv()

        config_path = Path("configs/config.yaml")

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self):
        return self.config