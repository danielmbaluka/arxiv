FROM node:14

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY package.json package-lock.json ./

RUN echo n | npm install

RUN echo n | npm install -g @angular/cli

RUN npm update

EXPOSE 4200

CMD ["ng", "serve"]
