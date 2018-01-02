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

[--uid myUser --pwd myPass]http://mydomain.com/app/provision/?mac=$MA



HTTPS
=======

Requires a Cisco Certificate.



Auto Delivery of the URL
============================

Use the DHCP Option 66 to deliver the provisioning URL to the phones without using the web interface.
