#########
ZyXel
#########



This guide was created using V4.2/4.25 firmware on a ZyXEL USG60 series UTM router.  FusionPBX is in the cloud with a public IP, and the ZyXEL USG60 router is at the customer’s location with the extensions behind it.

 

How to setup Bandwidth Management “BWM” aka QoS
================================================

There are more than one ways to apply the BWM rules.  They can be applied on a service level, or on an object level, or both.  In this example we will provide traffic priority to traffic between the LAN and the cloud PBX.

 

First, set up an Object for your Cloud PBX.

* Log into the USG and go to Configuration-> Object-> Address/GeoIP

* Click the Add button

Create a name, and enter the static public IP of your FusionPBX.  If you have more than one, such as a failover, add that as well and create a group.

.. image:: ../../_static/images/firewall/fusionpbx_zyxel_usg60_object_address.png
        :scale: 85%

Next, set up a Service Object for the VOIP traffic.

* Go to Configuration-> Object-> Service

* Click the Add button.

Create a name, and set the ports for your traffic.  In this example we will add a Service rule for 5060TCP, 5060UDP, and 16384-32768 UDP.

.. Note:: If you’ve created more than one service object, click the Service Group tab and create a group.  Add the service objects that you’ve created to the group.

.. image:: ../../_static/images/firewall/fusionpbx_zyxel_usg60_object_service.png
        :scale: 85%

