#!/usr/bin/env python

import distutils.core
import io
import sys

# Importing setuptools adds some features like "setup.py test", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

major, minor = sys.version_info[:2]
python_30 = major > 3 or (major == 3 and minor >= 0)
if not python_30:
    raise RuntimeError("Python 3.0 or newer is required")


with io.open("readme.md", mode="r", encoding="utf-8") as readme:
    long_description = readme.read()

    # Various parameters depend on whether we are the lite package or not

pkgname = "byfrost"
pkgs = [
    "byfrost",
    "byfrost.shared",
    "byfrost.shared.config",
    "byfrost.shared.errors",
    "byfrost.shared.types",
    "byfrost.shared.types.dataclass",
    "byfrost.shared.types.typeddict",
    "byfrost.gcs",
]

distutils.core.setup(
    name=pkgname,
    version="0.0.0.0",
    description="Rainbow bridge for shipping your files to any cloud storage service with the same function calls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ifihan Olusheye",
    author_email="victoriaolusheye@gmail.com",
    url="https://github.com/ifihan/bifrost",
    license="MIT License",
    packages=pkgs,
    test_suite="tests",
    platforms="Posix; MacOS X; Windows",
    package_data={"": ["*.pyi", "py.typed"]},
    install_requires=["typing_extensions", "google-cloud-storage", "google-cloud"],
    setup_requires=[
        "pytest-runner",
        "typing_extensions",
        "google-cloud-storage",
        "google-cloud",
    ],
    tests_require=["pytest", "typing_extensions"],
    python_requires=">=3.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Telephony",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords=[
        "bifrost",
        "thor",
        "storage",
        "sdk",
        "python",
        "filecoin",
        "ipfs",
        "web3",
        "pinata",
        "gcs",
        "s3",
        "google",
        "aws",
        "dropbox",
        "google drive",
        "one drive",
        "cloud storage",
        "byfrost",
    ],
)
