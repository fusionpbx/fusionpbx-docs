#####
Network Address Translation
#####

NAT is Network Address Translation. When your FusionPBX and/or FreeSWITCH are inside NAT then then you may experience one way audio or no audio in either direction the following information can help you get audio working in both directions.


Default config
^^^^^^^^^^^^^^^
The external_rtp_ip and external_sip_ip are set to $${local_ip_v4} in Advanced -> Variables by default. The local_ip_v4 variable is auto detected by FreeSWITCH. The variable can be also be overidden as a preset variable before it is used if you want to control the IP address that it represents.

* This works good when the server has a public IP address.
* It also works well when all phones are inside the same network and nothing needs to traverse the NAT. For example if you are using a SIP to TDM gateway and all your phones are in the same network.


SIP ALG
^^^^^^^^^^^^^^^
A SIP Application Layer Gateway (ALG) is a tool designed to help SIP traverse NAT. While the SIP ALG is good in theory it often causes more problems than it solves. Because of this it's usually best to disable the SIP ALG on your firewall. An alternative way to disable it is to move SIP to a non standard port.


Static IP
^^^^^^^^^^^^^^^
FusionPBX is behind NAT and you have a static public IP address and you have phones on the same network and/or outside the network.

* Set external_rtp_ip to autonat:xxx.xxx.xxx.xxx
* Set external_sip_ip to autonat:xxx.xxx.xxx.xxx
* If you don't register a gateway to the carrier you may need to port forward SIP and RTP.


UPnP or PMP
^^^^^^^^^^^^^^^
FusionPBX is behind NAT and you don't have a static ip address. You do have a firewall that is capable of UPnP or PMP.

* Enable UPnP or PMP in your firewall
* In Debian OS /etc/default/freeswitch  remove -nonat
* Make systemd aware of the changes.  systemctl daemon-reload
* Set external_rtp_ip to auto-nat
* Set external_sip_ip to auto-nat
* Restart FreeSWITCH.   service freeswitch restart

