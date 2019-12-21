from setuptools import setup, find_packages

DESCRIPTION = """
Python Specification and validation library.
"""

setup(
    name="spec",
    author="Pajo",
    version="0.0.1",
    description=DESCRIPTION,
    packages=find_packages(
        include=("specs", ),
        exclude=("tests", ),
    ),
    install_requires=[],
)
