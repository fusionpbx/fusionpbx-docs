*************
Quick Install
*************
.. image:: ../_static/images/logo_right.png
        :scale: 85% 

|

Welcome to the FUSIONPBX installation guide. FUSIONPBX can be several different operating systems. However this install is focused on a **minimal** install of Debian 8 with SSH enabled. This install has been designed to be fast, simple and modular. On many systems it will install in 5 minutes or less. Installation times depend on CPU, RAM and bandwidth. Install Video https://youtu.be/YmIht8hEHYU

|
    
**1.** Run the following commands under root. The script installs FusionPBX, FreeSWITCH release package and its dependencies, IPTables, Fail2ban, NGINX, PHP FPM and PostgreSQL.

Start with a **minimal** install of Debian 8 with SSH enabled. 
Paste the following commands in the console window **one line at a time**.

::
     
 apt-get update && apt-get upgrade -y --force-yes
 apt-get install -y --force-yes git
 cd /usr/src
 git clone https://github.com/fusionpbx/fusionpbx-install.sh.git
 chmod 755 -R /usr/src/fusionpbx-install.sh
 cd /usr/src/fusionpbx-install.sh/debian
 ./install.sh
     
|

**2.** At the end of the install, the script will instruct you to go to the ip address of the server (or domain name) in your web browser to login. The script will also provide a username and secure random password for you to use. This can be changed after you login. The install script builds the fusionpbx database. If you need the database password it is located in /etc/fusionpbx/config.php .


::

   Installation has completed.

   Use a web browser to login.
      domain name: https://000.000.000.000
      username: admin
      password: zxP5yatwMxejKXd

   The domain name in the browser is used by default as part of the authentication.
   If you need to login to a different domain then use username@domain.
      username: admin@000.000.000.000

   Official FusionPBX Training
      Admin Training    24 - 26 Jan (3 Days)
      Advanced Training 31 Jan - Feb 2 (3 Days)
      Timezone: https://www.timeanddate.com/worldclock/usa/boise
      For more info visit https://www.fusionpbx.com

   Additional information.
      https://fusionpbx.com/support.php
      https://www.fusionpbx.com
      http://docs.fusionpbx.com




|


**Login with the username and password.  Make sure it is admin@ip or admin@domain.tld**
     
     
.. image:: ../_static/images/ilogin.jpg
        :scale: 80%
      


**Note**: To display the logo at the top and not in the menu

::

  go to advanced -> default settings >  menu_style >  set to inline



Also, be sure to watch the youtube video from FreeSWITCH Cluecon Weekly https://www.youtube.com/embed/kejAxlYSW3o FusionPBX is installed and more!
