#############
Fail2ban
#############


Fail2ban is also used to protect SSH, FreeSWITCH, the web server as well as other services.

After the installation script finishes, the option for anything to register to the ip address is **ENABLED**. 

* If you plan on registering devices to the FusionPBX ip address then no further action is required. 

It is however recomended to register to a domain name (FQDN) since most scripted attacks happen to the public ip. Registering to the ip address will be blocked by the fail2ban rules freeswitch-ip and auth-challenge once these rules are set to true.

* To help secure your FusionPBX installation, enable the `fail2ban rules <http://docs.fusionpbx.com/en/latest/firewall/fail2ban.html>`_ [freeswitch-ip] and [auth-challenge-ip] in /etc/fail2ban/jail.local.


::

 [freeswitch-ip]
 enabled  = true

::

 [auth-challenge-ip]
 enabled  = true 

.. warning::

         If you find that your FusionPBX web interface isn't loading then check and see if fail2ban is blocking your ip.  Getting blocked by any fail2ban rule will block ssh, www, and phones registering if you don't have your ip in the /etc/fail2ban/jail.conf ignoreip= field .

You can view the IP addresses blocked by Fail2ban with the following command.


::
 
 iptables -L -n
 

To check the status of one of the fail2ban jails

::

 fail2ban-client status freeswitch-ip


Fail2ban configuration files are located in.

::

 cd /etc/fail2ban/


To exclude an IP so that it isn't blocked by any filters edit the **jails.conf** file.


::

 nano /etc/fail2ban/jail.conf


Find ignoreip and add the IP address, CIDR or DNS hostname that need to be white listed. Use a space as a delimitter between each one. Restart fail2ban to apply the changes to the ignoreip list.

::

 ignoreip = 127.0.0.1/8 192.168.0.0/16


.. note::
       To help keep the ip and hostnames you want unblocked it is a good idea to add customers and carriers to the ignoreip list.



Filters are defined in the following directory.

::

 /etc/fail2ban/filter.d


Inside jail.local points to filters and defines maxretry, bantime, logpath, ports to block and more.

::

 /etc/fail2ban/jail.local


Clear all blocked addresses by restarting fail2ban.

::

  service fail2ban restart


Fail2ban logs the addresses that it blocks with the filter that triggered it.

::

  /var/log/fail2ban.log


More information about Fail2ban can be found at http://www.fail2ban.org/wiki


.. Note::

    You can use a dynamic ip address service like dyndns to whitelist a dynamic ip address.


