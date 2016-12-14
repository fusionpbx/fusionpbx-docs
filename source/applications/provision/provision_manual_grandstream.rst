GrandStream
============

.. image:: ../../_static/images/fusionpbx_grandstream4.jpg
        :scale: 85%

|

Registering an **Extension** using a hardware phone or adapter (ata) using Grandstream. 

|

Granstream is one of the common brand of phone and adapters for voip.  From call centers to offices and home offices Grandstream products can be found.  Grandstream has a large selection of hardware from phones, video phones to analog telephone adapters.

|

In our example we will register an analog telephone adapter (ata) model HT701.

|

1. Goto the device ip address. The default password should be admin. Enter admin and click login

.. image:: ../../_static/images/fusionpbx_grandstream.jpg
        :scale: 85%

|

2. Click on the **FXS PORT** tab on the top right.

| ``Primary Sip Server: subdomain.domain.com``
| ``Failover SIP Server: subdomain1.domain.com (this can be left blank or can use Primary if only 1 sip server)``
| ``SIP User ID: 1000``
| ``Authenticated Password: thepassword``

|

Click **Update** then click **Apply** at the bottom

|

.. image:: ../../_static/images/fusionpbx_grandstream2.jpg
        :scale: 85%

|

3. Click the **Status** tab on the top left.  You should see the *Registration* as **Registered** and the *User ID* **1000**

.. image:: ../../_static/images/fusionpbx_grandstream1.jpg
        :scale: 85%

|

- Troubleshooting tips

|

* Check, double check that the correct extension number and password is being used.
* Reboot the device.
* Check Fail2ban and see if the ip got blocked.
* Make sure you have created an DNS A record for the domain being used and there are no typos
* Nat, firewalls and router settings.  Some brands of routers can cause issues.  Google the make and model of router or firewall appliance for common settings or remedies.
* Visit Grandstream Supoprt http://www.grandstream.com/support
|
