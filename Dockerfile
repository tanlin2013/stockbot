FROM python:3.7
MAINTAINER "TaoLin" <tanlin2013@gmail.com>

ARG WORKDIR=/home
ENV PYTHONPATH "${PYTHONPATH}:$WORKDIR"
WORKDIR $WORKDIR

# Install required python packages
COPY . $WORKDIR
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install stockbot
#RUN python setup.py install

ENTRYPOINT /bin/bash