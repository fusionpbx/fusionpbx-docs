Voicemail to Email
====================

Settings for voicemail to email and for fax notifications.


Goto Advanced > Default Settings and under the ``Email`` Section. Make sure these settings are enabled. Once these values are set press the **Reload** button at the top right of the page.
::

 method			text  	smtp 	
 smtp_auth		var  	true  	
 smtp_from		var  	username@gmail.com 	  	
 smtp_from_name	var  	Voicemail	  	
 smtp_host		var  	smtp.gmail.com 	  	
 smtp_password	var  	******* 	  	
 smtp_port		numeric  	587	
 smtp_secure		var  	tls	
 smtp_username	var  	username@gmail.com 


To see if there are any failed email attempts goto Status > Emails.  Once the issue causing the emails to fail is found you can click to resent them.

**Note**: The log is stored in the /tmp directory.

