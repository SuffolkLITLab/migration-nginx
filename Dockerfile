FROM nginx:latest

ARG ORG_DIR

RUN test -n  "$ORG_DIR"

COPY ./$ORG_DIR/index.html /usr/share/nginx/html/index.html
COPY ./$ORG_DIR/default.conf /etc/nginx/conf.d/default.conf

# Unpacks to /etc/letsencrypt
ADD ./letsencrypt.tar.gz /
