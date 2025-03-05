# GrandStream

![image](../../_static/images/fusionpbx_grandstream4.jpg)


## Manual Setup - Registration

Registering an **Extension** using a hardware phone or adapter (ata)
using Grandstream.



Granstream is one of the common brands of phone and adapters for VoIP.   
From call centers to offices and home offices, Grandstream products can   
be found. Grandstream has a large selection of hardware, from phones,   
video phones to analog telephone adapters.



In our example, we will register an analog telephone adapter (ATA) model
HT701.



-  Goto the device ip address. The default password should be admin.
    Enter admin and click login

![image](../../_static/images/fusionpbx_grandstream.jpg)



-  Click on the **FXS PORT** tab on the top right.
    - Primary Sip Server: subdomain.domain.com
    - Failover SIP Server: subdomain1.domain.com (this can be left blank or can use Primary if only 1 sip server)
    - SIP User ID: 1000
    - Authenticated Password: thepassword



- Click **Update** then click **Apply** at the bottom



![image](../../_static/images/fusionpbx_grandstream2.jpg)



-  Click the **Status** tab on the top left. You should see the
   *Registration* as **Registered** and the *User ID* **1000**

![image](../../_static/images/fusionpbx_grandstream1.jpg)



## **Troubleshooting tips**


-   Check, double-check that the correct extension number and password
    are being used.
-   Reboot the device.
-   Check Fail2ban and see if the IP got blocked.
-   Make sure you have created a DNS A record for the domain being used
    and that there are no typos
-   Nat, firewalls, and router settings. Some brands of routers can cause
    issues. Google the make and model of the router or firewall appliance
    for common settings or remedies.

Visit Grandstream Support <http://www.grandstream.com/support>
