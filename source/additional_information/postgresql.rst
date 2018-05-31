############
PostgreSQL
############


PostgreSQL is a enterprise grade open source database.
http://www.postgresql.org/

Backup
------

The following assumes the database username is fusionpbx and the
database to backup is fusionpbx. Make sure you have the database
password ready.

| ``su postgres``
| ``pg_dump -U fusionpbx fusionpbx -b -v -f /tmp/fusionpbx.sql``

Restore
-------

Assuming username fusionpbx and database fusionpbx

``psql -U fusionpbx -d fusionpbx -f fusionpbx.sql``

Console
-------

| ``su postgres``
| ``psql``

list the databases

``\l``

connect to the database

``\connect fusionpbx``

or

``\c fusionpbx``

list tables

``\d``

drop the database

``DROP DATABASE fusionpbx;``

create the database

``CREATE DATABASE fusionpbx;``

Links
-----

http://www.mkyong.com/database/backup-restore-database-in-postgresql-pg_dumppg_restore/

http://www.postgresql.org/docs/9.1/static/backup.html
