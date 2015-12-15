.. image:: https://github.com/fusionpbx/fusionpbx/blob/master/themes/enhanced/images/logo.png
*************



    Welcome to the FUSIONPBX getting started guide.  In this section we will show how to install FUSIONPBX.  FUSIONPBX can be used on multiple different operating systems, databases, and web servers.  In this guide we will show on Debian 8 (Jessie), Postgresql and NGINX.  **Please note to have a clean install.  The install script will install everthing but the Operating System**
    
    
    **1.** Goto a console and follow the recomended steps from http://fusionpbx.com/download.php  
     
    ::
     
     cd /usr/src 
     apt-get install wget  
     wget https://raw.githubusercontent.com/fusionpbx/fusionpbx-scripts/master/install/ubuntu/install_fusionpbx.sh  
     chmod 755 install_fusionpbx.sh 
     ./install_fusionpbx.sh install-both auto 
     
    **2.** The install script will apt-get update/upgrade the system and ask you a few questions
     
     
    ::
     
     The pgsql username is fusionpbx
     The pgsql database name is freeswitch
     Please provide a password for the fusionpbx user
      Password:IloveFusionpbx
     Let's repeat that
      Password:IloveFusionpbx
     
    *It can take between 15-30 minutes to compile and install*
     
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
     
    **4.** Web browser Installation part
     
     
    

 
     :Select Language: **Pick your language. Click next**
     .. image:: https://cloud.githubusercontent.com/assets/13131198/11797615/3b84a6aa-a292-11e5-92be-9130fe480f9b.jpg 
    
    
     :Freeswitch Detect: **Detecting folder paths used** 
     .. image:: https://cloud.githubusercontent.com/assets/13131198/11802026/c5a78c04-a2b9-11e5-9a79-e77ef3298c49.jpg 
    
    
    
     ** Don't change anything here**
    
    
    
    
     :Database Configuration: **Click Next**
     .. image:: https://cloud.githubusercontent.com/assets/13131198/11797607/2bfe2fb2-a292-11e5-9d58-e344678f3fdb.jpg
    
    
    
    
     **Don't change anything here**
    
    
    
     :Admin Login Configuration: **Click Next**
     .. image:: https://cloud.githubusercontent.com/assets/13131198/11797659/99b6c424-a292-11e5-81a2-1bfae36ce197.jpg 
    
    
    
     This will create the superadmin login that will be used in your web browser.
     
    **5.** Goto Console and press enter 
    
    
    
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
     Passwd: YourPasswordYouPicked
     Checking to see if FreeSWITCH is running!
        
     
     
        
     
     :Install Finished:  **Login!!!**
     .. image:: https://cloud.githubusercontent.com/assets/13131198/11797604/25935530-a292-11e5-8612-7dba48d65bde.jpg 
    
    

    .. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png 

