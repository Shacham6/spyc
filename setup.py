from setuptools import setup, find_packages

setup(
    name="spec",
    author="Ajo",
    version="0.0.1",
    packages=find_packages(
        include=("spec", ),
        exclude=("tests", ),
    ),
    install_requires=[],
)
