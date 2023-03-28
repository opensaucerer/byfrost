#!/usr/bin/env python3
import pathlib
from setuptools import setup, find_packages

setup(
    name="bifrost",
    version="0.0.1",
    license="GNU GENERAL PUBLIC LICENSE",
    description="Rainbow bridge for shipping your files to any cloud storage service with the same function calls.",
    author="Ifihan Olusheye <victoriaolusheye@gmail.com>, Perfection Loveday <wizard@opensaucerer.com>",
    # author_email="victoriaolusheye@gmail.com",
    url="https://github.com/ifihan/bifrost",
    packages=find_packages("pkg"),
    package_dir={"": "pkg"},
    install_requires=["requests"],
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
    ],
    long_description=(
        (pathlib.Path(__file__).parent.resolve()) / "readme.md"
    ).read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
)
