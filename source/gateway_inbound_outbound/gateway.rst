Inbound Destination setup
==========================

Inbound destinations are the DID/DDI, DNIS or Alias for inbound calls.

|

Configure Inbound Destinations: (This will auto-configure an Inbound Route also)

*Select* **Dialplan** from the drop-down list and then *click* **Destinations**. 

.. image:: ../_static/images/fusionpbx_inboundd.jpg
        :scale: 85%

Click on the

.. image:: ../_static/images/plus.png
        :scale: 85%

button on the right. 

.. image:: ../_static/images/fusionpbx_inboundd1.jpg
        :scale: 85%

*Enter* the route information below and *Click* **Save** once complete.

.. image:: ../_static/images/fusionpbx_inboundd2.jpg
        :scale: 85%

::

 Type: Inbound
 Destination Number: ^(?:\+?1)?(\d{10})$
 Action: Select desired destination from the drop-down list.  We choose "Extension 100" in our example.  This is where the call will route to.
 Enabled: true
 Description: VoiceTel-in
 
|
|
 
::

 Optional: Replace ^(?:\+?1)?(\d{10})$ in Inbound Routes with either 0123456789 or a DID Number depending on the Route Destination setting.
 

|
|


Outbound setup
===============

Route outbound calls to gateways, tdm, enum and more. When a call matches the conditions the call to outbound routes. 

|

Configure Outbound Route. 


Select **Dialplan** from the drop-down list and then click **Outbound Routes** . 

.. image:: ../_static/images/fusionpbx_outbound.jpg
        :scale: 85%

Click the 

.. image:: ../_static/images/plus.png
        :scale: 85%



button on the right. Enter the route information below and Click **Save** once entry is complete.

|
|

.. image:: ../_static/images/fusionpbx_outbound1.jpg
        :scale: 85%

|



|

.. image:: ../_static/images/fusionpbx_outbound2.jpg
        :scale: 85%

|
|

::

 Gateway: VoiceTel
 Dialplan Expression: ^(?:\+?1)?(\d{10})$ (You can also choose more than one from the drop down list also as needed)
 Order: 000
 Enabled: true
 Description: VoiceTel-out

|
|

**By using** `VoiceTel <http://tiny.cc/voicetel>`_ **you help support FusionPBX.  Thank you for your support!**

