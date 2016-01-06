Gateway setup
===========

.. image:: https://cloud.githubusercontent.com/assets/13131198/11903431/270a6c1c-a587-11e5-8473-f7e84e02bf0c.png
  
  
.. rubric:: .
.. rubric:: .

**In this example we will be using** `VoiceTel <http://tiny.cc/voicetel>`_ .  **Each Gateway provider has their own setings to use.**    
   
    



.. image:: https://cloud.githubusercontent.com/assets/13131198/12149664/e05ebd40-b472-11e5-83c3-5931c7c409d3.jpg 

`Click to visit <http://tiny.cc/voicetel>`_  
    
.. rubric:: .
.. rubric:: .
    


Select **Accounts** from the drop-down list and click on **Gateways**. 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12148465/999cf76a-b46c-11e5-85ae-e42c0d3dc97b.jpg

.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12148464/999caf08-b46c-11e5-832e-b13240e01bc5.jpg


Click the 

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png

button on the right. Enter the gateway information below and Click on **Save** once complete.

::

  Gateway: VoiceTel 
  Username: 0123456789 
  Password: 1b3d5f7h9j 
  From user: 0123456789 
  From domain: sbc.voicetel.com 
  Proxy: sbc.voicetel.com 
  Register: true 
  Enabled: true 
.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12148466/99a8a5ba-b46c-11e5-80d2-4aca54114640.jpg


Inbound Destination setup
===========

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
 
 
 
::

 Optional: Replace ^(?:\+?1)?(\d{10})$ in Inbound Routes with either 0123456789 or a DID Number depending on the Route Destination setting.
 

.


Outbound setup
===========


Configure Outbound Route. 


Select **Dialplan** from the drop-down list and then click **Outbound Routes** . 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12156744/e8fd860c-b49a-11e5-9136-2025ed9b9cd2.jpg

Click the 

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png



button on the right. Enter the route information below and Click **Save** once complete.

.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12156743/e8f91c0c-b49a-11e5-88c5-f2475fc1bfad.jpg

.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12157521/633bfb4c-b4a0-11e5-9019-8217560076cc.jpg

::

 Gateway: VoiceTel
 Dialplan Expression: ^(?:\+?1)?(\d{10})$ (You can also choose more than one from the drop down list also as needed)
 Order: 000
 Enabled: true
 Description: VoiceTel-out


**By using** `VoiceTel <http://tiny.cc/voicetel>`_ **you help support FusionPBX.  Thank you for your support!**

