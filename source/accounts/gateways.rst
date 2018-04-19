Gateways
=========

Gateways define the location and settings for other VoIP servers or Providers. After defining the Gateways use the Outbound routes to direct calls through the gateways. Required items are in bold.


`Check out the Youtube video <https://youtu.be/YKOTACDYQ3A>`_ .

**In this example we will be using** `VoiceTel <http://tiny.cc/voicetel>`_ .  **Each Gateway provider has their own setings to use.**    

.. image:: ../_static/images/fusionpbx_voicetel.jpg
        :scale: 85% 
        :target: http://tiny.cc/voicetel

 

Select **Accounts** from the drop-down list and click on **Gateways**. 

.. image:: ../_static/images/fusionpbx_gateway.jpg
        :scale: 85%


.. image:: ../_static/images/fusionpbx_gateway1.jpg
        :scale: 85%


Click the 

.. image:: ../_static/images/plus.png
        :scale: 85%

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

|

.. image:: ../_static/images/fusionpbx_gateway2.jpg
        :scale: 85%


Basic Gateway Settings
^^^^^^^^^^^^^^^^^^^^^^^^

* **Gateway:**  Name the Gateway.
* **Username:** This is specific and typically given by the carrier.
* **Password:** This is specific and typically given by the carrier.
* **From User:** This is specific and typically given by the carrier.
* **From Domain:** This is specific and typically given by the carrier.  This will be the domain your FusionPBX connects to for sending calls.
* **Proxy:** Proxy server address used by the carrier. This will vary by carrier.
* **Realm:** This is specific and typically given by the carrier. Most times will be blank.  Only used by some carriers
* **Expire Seconds:** Time until the registration to the carrier expires.
* **Register:** Set to **true** if the carrier uses a user name and password.  Set to **false** if the carrier uses ip authentication.  If false, you will need to specify all of the carrier ip's in **Advanced > Access Controls.**
* **Context:** This is usually set as public.
* **Profile:** The sip profile used.  If you change the sip profiles, be sure to change this to match.
* **Hostname:** When the hostname is set the gateway will only start on the matching server with same hostname. If the hostname is left blank the gateway will start regardless of the server's hostname.
* **Enabled:** If the gateway is enabled or disabled.
* **Description:** A way to organize if you use more than one gateway.


Advanced Gateway Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^

Most settings in the Advanced Gateway Settings can remain the same.  Some carriers will require slight changes in this section to help with outbound caller ID.

* **Distinct To:** 
* **Auth Username:** 
* **Extension:** Mostly used for testing and not for production. Hard codes a set number and all calls would be hard coded to that number for inbound calls from that gateway.
* **Register Transport:** Use this setting to register with tcp, udp or tls to the carrier.
* **Register Proxy:** Enter the hostname or IP address of the register proxy. host[:port].
* **Outbound Proxy:** Enter the hostname or IP address of the outbound proxy. host[:port].
* **Caller ID In From:** Set to true or false.
* **Supress CNG:** Set to true or false.
* **Sip CID Type:** Enter the sip cid type: none, pid, and rpid.
* **Codec Preferences:** Enter the codec preferences as a list. Ex: PCMA,PCMU,G722,OPUS
* **Extension In Contact:** Enters the Extension In Contact.
* **Ping:** Enter the ping interval here in seconds.
* **Domain:** If the gateway will be used on a specific domain or global to all tenants.


