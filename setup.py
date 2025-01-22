from setuptools import setup, find_packages

setup(
    name="maktab-dl",
    version="0.1.0",
    description="A simple command line tool to download videos",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.28.1",
        "pydantic>=2.10.5",
        "lxml>=5.3.0",
        "click>=8.1.8",
        "tqdm>=4.67.1",
    ],
    entry_points={
        "console_scripts": [
            "maktab-dl=maktab_dl.cli:cli",
        ],
    },
)
