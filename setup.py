# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="pynasne",
    packages=['pynasne'],
    version="0.1.0",
    description="Python wrapper for Nasne's REST API.",
    author="irotoris",
    author_email="shiroto00@yahoo.co.jp",
    url="https://github.com/irotoris/pynasne",
    install_requires=['requests'],
    keywords=["nasne", "REST API"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
