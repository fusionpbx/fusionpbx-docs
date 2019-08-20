#########
Gmail
#########


Goto Advanced > Default Settings and under the ``Email`` Section. Make sure these settings are enabled. Once these values are set press the **Reload** button at the top right of the page.

* There is a good chance you will have to do this via command line on your FusionPBX install https://accounts.google.com/b/0/DisplayUnlockCaptcha
* If you have a headless install(no desktop gui) then you will have to install lynx.  Lynx is a command line web browser.  For Debian you would type the example below.  Follow the prompts for email address and password.

::

 apt-get install lynx
 lynx https://accounts.google.com/b/0/DisplayUnlockCaptcha


* You may also have to enable less secure apps https://support.google.com/accounts/answer/6010255?hl=en

+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| Default Setting Subcategory | Default Setting Name | Default Setting Value      | Default Setting Enabled | Default Setting Description                                                       |
+=============================+======================+============================+=========================+===================================================================================+
| smtp_host                   | text                 | smtp.gmail.com             | True                    |  email providers server address                                                   |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from                   | text                 | emailaddress@gmail.com     | True                    |  smtp from emaill address                                                         |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_port                   | numeric              | 587                        | True                    | port number of the mail server provider                                           |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from_name              | text                 | Voicemail                  | True                    |  smtp from name                                                                   |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_auth                   | text                 | true                       | True                    |  smtp auth is required                                                            |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_username               | text                 | emailaddress@gmail.com     | True                    |  Use the full email address                                                       |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_password               | text                 | ************************** | True                    |   typically the email password                                                    |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_secure                 | text                 | tls                        | True                    |  tls or ssl depending on the provider.                                            |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_validate_certificate   | boolean              | true                       | True                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+
| method                      | text                 | smtp                       | True                    | smtp|sendmail|mail|qmail                                                          |
+-----------------------------+----------------------+----------------------------+-------------------------+-----------------------------------------------------------------------------------+

To see if there are any failed email attempts goto Status > Emails.  Once the issue causing the emails to fail is found you can click to resent them.

.. Note::
       The log is stored in the /tmp directory.

