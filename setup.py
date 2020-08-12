from setuptools import setup

setup(
    name ="library1",
    version="0.0.1",
    description="it is just library for fun",
    author="ayan",
    author_email="ayan@gmail.com",
    url="https://github.com/mazh661/python_lib",
    license="MIT",
    packages=["library1","library2","kafka_lib"],
    install_requires=[
        "numpy==1.19.1",
        "kafka==1.3.5"
    ]
)