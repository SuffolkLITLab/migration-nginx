test -z "$1" && echo "Pass in the org you want" && exit

# Get the existing certs off the docassemble container
docker_name=$(docker ps --format '{{.Name}}')
docker exec $docker_name /usr/bin/tar -zcf /tmp/letsencrypt.tar.gz etc/letsencrypt
docker cp $docker_name:tmp/letsencrypt.tar.gz .

docker build -t $1-nginx --build-arg ORG_DIR=$1-content .


