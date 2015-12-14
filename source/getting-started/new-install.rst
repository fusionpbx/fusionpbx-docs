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
     
     
    ::
     
.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png 

