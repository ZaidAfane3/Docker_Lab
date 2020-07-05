# docker build -t nuxt . 

FROM node:latest 

RUN mkdir -p /usr/src/nuxt-app 
WORKDIR /usr/src/nuxt-app

RUN yarn global add git 

# Change {Project_01/nuxt/app1} to your Project file containing package.json
COPY Project_01/nuxt/app1 . 

RUN npm install 
RUN npm run build 

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000 

CMD npm start

# docker run -it -p 3000:3000 nuxt 