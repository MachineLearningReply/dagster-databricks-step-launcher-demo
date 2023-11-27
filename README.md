# 🚀 Dagster Databricks Integration Demo 🚀

This repository contains a demo project showcasing the integration of Dagster with Databricks using the Databricks Step Launcher. The demo demonstrates how to develop PySpark code locally, version it using Git, upload it to Databricks, and execute it there, providing an efficient workflow compared to just scheduling Databricks Jobs via Dagster.

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Databricks Cluster**: You will need an active Databricks cluster. The Cluster ID will be required later to run the PySpark script.
- **Python**: This demo is developed with Python 3.8.6. Ensure you have the same or compatible Python version installed.

## ⚙️ Configuration

To use this demo, you need to specify several configuration parameters:

1. **Databricks Cluster ID**: Find this in your Databricks cluster configurations and update it in the `dagster_demo/__init__.py` file (i.e., replace "<CLUSTER_ID>").
2. **Databricks Host**: This is the URL of your Databricks workspace. Update it in the `dagster_demo/__init__.py` file (i.e., replace "<HOST_HTTPS_PATH>", sample format: "https://abd-123abcde-0a1b.cloud.databricks.com").
3. **Databricks Token**: This is your personal access token for Databricks. Update it in the `dagster_demo/__init__.py` file (i.e., replace "<HOST_TOKEN>").
4. **Databricks Schema**: This is the schema/database where you want to store the sample table for this demo, assuming you store it in the Hive Metastore. Update the schema in the `dagster_demo/pyspark_asset.py` (i.e., replace "<DB_SCHEMA>").

For more detailed instructions on how to find these parameters, refer to the Databricks documentation.

## 🔨 Installation and Setup

Follow these steps to set up and run the demo:

1. **Clone the Repository**:
```bash
git clone <repository-url>
cd dagster_demo
```

2. **Install Dependencies**:
Install the required dependencies for the project:
```bash
pip install -e ".[dev]"
```

3. **Start the Dagster UI**:
Launch the Dagster development environment:
```bash
dagster dev
```

Once the UI is running, access it via http://localhost:3000 in your browser.

## 🏃 Running the Demo

After setting up, you can run the demo pipeline using the Dagster UI. The pipeline will execute the PySpark script on your Databricks cluster.
If everything worked out, you should see the table `raw_full_moon_dates` in Databricks in the specified schema.

## 🤝 Contributing

Contributions to this demo are welcome. Please ensure that your code adheres to the best practices for PySpark development and is compatible with the Databricks environment.

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- Tobias Zeulner - t.zeulner@reply.de
- David Weber - da.weber@reply.de
- Döme Lörinczy - d.loerinczy@reply.de

Machine Learning Reply,
Luise-Ullrich Str 14,
80636 Munich