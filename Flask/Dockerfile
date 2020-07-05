# docker build -t flask . 
FROM ubuntu:18.04 

RUN apt-get update\
    && apt-get install python3-dev python3-flask -y\
    && apt install python3-pip -y\
    && pip3 install -U Flask jsonify request

ENV FLASK_APP=web_app
ENV FLASK_ENV=development 
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app 

EXPOSE 80

CMD flask run -p 80 --host 0.0.0.0

# docker run -it -p 80:80 -v {PATH_TO_PROJECT}:/app flask  
