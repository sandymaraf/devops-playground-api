# setup.py na raiz
from setuptools import setup, find_packages

setup(
    name="devops_playground_api",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.128.0",
        "uvicorn==0.40.0",
        "pytest==9.0.2",
        "pytest-cov==4.1.0",
        "httpx==0.28.1",
        "pydantic==2.12.5",
    ],
)