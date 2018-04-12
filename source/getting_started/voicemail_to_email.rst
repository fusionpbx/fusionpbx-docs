Voicemail to Email
====================

Settings for voicemail to email and for fax notifications.


Goto Advanced > Default Settings and under the ``Email`` Section. Make sure these settings are enabled. Once these values are set press the **Reload** button at the top right of the page.
::

 method			text		smtp 	
 smtp_auth		text		true
 smtp_from		text		username@gmail.com
 smtp_from_name		text		Voicemail
 smtp_host		text	 	smtp.gmail.com
 smtp_password		text		*******
 smtp_port		numeric		587
 smtp_secure		text		tls
 smtp_username		text		username@gmail.com


To see if there are any failed email attempts goto Status > Emails.  Once the issue causing the emails to fail is found you can click to resent them.

**Note**: The log is stored in the /tmp directory.

