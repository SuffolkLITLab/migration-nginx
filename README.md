# Migration Nginx Dockerfile and Contents

A quick-n-dirty way to bring up a temporary maintenance page when migrating or turning down docassemble servers.

## Example usage

```bash
# clone the repo
git clone https://github.com/SuffolkLitLab/migration-nginx

# Build the image for the org you want (assumes a running docassemble container)
./build-nginx.sh mi

# Stop the running docassemble container 
docker stop -t 600 da_container

./run-nginx.sh mi
```
