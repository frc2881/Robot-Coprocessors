FROM python:3.11-slim-bookworm

RUN apt update
RUN apt upgrade -y
RUN apt install -y git build-essential libc-dev swig libpcsclite-dev pcscd

RUN pip install --upgrade pip
RUN pip install python-decouple
RUN pip install --extra-index-url=https://wpilib.jfrog.io/artifactory/api/pypi/wpilib-python-release-2024/simple pyntcore

RUN git clone https://github.com/LudovicRousseau/pyscard.git
WORKDIR /pyscard
RUN python setup.py build_ext install
