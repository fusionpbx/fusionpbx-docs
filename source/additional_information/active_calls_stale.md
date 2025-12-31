## Active Calls - Remove Stale Calls
---

Sometimes FreeSWITCH will not remove all active calls and you may see old calls that still show in Active Calls. These calls are no longer running but are still in the FreeSWITCH database so they show up under the Active Calls feature. The following scripts show how to remove these stale calls.

FreeSWITCH uses SQLite by default. So, in most cases, people should use the instructions for SQLite. SQLite on Debian and Ubuntu use the ``/var/lib/freeswitch/db`` directory. FreeSWITCH also can be set up to use a different directory like ``/dev/shm``. If this is the case, the path to the SQLite database would need to be updated. However, if someone has manually set up FreeSWITCH to use PostgreSQL, then you would need to follow the PostgreSQL instructions below.

### SQLite or PostgreSQL

You need to use the section that matches your system's database. FreeSWITCH uses SQLite by default, but if FreeSWITCH was configured to use PostgreSQL you would likely see DSN values defined in Advanced -> Variables.

The following command can be used to view the dates on the SQLite database files...
```
ls -lh /var/lib/freeswitch/db
```
or
```
ls -lh /dev/shm
```
If the dates on the returned files are more recent, then FreeSWITCH is likely set up to use SQLite and not PostgreSQL.

### Create the Script

Run the following commands...
```
cd /usr/src
touch freeswitch-channels.sh
chmod 750 /usr/src/freeswitch-channels.sh
nano /usr/src/freeswitch-channels.sh
```

### SQLite

By default, SQLite is the script you should use.

```
apt install sqlite3
```

Add this to the freeswitch-channels.sh file.
```
#!/bin/sh

#default location
sqlite3 /var/lib/freeswitch/db/core.db "delete from channels where strftime('%s','now') - created_epoch > 14400;"

#ram drive
#sqlite3 /dev/shm/core.db "delete from channels where strftime('%s','now') - created_epoch > 14400;"
```

### PostgreSQL

If FreeSWITCH was setup to manually use PostgreSQL then you would use these instructions from this PostgreSQL section.

Get the fusionpbx database password

FusionPBX 5.0.5 and higher.
```
cat /etc/fusionpbx/config.conf | grep password
```
or
FusionPBX 5.0.4 and lower.
```
cat /etc/fusionpbx/config.php | grep password
```

(replace PGPASSWORD="zzzzzzzz" specifically the zzzzzzzz with the fusionpbx database password from the previous step)
```
#!/bin/sh

now=$(date +%Y-%m-%d)
db_host=127.0.0.1
db_port=5432
export PGPASSWORD="zzzzzzzz"

psql --dbname=freeswitch --host=$db_host --port=$db_port --username=fusionpbx -c "DELETE FROM channels WHERE to_timestamp(created_epoch)::timestamptz < NOW() - INTERVAL '4 hours';"
```

### Cron job

```
crontab -e
```

Run the cron job every 30 minutes or adjust as needed. This should remove calls older than 4 hours with the cronjob running every 30 minutes.
```
*/30 * * * * /usr/src/./freeswitch-channels.sh
```

Or run this at some time at night. This example runs at 2:00 am.

```
0 2 * * * /usr/src/./freeswitch-channels.sh
```
