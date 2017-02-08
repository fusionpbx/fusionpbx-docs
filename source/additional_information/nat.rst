#####
Network Address Translation
#####

NAT is Network Address Translation. When your FusionPBX and/or FreeSWITCH are inside NAT then then you may experience one way audio or no audio in either direction the following information can help you get audio working in both directions.


Default config
^^^^^^^^^^^^^^^
The external_rtp_ip and external_sip_ip are set to $${local_ip_v4} in Advanced -> Variables by default.

* This works good when the server has a public IP address.
* Also works good when all phones are inside the same network.
* The local_ip_v4 variable auto detects the IP address and sets it. This works well for systems that are inside NAT but using a SIP to TDM gateway. 


SIP ALG
^^^^^^^^^^^^^^^
A SIP Application Layer Gateway is a tool designed to help SIP traverse NAT. While the SIP ALG is good in theory it is often causes more problems than it solves because of this its usually best to disable the SIP ALG on your firewall. An alternative way to disable it is to move SIP to a non standard port.


Static IP
^^^^^^^^^^^^^^^
FusionPBX is behind NAT and you have a static public IP address.

* autonat:xxx.xxx.xxx.xxx


UPnP or PMP
^^^^^^^^^^^^^^^
FusionPBX is behind NAT and you don't have a static ip address. You do have a firewall that is capable of UPnP or PMP.

* Enable UPnP or PMP in your firewall
* In Debian OS /etc/default/freeswitch  remove -nonat
* Make systemd aware of the changes.  systemctl daemon-reload
* Set external_rtp_ip and external_sip_ip to auto-nat in Advanced -> Variables.
* Restart FreeSWITCH.   service freeswitch restart





.. _FreeSWITCH documented infomation on NAT: https://freeswitch.org/confluence/dosearchsite.action?queryString=nat
