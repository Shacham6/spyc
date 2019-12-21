from setuptools import setup, find_packages

setup(
    name="specs",
    author="Ajo",
    version="0.0.1",
    packages=find_packages(
        include=("specs", ),
        exclude=("tests", ),
    ),
    install_requires=[],
)
