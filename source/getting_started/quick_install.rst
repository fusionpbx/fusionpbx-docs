*************
Quick Install
*************
.. image:: ../_static/images/logo_right.png
        :scale: 85% 

|

Quick Install Video https://youtu.be/YmIht8hEHYU

|

Welcome to the FUSIONPBX getting started guide.  In this section we will show how to install FUSIONPBX.  FUSIONPBX can be used on multiple different operating systems, databases, and web servers.  In this guide we will show on Debian 8 (Jessie), Postgresql and NGINX.  **Please note to have a clean install.  The install script will install everything but the Operating System**
    
    
**1.** Goto a console and follow the recommended steps from https://fusionpbx.com/app/www/download.php for a standard installation.  Some installations require special considerations.  Visit https://github.com/fusionpbx/fusionpbx-install.sh Readme section for more details.

This install script is designed to be a fast, simple, and modular way to install FusionPBX. Start with a minimal install of Debian 8 with SSH enabled. Run the following commands under root. The script installs FusionPBX, FreeSWITCH release package and its dependencies, IPTables, Fail2ban, NGINX, PHP FPM and PostgreSQL.

Also, be sure to watch the youtube video from FreeSWITCH Cluecon Weekly https://www.youtube.com/embed/kejAxlYSW3o FusionPBX is installed and more!
     
::
     
  wget https://raw.githubusercontent.com/fusionpbx/fusionpbx-install.sh/master/install.sh -O install.sh && sh install.sh
     
|

**2.** At the end of the install the script will instruct you to go to the ip address of the server in your web browser to login. The script will also provides a username and secure random password for you to use. This can be changed after you login. The install script builds the fusionpbx database so you will not need to use the create database username and password. If you need the database password it is located in /etc/fusionpbx/config.php .

   

::

   Installation has completed.

   Use a web browser to login.
      domain name: https://108.61.158.12
      username: admin
      password: zxP5yatwMxejKXd

   The domain name in the browser is used by default as part of the authentication.
   If you need to login to a different domain then use username@domain.
      username: admin@108.61.158.12

   Official FusionPBX Training
      Admin Training    24 - 26 Jan (3 Days)
      Advanced Training 31 Jan - Feb 2 (3 Days)
      Timezone: https://www.timeanddate.com/worldclock/usa/boise
      For more info visit https://www.fusionpbx.com

   Additional information.
      https://fusionpbx.com/support.php
      https://www.fusionpbx.com
      http://docs.fusionpbx.com


*The new install has been optimized to be simple to use and quick to install. On manysystems it will install in 5 minutes or less.  Installation times depends on CPU, RAM and bandwidth to the internet.)

|


Install Finished  **Login with the username and password you choose during the install**
     
     
.. image:: ../_static/images/ilogin.jpg
        :scale: 80%
      


**Note**: To display the logo at the top and not in the menu

::

  go to advanced -> default settings >  menu_style >  set to inline

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



