*************
Hardware
*************



Auto Provision Phones
==============================

Auto provisioning is disabled by default. This is to give a chance to secure provisioning server with HTTP Authentication or CIDR. HTTP Authentication requires the phone to send hash of the combined username and password in order to get configuration. CIDR is an IP address restriction that can be used to restrict which IP addresses are allowed to get the device configuration. An example of CIDR is xxx.xxx.xxx.xxx/32 the /32 represents a single IP address. To set one of these values go to Advanced > Default Settings and find the Provision category from there used the edit button to set a value. After this is done it is safe to set enabled equal to true.

.. toctree::
   :maxdepth: 4
  
  applications/provision/provision_auto_yealink.rst
  applications/provision/provision_auto_polycom.rst
  applications/provision/provision_auto_cisco.rst
  applications/provision/provision_auto_fanvil.rst
  applications/provision/provision_auto_grandstream.rst
  applications/provision/provision_auto_htek.rst
  applications/provision/provision_auto_zoiper.rst




Manually Provision Phones
==============================

How to setup the device using the phone’s web interface.

.. toctree::
   :maxdepth: 4
  
  applications/provision/provision_manual_yealink.rst
  applications/provision/provision_manual_polycom.rst
  applications/provision/provision_manual_cisco.rst
  applications/provision/provision_manual_fanvil.rst
  applications/provision/provision_manual_grandstream.rst
  applications/provision/provision_manual_htek.rst
  applications/provision/provision_manual_zoiper.rst
  applications/provision/provision_manual_snom.rst
  applications/provision/phone_screen_capture.rst







Firewall Devices
=====================

Firewall device settings that help with SIP connections.

.. toctree::
   :maxdepth: 4
   
  hardware/firewall_devices/asus_rt_ac66u.rst
  #firewall/firewall_devices/asus_rt_ac66u_sip_alg.rst
  firewall/firewall_devices/edgerouterx.rst
  #firewall/firewall_devices/edgerouterx_alg.rst
  firewall/firewall_devices/pfsense.rst
  firewall/firewall_devices/sonicwall_tz_soho.rst
  #firewall/firewall_devices/sonicwall_tz_soho_sip_alg.rst
  firewall/firewall_devices/zyxel.rst
  #firewall/firewall_devices/zyxel_sip_alg.rst
  firewall/firewall_devices/cisco_ea6500.rst
  
  



