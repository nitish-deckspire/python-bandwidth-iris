from setuptools import setup, find_packages

setup(
    name             = "iris_sdk",
    version          = "0.1",
    description      = "IRIS / BBS Python API",
    author           = "Bandwidth",
    maintainer       = "Bandwidth",
    url              = "https://github.com/scottbarstow/iris-python",
    license          = "MIT",
    # packages         = ["iris_sdk"],
    packages         = find_packages(),
    include_package_data = True,
    long_description = "Python client library for IRIS / BBS API",
    classifiers = [
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    install_requires=[
        "future",
        "requests",
    ]
)