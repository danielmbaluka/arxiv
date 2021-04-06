FROM node:14

RUN npm install -g @angular/cli

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN npm install

RUN ng update

RUN npm update

EXPOSE 4200
