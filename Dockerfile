FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    npm \
    python3 \
    python3-pip \
    python3.12-venv \
    && rm -rf /var/lib/apt/lists/*

# RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
#     && apt-get install -y nodejs \
#     && node --version \
#     && npm --version
    
RUN python3 -m venv venv
RUN ./venv/bin/pip install flask

# RUN python3 -m pip install flask
# RUN apt install python3-flask
WORKDIR /usr/src/app

RUN apt-get install npm
RUN npm install react-scripts --verbose





CMD ["sh", "-c", "venv/bin/python /usr/src/backend/server.py & npm start"]