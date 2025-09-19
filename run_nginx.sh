# docker run -it --rm -p 8080:80 --name web --mount type=bind,src=./mi-content,dst=/usr/share/nginx/html nginx
docker run -it --rm -d -p 80:80 -p 443:443 --name web mi_nginx 
