*************
Quick Install
*************
.. image:: ../_static/images/logo_right.png
        :scale: 85% 

|

Welcome to the FusionPBX installation guide. 

|

FusionPBX can be several different operating systems. However this install is focused on a **minimal** install of Debian 8 with SSH enabled. This install has been designed to be fast, simple and modular. On many systems it will install in 5 minutes or less. Installation times depend on CPU, RAM and bandwidth. Install Video https://youtu.be/YmIht8hEHYU

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="100%" height="350" src="https://www.youtube.com/embed/YmIht8hEHYU?rel=0" frameborder="0" ; encrypted-media" allowfullscreen></iframe>
    </div>
    
**1.** Run the following commands under root. The script installs FusionPBX, FreeSWITCH release package and its dependencies, IPTables, Fail2ban, NGINX, PHP FPM and PostgreSQL.

Start with a **minimal** install of Debian 8 with SSH enabled. 
Paste the following commands in the console window **one line at a time**.

::
     
wget -O - https://raw.githubusercontent.com/fusionpbx/fusionpbx-install.sh/master/debian/pre-install.sh | sh;
cd /usr/src/fusionpbx-install.sh/debian && ./install.sh
     
|

If using **Debian on Proxmox LXC** containers please run the following **BEFORE** starting the FusionPBX install.

::

 apt-get update && apt-get upgrade
 apt-get install systemd
 apt-get install systemd-sysv
 apt-get install ca-certificates
 reboot

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
      For more info visit https://www.fusionpbx.com/training.php

   Additional information.
      https://fusionpbx.com/support.php
      https://www.fusionpbx.com
      http://docs.fusionpbx.com
      https://www.fusionpbx.com/training.php

|
     
.. image:: ../_static/images/ilogin.jpg
        :scale: 80%
|

After the install script has completed go to your web browser and login with the information provided by the install script.
  
