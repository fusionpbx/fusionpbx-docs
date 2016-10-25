*****************
Backup
*****************

|

It's always good to have a backup method in place.  Here are the steps to a basic backup method with FusionPBX. This is one of the many ways you can backup.

From the Gui.

::

 Goto Advanced > Default Settings.
 
 Settings for FreeSWITCH package installs are allready in place.
 
 For FreeSWITCH Source edit the backup paths
 path		array  	/usr/local/freeswitch/scripts 		True 	scripts  	 	
 path		array  	/usr/local/freeswitch/recordings 	True 	recordings  	
 path		array  	/var/www/fusionpbx 		        True 	fusionpbx  	
 path		array  	/usr/local/freeswitch/conf	        True 	conf  	
 path		array  	/usr/local/freeswitch/storage 		True 	storage
 
 Click "Reload" at the top of the page.


From the command line.

::
 
 
 cd /usr/src/fusionpbx-install.sh
 git pull
 cd debian/resources/backup/
 nano fusionpbx-backup.sh
 
 You will need to provide the database password
 Edit line #3 with the database passsword
 Save settings and exit
 
You should have the script ready to execute. (Default the script will use FreeSWITCH package paths.  If you have an older install using source be sure to change this by commenting the package line #22 and uncomment the source line #25.)
 
 
