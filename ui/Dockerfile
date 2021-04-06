FROM node:14

RUN npm install -g @angular/cli

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN npm install

EXPOSE 4200
