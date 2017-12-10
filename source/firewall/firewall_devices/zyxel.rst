#########
ZyXel
#########



This guide was created using V4.2/4.25 firmware on a ZyXEL USG60 series UTM router.  The PBX is in the cloud with a public IP, and the ZyXEL USG60 router is at the customer’s location with the extensions behind it.

 

How to setup Bandwidth Management “BWM” aka QoS
================================================

There are more than one ways to apply the BWM rules.  They can be applied on a service level, or on an object level, or both.  In this example we will provide traffic priority to traffic between the LAN and the cloud PBX.

 

First, set up an Object for your Cloud PBX.

                * Log into the USG and go to Configuration-> Object-> Address/GeoIP

                * Click the Add button

Create a name, and enter the static public IP of your PBX.  If you have more than one, such as a failover, add that as well and create a group.

.. image:: ../../_static/images/firewall/fusionpbx_zyxel_usg60_bwm_.png
        :scale: 85%

