from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name="document_assembler",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    description="A set of tools to convert a markup document into something more readable.",
    author="Daniel Abrajan C.",
    author_email="seorc.d@gmail.com",
    install_requires=[
        'Jinja2>=2.7.3',
        'Markdown>=2.4.1',
        'PyYAML>=3.11'
    ],
)
