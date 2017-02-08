#####
NAT
#####

NAT is Network Address Translation.  When problems happen with VOIP the usual suspect is NAT.

Freeswitch NAT
^^^^^^^^^^^^^^^

`FreeSWITCH documented infomation on NAT`_

NAT Example: If you have a static ip.

* autonat:xxx.xxx.xxx.xxx  (for the static ip)


NAT Example: FreeSWITCH is behind a firewall

* If using UPnP or PMP on the firewall
* Some routers you would need to disable or enable (usually disable) SIP ALG

* In Debian OS /etc/default/freeswitch  remove -nonat
* Set external rtp and sip ip to auto-nat in advanced -> variables

If server is **not** behind NAT then default config works





.. _FreeSWITCH documented infomation on NAT: https://freeswitch.org/confluence/dosearchsite.action?queryString=nat
