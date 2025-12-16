import os
import sys
import re


header = """
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;
"""


def mkdir_and_split_tables(in_file, out_dir):
  os.mkdir(out_dir)
  idx = 0
  current_file = open(f'{out_dir}/db_dump_{idx:02}.sql', 'w')
  reg = re.compile('^-- Data for Name: ([^;]+);')
  with open(in_file, 'r') as f:
    for line in f:
      found = reg.search(line)
      if found:
         current_file.close()
         idx += 1
         print(f'On to the next file: {idx}')
         current_file = open(f'{out_dir}/db_dump_{idx:02}.sql', 'w')
         current_file.write(header)
      current_file.write(line)

def split_large_tables(out_dir):
  for out_file in os.listdir(out_dir):
    the_size = os.stat(f'{out_dir}/{out_file}').st_size
    print(f'{out_file}: {the_size}')
    if the_size > 1000000:
        idx = 0
        new_file = open(f'{out_dir}/{out_file[0:-4]}_{idx:03}.sql', 'w')
        new_file.write(header)
        existing_file = open(f'{out_dir}/{out_file}', 'r')
        the_copy = 'PLACEHOLDER COPY\n'
        line_num = 0
        for line in existing_file:
            line_num += 1
            if line.startswith('COPY '):
                the_copy = line
            new_file.write(line)
            if line_num > 5000:
                line_num = 0
                new_file.write('\\.\n')
                new_file.close()
                idx += 1
                new_file = open(f'{out_dir}/{out_file[0:-4]}_{idx:03}.sql', 'w')
                new_file.write(header)
                new_file.write(the_copy)
        existing_file.close()
        os.remove(f'{out_dir}/{out_file}')

def main(argv):
  in_file = argv[1]
  out_dir = argv[2]
  mkdir_and_split_tables(in_file, out_dir)
  split_large_tables(out_dir)

if __name__ == '__main__':
  main(sys.argv)
