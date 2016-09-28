***********
Security
***********

Much like the days of castles, today's server security should have the same type of practice with layers.  Having just a perimeter is not enough.  A `firewall`_ on each server is a highly suggested layer of protection.

Upgrade
^^^^^^^^

Security is fixed as problems are discovered and so upgrades are considered an important part of keep the server secure. `Upgrades`_ always need to be done on the opeating system, FreeSWITCH and FusionPBX. On Debian and Ubuntu you can check your firewall with the following command.

::

 iptables -L


If you need help upgrading safely please consider `paid support`_.

mod_xml_rpc
^^^^^^^^^^^^

New install mod_xml_rpc is not enabled by default. It is recommended to run a firewall on all FusionPBX servers. The latest debian install script configures the firewall by default. However it is recommended to check to make sure it is installed and running.

Mod_xml_rpc allows running remote commands to FreeSWITCH. Ensure you have afirewall that is protecting the XML RPC port. Consider changing the XML RPC password. At very least do not allow access to the public. Advanced -> Settings page in the interface allows you to change the password or the port. Do not allow public access to the XML RPC port.

Latest Debian install script installs `iptables`_ firewall which prevents public access to the mod_xml_rpc port. If you are not using a firewall on the server you should even if its protected by by an external firewall. Some not informed co-worker could expose the server to the public internet at some point in the future. Multiple layers of security is considered best practice.




.. _Upgrade: /en/latest/getting_started/advanced/upgrade.html
.. _Upgrades: /en/latest/getting_started/advanced/upgrade.html
.. _paid support: http://www.fusionpbx.com
.. _firewall: /en/latest/getting_started/post_installation.html#iptables
.. _iptables: /en/latest/getting_started/post_installation.html#iptables
