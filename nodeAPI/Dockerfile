FROM node:9

RUN mkdir /root/api
WORKDIR /root/api

COPY package.json ./
RUN npm install
COPY ./ ./

#EXPOSE 3000

ENV PORT=5555

CMD ["node", "app.js"]
