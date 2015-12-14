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
     
    **2.** The install script will ask you a few questions
    
  


.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png
