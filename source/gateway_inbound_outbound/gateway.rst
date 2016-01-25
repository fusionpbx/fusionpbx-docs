Inbound Destination setup
===========

Inbound destinations are the DID/DDI, DNIS or Alias for inbound calls.

|

Configure Inbound Destinations: (This will auto-configure an Inbound Route also)

*Select* **Dialplan** from the drop-down list and then *click* **Destinations**. 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153363/86efa890-b487-11e5-8628-0b7358797493.jpg

Click on the

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png

button on the right. 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153365/86f0df3a-b487-11e5-967d-4820f7c77f77.jpg

*Enter* the route information below and *Click* **Save** once complete.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153362/86ef406c-b487-11e5-9b63-af8d485cb4e1.jpg

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
===========

Route outbound calls to gateways, tdm, enum and more. When a call matches the conditions the call to outbound routes. 

|

Configure Outbound Route. 


Select **Dialplan** from the drop-down list and then click **Outbound Routes** . 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12156744/e8fd860c-b49a-11e5-9136-2025ed9b9cd2.jpg

Click the 

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png



button on the right. Enter the route information below and Click **Save** once complete.

|
|

.. image:: https://cloud.githubusercontent.com/assets/13131198/12156743/e8f91c0c-b49a-11e5-88c5-f2475fc1bfad.jpg

|
|

.. image:: https://cloud.githubusercontent.com/assets/13131198/12157521/633bfb4c-b4a0-11e5-9019-8217560076cc.jpg

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

