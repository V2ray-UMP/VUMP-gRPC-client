from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
NAME = 'VUMP-gRPC-client'
DESCRIPTION = " a python gRPC client for V2Ray/V2Fly gRPC API"
URL = 'https://github.com/V2ray-UMP/VUMP-gRPC-client'
EMAIL = 'a@b.c'
AUTHOR = 'V2ray-UMP'
REQUIRES_PYTHON = '>=3.9.0'
VERSION = '1.0.2'
LICENSE = 'MIT License (MIT)'
try:
    with open(path.join(here, "requirements.txt"), encoding="utf-8") as r:
        REQUIRED = [i.strip() for i in r]
except FileNotFoundError:
    REQUIRED = ['grpcio==1.50', 'grpcio-tools==1.50']
try:
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        README = f.read()
except FileNotFoundError:
    README = 'https://github.com/V2ray-UMP/VUMP-gRPC-client/blob/master/README.md'
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    project_urls={
        "API Docs Reference": "https://www.v2fly.org/config/api.html#apiobject",
        "Discussions": "https://github.com/V2ray-UMP/VUMP-gRPC-client/discussions",
        "Issues": "https://github.com/V2ray-UMP/VUMP-gRPC-client/issues",
    },
    keywords='v2ray grpc python client',
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    packages=find_packages(include=['vump_grpc_client*']),
    classifiers=[
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
    ],
    zip_safe=False
)
