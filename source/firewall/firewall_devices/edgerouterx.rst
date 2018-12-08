######################
Ubiquity EdgerouterX
######################


Ubiquity EdgerouterX Advanced Gigabit Ethernet Router.



Port Forwarding
^^^^^^^^^^^^^^^^^

Go to top first menu item Firewall/NAT then second top menu item Port Forwarding.

.. image:: ../../_static/images/firewall/fusionpbx_ubnt_port_forward.jpg
        :scale: 85%


* Optional: SSH port 22 is optional.
* Required: Sip port range 5060-5090 is recomended.
* Required: HTTPS port 443 is required in order to access your FusionPBX installation and phone provisioning.
* Optional: HTTP port 80 is used by some phone manufactures for provisioning.
* Required: RTP port range 16384-32768.

.. note::
       In order to Port Forward and still have access to the EdgerouterX GUI you must change the port number for the EdgerouterX GUI.




Access from another LAN Subnet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are behind NAT and are going to use the EdgerouterX subnet in addition to an existing subnet (behind another router) also some setting changes are required. These settings are only recommended in this scenerio.

* Go to First top menu Firewall/NAT tab.
* Go to Second top menu Firewall Policies.
* Edit WAN_LOCAL at the right menu item Actions > Edit RuleSet 


.. image:: ../../_static/images/firewall/fusionpbx_ubnt_firewall_policies_enable_outside_lan_gui_access.jpg
        :scale: 85%



* From the Configuration tab, Change the radio button to "Accept" and click "Save Ruleset".


.. image:: ../../_static/images/firewall/fusionpbx_ubnt_firewall_policies_enable_outside_lan_gui_access1.jpg
        :scale: 85%


.. warning::
         Be sure you want to do this and that you are behind either a firewall appliance or another router.


Add Static Route (Double NAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This will look different depending on the other router that you might have and what IP range you use.

* A static route is needed on the other router in order for traffic to reach your FusionPBX installation and is only needed if the EdgerouterX is the double NAT.

Scenerio: Router A is the primary router that has a public IP address and a LAN subnet of 10.10.2.1. From this pool of IP addresses, the EdgerouterX gets IP 10.10.2.209. *Be sure that router A has DHCP reservation or the ability to make 10.10.2.209 a static IP*. 

* **Router A Router name:** This is a label for organizing.
* **Router A Destination IP address:** 192.168.1.38 This is the IP that the EdgerouterX gave to your FusionPBX install.
* **Router A Subnet mask:** 255.255.255.0 is the subnet mask used in this example.
* **Gateway:** 10.10.2.209 is the IP Router A gave to the EdgerouterX WAN eth0.
* **Interface:** LAN is a label on Router A to show it's a local area network address.

.. image:: ../../_static/images/firewall/fusionpbx_ubnt_static_route_other_router.jpg
        :scale: 85%


