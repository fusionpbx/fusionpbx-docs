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

