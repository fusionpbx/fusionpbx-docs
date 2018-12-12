***********
Firewall
***********

**Basic ports used**

* SIP TCP/UDP
    *    5060-5090
* RTP UDP
    *    16384-32768
* SSH
    *    22
* HTTP
    *    80, 443


.. toctree::
  :maxdepth: 3
  :glob:

  firewall/iptables.rst
  firewall/fail2ban.rst
  firewall/pf.rst
 
 
Firewall Devices
=====================

Firewall device settings that help with SIP connections.

.. toctree::
   :maxdepth: 4
   
  hardware/firewall_devices/asus_rt_ac66u.rst  
  firewall/firewall_devices/edgerouterx.rst
  firewall/firewall_devices/pfsense.rst
  firewall/firewall_devices/sonicwall_tz_soho.rst
  firewall/firewall_devices/zyxel.rst
  
  

Firewall Devices ALG
========================

Most of the time this setting is set to off or disabled and varies. Rarely this should be enabled. Below is a list a devices that need setting changes to address SIP ALG issues.

.. toctree::
   :maxdepth: 4
   
  firewall/firewall_devices/asus_rt_ac66u_sip_alg.rst
  firewall/firewall_devices/cisco_ea6500.rst
  firewall/firewall_devices/sonicwall_tz_soho_sip_alg.rst
  firewall/firewall_devices/zyxel_sip_alg.rst

