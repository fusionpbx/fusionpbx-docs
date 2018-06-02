#########
GMAIL
#########


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

+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| Default Setting Subcategory | Default Setting Name | Default Setting Value      | Default Setting Enabled | Default Setting Description                                                       |
+=============================+======================+============================+=========================+===================================================================================+
| smtp_host                   | text                 | smtp.gmail.com             | False                   |  email providers server address                                                   |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from                   | text                 | emailaddress@gmail.com     | True                    |  smtp from emaill address                                                         |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_port                   | numeric              | 587                        | True                    | port number of the mail server provider                                           |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from_name              | text                 | Voicemail                  | True                    |  smtp from name                                                                   |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_auth                   | text                 | TRUE                       | True                    |  smtp auth is required                                                            |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_username               | text                 | emailaddress@gmail.com     | True                    |  Use the full email address                                                       |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_password               | text                 | ************************** | True                    |   typically the email password                                                    |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_secure                 | text                 | tls                        | True                    |  tls or ssl depending on the provider.                                            |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_validate_certificate   | boolean              | TRUE                       | True                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| method                      | text                 | smtp                       | True                    | smtp|sendmail|mail|qmail                                                          |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+

To see if there are any failed email attempts goto Status > Emails.  Once the issue causing the emails to fail is found you can click to resent them.

**Note**: The log is stored in the /tmp directory.

