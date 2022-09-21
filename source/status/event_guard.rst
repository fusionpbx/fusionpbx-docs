########
Event Guard
########

This is an optional service called event_guard and it was designed to protect your VoIP server. It watches registration events and blocks those that abuse it. It doesn't watch server logs. It currently supports iptables and pf firewalls. Netfilter firwall support will be added in the future.

Event guard logs blocked and unblocked calls to Status -> Event Guard. Event guard uses the Advanced -> Access Control allowed nodes as a white list. I n addition to this it also looks at current allowed IP addresses and trusts these registered IP addresses.

Install Instructions
^^^^^^^^^^^^^^^^^^^^

- Make sure to upgrade to the latest FusionPBX version
- Update the database structure

  - Advanced -> Upgrade -> Schema
  
- Update App Defaults

  - Advanced -> Upgrade -> App Defaults
  
* Run the following commands to install as a service

::

 cp /var/www/fusionpbx/app/event_guard/resources/service/debian.service /etc/systemd/system/event_guard.service
 systemctl enable event_guard
 systemctl start event_guard
 systemctl daemon-reload


- or as a cron job

 php /var/www/fusionpbx/app/event_guard/resources/service/event_guard.php >/dev/null 2>&1 &

::


Unblock an IP Address
^^^^^^^^^^^^^^^^^^^^

To unblock an address select the check box and then press the UNBLOCK button on the top right.
