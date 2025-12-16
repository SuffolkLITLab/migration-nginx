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

## Database moving

Moving postgres databases from the files inside of the docassemble container to one that's external is fairly difficult. This repo also
includes a `split-pg-dump.py` file that will turn a `*.sql` dump from postgres into multiple files that can be uploaded to the new database
one by one, and aren't too big, running into a `SSL error: sslv3 alert bad record mac`.

Instructions are as follows:

```bash
python3 split-pg-dump.py prod-database.sql tmp_prod
find . -name "*.sql" | sort | xargs -I{} psql -h ... -p 5432 -d postgres -U postgres -f {}
```

TODO: add some extra sleeps and status prints to the last command.
