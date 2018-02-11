#############
Fail2ban
#############


Fail2ban is also used to protect SSH, FreeSWITCH, the web server as well as other services. You can view the IP addresses blocked by Fail2ban with the following command.


::
 
 iptables -L
 

To check the status of one of the fail2ban jails

::

 fail2ban-client status freeswitch-ip-tcp
 
Then will show

::

` Status for the jail: freeswitch-ip-tcp
` |- filter
` |  |- File list:        /usr/local/freeswitch/log/freeswitch.log
` |  |- Currently failed: 0
` |  `- Total failed:     4
` `- action
`  |- Currently banned: 3
`  |  `- IP list:       207.38.90.177 51.15.145.32 207.38.90.197
`   `- Total banned:     3

To exclude an ip so that it isn't blocked by any filters edit the **jails.conf** file.

::

 nano /etc/fail2ban/jail.conf


Find ignoreip = and place domain.tld or 000.000.000.000

::

 ignoreip = domain.tld or 000.000.000.000
 

More about whitelisting can be found at http://www.fail2ban.org/wiki/index.php/Whitelist


Note::

    You can use a dynamic ip address like dyndns to whitelist a dynamic ip address.


