Outbound Routes
================

Route outbound calls to gateways, tdm, enum and more. When a call matches the conditions the call to outbound routes. `Check out the youtube video <https://youtu.be/rhyfCKLBI-Y>`_ .

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
