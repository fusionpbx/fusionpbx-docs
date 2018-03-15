########
Cisco SPA
########

The following information can be used to provisioning Cisco SPA phones.



Basic URL
===========
An example URL for provisioning URL for a Cisco SPA.

http://mydomain.com/app/provision/?mac=$MA



HTTP Authentication
=====================
Phone web interface -> Provision - > Profile Rule

::

[--uid myUser --pwd myPass]http://mydomain.com/app/provision/?mac=$MA



HTTPS
=======
Requires a Cisco Certificate that you will likely need to obtain from a Cisco distributor.


Browser Command
=================
Use your web browser to send the following command to pass the provision the phone now and this will pass URL to the phone so it has the location neeeded for provisioning the device. In this example 192.168.1.5 is the IP address of the phone and domain.com needs updated to use the correct tenant domain name.


**No HTTP Authentication**

::

http://192.168.1.5/admin/resync?http://domain.com/app/provision/?mac=$MA


**With HTTP Authentication**

::

http://192.168.1.4/admin/resync?%5B--uid+admin+--pwd+555%5Dhttp://domain.com/app/provision/?mac=$MA



DHCP Option
=============
Use the DHCP Option 66 to deliver the provisioning URL to the phones without using the web interface.

Additional Information
=======================
More information can also be found at https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/csbpvga/spa100-200/provisioning/guide/SPA100-200_Provisioning.pdf

