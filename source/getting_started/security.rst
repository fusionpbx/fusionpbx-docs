***********
Security
***********

Similar to medieval fortifications it is best practice to provide your servers with multiple layers of defenses. Latest FusionPBX Debian install script configures iptables for you. Fail2ban is also used to protect SSH, FreeSWITCH, the web server and more. It is also good practice to use secure passwords for extensions. FusionPBX creates extension passwords for you and you can use default settings to lengthen the passwords for increased security. SSH public key authentication can be used to help protect the server from the SSH password being discover by brute forced. 

::

 iptables -L


Upgrade
^^^^^^^^

Security problems are fixed as they are discovered and are updated for master and the latest release. Upgrades are considered an important part of keeping the server secure. `Upgrades`_ always need to be done on the operating system, FreeSWITCH and FusionPBX. On Debian and Ubuntu you can check your firewall with the following command.

Latest install script will install FreeSWITCH packages by default to upgrade them and operating system packages run the following commands.

::

 apt-get update
 apt-get upgrade


If you need help upgrading safely please consider `paid support`_.


XML RPC
^^^^^^^^^^^^

New install mod_xml_rpc is not enabled by default. It is recommended to run a firewall on all FusionPBX servers. The latest debian install script configures the firewall by default. However it is recommended to check to make sure it is installed and running.

Mod_xml_rpc allows running remote commands to FreeSWITCH. Ensure you have afirewall that is protecting the XML RPC port. Consider changing the XML RPC password. At very least do not allow access to the public. Advanced -> Settings page in the interface allows you to change the password or the port. Do not allow public access to the XML RPC port.

Latest Debian install script installs `iptables`_ firewall which prevents public access to the mod_xml_rpc port. If you are not using a firewall on the server you should even if its protected by by an external firewall. Some not informed co-worker could expose the server to the public internet at some point in the future. Multiple layers of security is considered best practice.



.. _Upgrade: /en/latest/getting_started/advanced/upgrade.html
.. _Upgrades: /en/latest/getting_started/advanced/upgrade.html
.. _paid support: http://www.fusionpbx.com
.. _firewall: /en/latest/getting_started/post_installation.html#iptables
.. _iptables: /en/latest/getting_started/post_installation.html#iptables
