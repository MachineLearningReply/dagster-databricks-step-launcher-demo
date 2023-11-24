import os
from pathlib import Path

from dagster import Definitions
from dagster_databricks import databricks_pyspark_step_launcher

from .pyspark_asset import full_moon_dates_delta_table

# Configuration for PySpark step launcher
PYSPARK_STEP_LAUNCHER_CONFIG = {
    "run_config": {
        "run_name": "test_dagster",
        "cluster": {"existing": "<CLUSTER_ID>"},
        "libraries": [],
    },
    "permissions": {},
    "databricks_host": '<HOST_HTTPS_PATH>',
    "secrets_to_env_variables": [], 
    "staging_prefix": "/dbfs/tmp",
    "wait_for_logs": True,
    "max_completion_wait_time_seconds": 3600,
    "databricks_token": '<HOST_TOKEN>',
    "local_pipeline_package_path": str(Path(__file__).parent.parent)
}

defs = Definitions(
    assets=[full_moon_dates_delta_table],
    resources={
        "databricks_step_launcher": databricks_pyspark_step_launcher.configured(PYSPARK_STEP_LAUNCHER_CONFIG)
    }
)