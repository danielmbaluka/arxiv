FROM node:14

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

COPY . ./

RUN echo n | npm install

RUN echo n | npm install -g @angular/cli

RUN echo n | npm update

EXPOSE 4200
