import os
import sys

from pyspark.sql import SparkSession

from src.utils.config_loader import ConfigLoader


def get_spark_session() -> SparkSession:
    """
    Create and return a configured SparkSession.
    """

    # Force Spark to use the current virtual environment's Python
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    config = ConfigLoader().get()

    spark = (
        SparkSession.builder
        .appName(config["spark"]["app_name"])
        .master(config["spark"]["master"])
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark