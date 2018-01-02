##################
SonicWall TZ-SOHO
##################




This guide was created using 6.5.0.1-14n firmware on a SonicWall TZ-SOHO series UTM router. FusionPBX is in the cloud with a public IP, and the SonicWall router is at the customer’s location with the extensions behind it.

How to setup Bandwidth Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**First, enable Global Bandwidth Management:**

* Log into the SonicWall and go to Security Configuration -> Firewall Settings -> Bandwidth Management
* For Bandwidth Management Type, click the Global radio button.
* This will enable BWM for all traffic.
Enable your required Priority levels.  For voice traffic, we’ll enable the “0 Realtime” priority level.


.. image:: ../../_static/images/firewall/fusionpbx_sonicwall_bwm1.png
        :scale: 85%


Now create your VOIP services.  In this example we’ll use 5060TCP, 5060UDP, and 16384-32768UDP for voice traffic.

* Go to Policies -> Objects -> Service Objects, and click Add.
* Add objects for your VOIP services.  On typical installs this would be 5060TCP/UPD and 16384-32768UDP.
* Click on the Service Groups tab and add all of the services you’ve created to a group.


.. image:: ../../_static/images/firewall/fusionpbx_sonicwall_bwm2.png
        :scale: 85%





