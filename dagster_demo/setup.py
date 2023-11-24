from setuptools import find_packages, setup

setup(
    name="dagster_demo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster==1.5.5",
        "dagster-cloud==1.5.5",
        "dagster-databricks==0.21.5",
    ],
    extras_require={
        "dev": [
            "dagster-webserver==1.5.5",
        ]
    },
)