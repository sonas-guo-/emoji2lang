#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "emoji2lang",
    version = "0.0.2",
    keywords = ("pip", "emoji", "human language", "convert"),
    description = "convert emoji to human language",
    long_description = "convert emoji to human language",
    license = "MIT Licence",

    url = "https://github.com/sonas-guo-/emoji2lang",
    author = "sonas",
    author_email = "guolinsen123@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [],
    package_data = {
        "emoji2lang" : ["emoji2lang/data"]
    }
)
