FROM nginx:latest

ARG ORG_DIR=suffolk-content

COPY ./$ORG_DIR/index.html /usr/share/nginx/html/index.html
COPY ./$ORG_DIR/default.conf /etc/nginx/conf.d/default.conf

# Unpacks to /etc/letsencrypt
ADD ./letsencrypt.tar.gz /
