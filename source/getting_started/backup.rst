*****************
Backup
*****************

|

It's always good to have a backup method in place.  Here are the steps to a basic backup method with FusionPBX. The install script on Debian will automatically copy this backup script to /etc/cron.daily/fusionpbx-backup. Backups get stored in /var/backups/fusionpbx/postgresql by default.

Command Line
^^^^^^^^^^^^^^

Be sure to change the password by replacing the zzzzzzzz in PGPASSWORD="zzzzzzzz" with your database password. You can get the password from /etc/fusionpbx/config.php.


::

 cd /etc/cron.daily
 nano fusionpbx-backup


 #!/bin/sh
 
 export PGPASSWORD="zzz"
 db_host=127.0.0.1
 db_port=5432
 
 now=$(date +%Y-%m-%d)
 mkdir -p /var/backups/fusionpbx/postgresql
 
 echo "Backup Started"
 
 #delete postgres backups
 find /var/backups/fusionpbx/postgresql/fusionpbx_pgsql* -mtime +4 -exec rm {} \;
 
 #delete the main backup
 find /var/backups/fusionpbx/*.tgz -mtime +2 -exec rm {} \;
 
 #backup the database
 pg_dump --verbose -Fc --host=$db_host --port=$db_port -U fusionpbx fusionpbx --schema=public -f /var/backups/fusionpbx/postgresql/fusionpbx_pgsql_$now.sql
 
 #package
 #tar --exclude='/var/lib/freeswitch/recordings/*/archive' -zvcf /var/backups/fusionpbx/backup_$now.tgz /var/backups/fusionpbx/postgresql/fusionpbx_pgsql_$now.sql /var/www/fusionpbx /usr/share/freeswitch/scripts /var/lib/freeswitch/storage /var/lib/freeswitch/recordings /etc/fusionpbx /etc/freeswitch /usr/share/freeswitch/sounds/music/

 #source
 #tar -zvcf /var/backups/fusionpbx/backup_$now.tgz /var/backups/fusionpbx/postgresql/fusionpbx_pgsql_$now.sql /var/www/fusionpbx /usr/local/freeswitch/scripts /usr/local/freeswitch/storage /usr/local/freeswitch/recordings /etc/fusionpbx /usr/local/freeswitch/conf /usr/local/freeswitch/sounds/music/
 
 echo "Backup Completed"


To save the file press ctrl + x then y to save it.


You should have the script ready to execute. (Default the script will use FreeSWITCH package paths.  If you have an older install using source be sure to change this by commenting the package line #22 and uncomment the source line #25.)
 
Crontab (optional)
^^^^^^^^^^^^^^^^^

Files in /etc/cron.daily will execute automatically if they don't have an extension like .sh for this reason the backup script was renamed from fusionpbx-backup.sh to fusionpbx-backup and then it runs nightly without needing to use crontab.

Setting crontab -e
 
::

 crontab -e
 Choose 1 for nano
 Goto the last blank line and paste in the next line.
 0 0 * * * /bin/sh /etc/cron.daily/fusionpbx-backup.sh
 press enter then save and exit.
 

Once this is complete you will have the backup ready to execute by ./fusionpbx-backup or from the daily cron job. 

