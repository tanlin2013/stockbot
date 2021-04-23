FROM python:3.7
MAINTAINER "TaoLin" <tanlin2013@gmail.com>

# Environment Settings
ARG WORKDIR=/home
ENV PYTHONPATH "${PYTHONPATH}:$WORKDIR"
WORKDIR $WORKDIR

# Install TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz &&\
    tar -xzf ta-lib-0.4.0-src.tar.gz &&\
    cd ta-lib/ &&\
    ./configure --prefix=/usr &&\
    make &&\
    sudo make install

# Install Python Dependencies
COPY . $WORKDIR
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

# Install Stockbot
#RUN python setup.py install

ENTRYPOINT /bin/bash