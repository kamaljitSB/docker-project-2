FROM node:latest

WORKDIR /app

COPY . .

RUN npm install

RUN npm install mysql2

# USER root

# RUN echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf && sysctl -p
RUN echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf
CMD ["npm", "start"]
