FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    git \
    vim \
    # npm \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && node --version \
    && npm --version
    
# RUN npm install react-scripts --save --verbose

WORKDIR /usr/src/app

CMD ["sh", "-c", "npm install && npm start"]