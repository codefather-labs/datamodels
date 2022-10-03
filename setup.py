from setuptools import setup

from datamodels import __author__

setup(
    name="datamodels",
    version="0.1",
    packages=["datamodels"],
    maintainer=__author__,
)

from test import *
