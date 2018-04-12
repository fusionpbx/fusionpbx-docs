*****************
Backup
*****************

|

It's always good to have a backup method in place.  Here are the steps to a basic backup method with FusionPBX.

Command Line
^^^^^^^^^^^^^^

Be sure to change the password by replacing the zzzzzzzz in PGPASSWORD="zzzzzzzz" with your database password. You can get the password from /etc/fusionpbx/config.php.


::
 
 
 cd /etc/cron.daily
 nano fusionpbx-backup.sh
 
 #!/bin/sh
 now=$(date +%Y-%m-%d)
 echo "Server Backup"
 export PGPASSWORD="zzzzzzzz"
 mkdir -p /var/backups/fusionpbx/postgresql
 #delete postgres logs older than 7 days
 find /var/log/postgresql/postgresql-9.4-main* -mtime +7 -exec rm {} \;
 #delete freeswitch logs older 3 days
 find /usr/local/freeswitch/log/freeswitch.log.* -mtime +2 -exec rm {} \;
 pg_dump --verbose -Fc --host=$database_host --port=$database_port -U fusionpbx fusionpbx --schema=public -f /var/backups/fusionpbx/postgresql/fusionpbx_pgsql_$now.sql
 echo "Backup Complete";
 
To save the file press ctrl + x then y to save it.


You should have the script ready to execute. (Default the script will use FreeSWITCH package paths.  If you have an older install using source be sure to change this by commenting the package line #22 and uncomment the source line #25.)
 
Crontab
^^^^^^^^^^^^^^^^^

Setting crontab -e
 
::

 crontab -e
 Choose 1 for nano
 Goto the last blank line and paste in the next line.
 0 0 * * * /bin/sh /etc/cron.daily/fusionpbx-backup.sh
 press enter then save and exit.
 


Once this is complete you will have the backup ready to execute by ./fusionpbx-backup.sh or from the daily cron job. 

Web Interface (optional)
^^^^^^^^^^^^^^^^^^^^^^^^

**FreeSWITCH Package install paths.**

.. image:: ../_static/images/fusionpbx_backup_source1.jpg
        :scale: 85%

**Goto Advanced > Default Settings.**

::

 Settings for FreeSWITCH package backup paths.
 
 path		array  /var/backups/fusionpbx/postgresql		True	postgresql
 path		array  /usr/share/freeswitch/scripts			True 	scripts
 path		array  /var/www/fusionpbx	             	 	True 	fusionpbx
 path		array  /var/lib/freeswitch/storage	          	True 	storage
 path		array  /var/lib/freeswitch/recordings			True 	recordings
 path		array  /etc/freeswitch 				True 	conf 
 
 Click "Reload" at the top of the page.

**FreeSWITCH Source install paths.**

.. image:: ../_static/images/fusionpbx_backup_source1.jpg
        :scale: 85%


:: 
 
 Settings for FreeSWITCH source backup paths.
 
 path  array   /var/backups/fusionpbx/postgresql       True    postgresql
 path		array  	/usr/local/freeswitch/scripts 		True 	scripts  	 	
 path		array  	/usr/local/freeswitch/recordings 	True 	recordings  	
 path		array  	/var/www/fusionpbx 		        True 	fusionpbx  	
 path		array  	/usr/local/freeswitch/conf	        True 	conf  	
 path		array  	/usr/local/freeswitch/storage 		True 	storage
 
 Click "Reload" at the top of the page.

Download Backups
^^^^^^^^^^^^^^^^^

From Advanced > Backup you can download the backup from the web interface this is optional. You would need to make sure that PHP doesn't timeout while compressing your backup and that it has enough access to RAM to do the work.

**FreeSWITCH Source install paths.**

.. image:: ../_static/images/fusionpbx_backup_source.jpg
        :scale: 85%


**FreeSWITCH Package install paths.**

.. image:: ../_static/images/fusionpbx_backup_package1.jpg
        :scale: 85%
