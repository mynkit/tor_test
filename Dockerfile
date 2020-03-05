FROM joyzoursky/python-chromedriver:3.6

WORKDIR /src

RUN pip install -U pip && \
    pip install -U requests[socks] beautifulsoup4 selenium lxml autopep8 && \
    apt-get install vim curl git tor -y
