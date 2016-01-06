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

Configure Inbound Destinations:

*Select* **Dialplan** from the drop-down list and then *click* **Destinations**. 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153363/86efa890-b487-11e5-8628-0b7358797493.jpg

Click on the

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png

button on the right. 

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153365/86f0df3a-b487-11e5-967d-4820f7c77f77.jpg

*Enter* the route information below and *Click* **Save** once complete.

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153362/86ef406c-b487-11e5-9b63-af8d485cb4e1.jpg

::

 Name: VoiceTel DID
 Destination Number: ^(?:\+?1)?(\d{10})$
 Action: Select desired destination from the drop-down list
 Order: 999
 Enabled: true
 Description: VoiceTel-in

::

 Optionally replace ^(?:\+?1)?(\d{10})$ in Inbound Routes with either 0123456789 or a DID Number depending on the Route Destination setting.
 

.


Outbound setup
===========


Configure Outbound Route. 


Select **Dialplan** from the drop-down list and then click **Outbound Routes** . 

Click the 

.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png

button on the right. Enter the route information below and Click **Save** once complete.

::

 Gateway: VoiceTel
 Dialplan Expression: ^(?:\+?1)?(\d{10})$
 Order: 000
 Enabled: true
 Description: VoiceTel-out


**By using** `VoiceTel <http://tiny.cc/voicetel>`_ **you help support FusionPBX.  Thank you for your support!**

