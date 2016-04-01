*****************
New Install
*****************
.. image:: ../_static/images/logo_right.png
        :scale: 85% 
*************

    Welcome to the FUSIONPBX getting started guide.  In this section we will show how to install FUSIONPBX.  FUSIONPBX can be used on multiple different operating systems, databases, and web servers.  In this guide we will show on Debian 8 (Jessie), Postgresql and NGINX.  **Please note to have a clean install.  The install script will install everthing but the Operating System**
    
    
    **1.** Goto a console and follow the recomended steps from http://fusionpbx.com/download.php  
     
    ::
     
     cd /usr/src 
     apt-get install wget  
     wget https://raw.githubusercontent.com/fusionpbx/fusionpbx-scripts/master/install/debian/install_fusionpbx.sh  
     chmod 755 install_fusionpbx.sh 
     ./install_fusionpbx.sh install-both auto 
     
|

    **2.** The install script will apt-get update/upgrade the system and ask you a few questions
     
     
    ::
     
     The pgsql username is fusionpbx
     The pgsql database name is fusionpbx
     Please provide a password for the fusionpbx user
      Password:IloveFusionpbx
     Let's repeat that
      Password:IloveFusionpbx
     
    *It can take between 15-30 minutes to compile and install*

|

    **3.** Goto a web browser and enter the ip address
    ::
     
     Now you'll need to manually finish the install and come back
     This way I can finish up the last bit of permissions issues
     Just go to
     http://ur_domain_or_ip.com
     MAKE SURE YOU CHOOSE PostgreSQL as your Database on the first page!!!
     ON the Second Page:
     Database Name: fusionpbx
     Database Username: fusionpbx
     Database Password: whateveryouentered
     Create Database Username: Leave_Blank
     Create Database Password: Leave_Blank
 
|

     
    **4.** Web browser Installation part
     :Select Language: **Pick your language. Click next**
     .. image:: ../_static/images/install_lang.jpg
        :scale: 85%

|

     :Freeswitch Detect: **Detecting folder paths used** 
     .. image:: ../_static/images/install_detect_freeswitch.jpg
        :scale: 85% 

     
     **Don't change anything here**
    
|

     :Database Configuration: **Click Execute**
     .. image:: ../_static/images/install_database_config.jpg
        :scale: 85% 
     
     **Don't change anything here** 
     
|

     :Admin Login Configuration: **Click Next**
     .. image:: ../_static/images/install_admin_username.jpg
        :scale: 85% 
     
     This will create the superadmin login that will be used in your web browser.

 
|

    **5.** Goto Console and press enter 
    ::
     When PostgreSQL is configured come back and press enter.
     
     The FusionPBX installation changed permissions of /usr/local/freeswitch/storage
     Waiting on you to finish installation (via browser), I'll clean up
     the last bit of permissions when you finish.Waiting on /var/www/fusionpbx/resources/config.php
     
     /var/www/fusionpbx/resources/config.php Found!
     Waiting 5 more seconds to be sure.
     .....   Fixing...
     FIXED
     Setting up Fail2Ban for FusionPBX
     
     
     
     Installation Completed.  Now configure FreeSWITCH via the FusionPBX browser interface
     
     http://104.233.77.151
     Default login is (whatever you picked in the GUI install):
     User: WhateverUsernameYouPicked
     Password: YourPasswordYouPicked
     Checking to see if FreeSWITCH is running!
        
     
    
|

     :Install Finished:  **Login with the username and password you choose during the install**
     
     
      .. image:: ../_static/images/ilogin.jpg
        :scale: 50%
      
    
|

**Note**: To display the logo at the top and not in the menu

::

  go to advanced -> default settings >  menu_style >  set to inline

