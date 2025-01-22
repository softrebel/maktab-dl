from setuptools import setup, find_packages

setup(
    name="maktab-dl",
    version="0.3.0",
    description="A simple downloader videos from maktabkhooneh",
    author="Mohammadreza Shaghouzi",
    author_email="sh.mohammad66@gmail.com.com",
    packages=find_packages(),
    install_requires=[
        "httpx",
        "pydantic",
        "lxml",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "maktab-dl=maktab_dl.cli:main",
        ],
    },
)
