Gateway setup
===========
    .. image:: https://cloud.githubusercontent.com/assets/13131198/11903431/270a6c1c-a587-11e5-8473-f7e84e02bf0c.png
  
  
    
    
    

   .. image:: http://www.voicetel.com/images/voicetel_logo.png 


    
    
    
    

* Setting up a gateway.  

In this example we will be using Voicetel.  Each Gateway provider has their own setings to use.
Select **Accounts** from the drop-down list and click on **Gateways**. Click the 
``.. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png``
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




Inbound Destination setup
===========

Configure Inbound Route:

*Select* **Dialplan** from the drop-down list and then *click* on **Inbound Routes**. Click on the .. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png button on the right. *Enter* the route information below and *Click* on **Save** when complete.
::

 Name: VoiceTel DID
 Destination Number: ^(?:\+?1)?(\d{10})$
 Action: Select desired destination from the drop-down list
 Order: 999
 Enabled: true
 Description: VoiceTel-in

``Optionally replace ^(?:\+?1)?(\d{10})$ in Inbound Routes with either 0123456789 or a DID Number depending on the Route Destination setting.`` .

.


Outbound setup
===========


Configure Outbound Route. 


Select **Dialplan** from the drop-down list and then click **Outbound Routes** . Click the .. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png button on the right. Enter the route information below and Click on **Save** when complete.

::

 Gateway: VoiceTel
 Dialplan Expression: ^(?:\+?1)?(\d{10})$
 Order: 000
 Enabled: true
 Description: VoiceTel-out


