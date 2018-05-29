************
Provision
************


Automatic
^^^^^^^^^^

Auto provisioning is disabled by default. This is to give a chance to secure provisioning server with HTTP Authentication or CIDR. HTTP Authentication requires the phone to send hash of the combined username and password in order to get configuration. CIDR is an IP address restriction that can be used to restrict which IP addresses are allowed to get the device configuration. An example of CIDR is xxx.xxx.xxx.xxx/32 the /32 represents a single IP address. To set one of these values go to Advanced > Default Settings and find the Provision category from there used the edit button to set a value. After this is done it is safe to set enabled equal to true.

*  `Yealink <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_yealink.html>`_
*  `Polycom <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_polycom.html>`_
*  `Cisco <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_cisco.html>`_
*  `Fanvil <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_fanvil.html>`_
*  `Grandstream <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_grandstream.html>`_
*  `Htek <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_htek.html>`_
*  `Zoiper <http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_zoiper.html>`_


Manual
^^^^^^^

How to setup the device using the phone's web interface.

*  `Yealink <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_yealink.html>`_
*  `Polycom <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_polycom.html>`_
*  `Cisco <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_cisco.html>`_
*  `Fanvil <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_fanvil.html>`_
*  `Grandstream <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_grandstream.html>`_
*  `Htek <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_htek.html>`_
*  `Zoiper <http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_zoiper.html>`_


Advanced > Default Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the Provisioning section, there are a few key options that have to be set in order to turn auto provisioning on.

* **enabled** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default.
* **http_auth_username** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default. Be sure to use a strong username.
* **http_auth_password** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default. Be sure to use a strong password.



Phone Screen Capture
^^^^^^^^^^^^^^^^^^^^^

* `Screen Capture <http://docs.fusionpbx.com/en/latest/applications/provision/phone_screen_capture.html>`_


.. Note::
       `Click here to view how to add a device <http://docs.fusionpbx.com/en/latest/accounts/devices.html>`_.

