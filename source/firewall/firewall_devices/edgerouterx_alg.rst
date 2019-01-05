##############################
Ubiquiti EdgerouterX SIP ALG
##############################

In some scenerios you may have to turn off SIP ALG.  




Check if SIP ALG is running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Command:** lsmod | grep sip



 
::
 
  shwim@ubnt:~$ lsmod | grep sip
  nf_nat_sip              8853  0
  nf_conntrack_sip       21773  1 nf_nat_sip
  nf_nat                 13284  10 nf_nat_ftp,nf_nat_sip,ipt_MASQUERADE,nf_nat_proto_gre,nf_nat_h323,nf_nat_ipv4,nf_nat_pptp,nf_nat_tftp,xt_nat,iptable_nat
  nf_conntrack           62604  18 nf_nat_ftp,nf_nat_sip,xt_CT,nf_conntrack_proto_gre,ipt_MASQUERADE,nf_nat,nf_nat_h323,nf_nat_ipv4,nf_nat_pptp,nf_nat_tftp,xt_conntrack,nf_conntrack_ftp,nf_conntrack_sip,iptable_nat,nf_conntrack_h323,nf_conntrack_ipv4,nf_conntrack_pptp,nf_conntrack_tftp
  shwim@ubnt:~$

 
This shows that SIP ALG is running in the example above.


Disable SIP ALG
^^^^^^^^^^^^^^^^^

To disable SIP ALG:

* Either click on the CLI button from the Ubiquiti EdgerouterX GUI or via you favorite SSH client to the EdgerouterX.
* **Then type:** configure
* **Then type:** set system conntrack modules sip disable
* **Then type:** commit
* **Then type:** save
* **Then type:** exit

::

 root@ubnt:/home/shwim# configure
 [edit]
 root@ubnt# set system conntrack modules sip disable
 [edit]
 root@ubnt# commit
 [edit]
 root@ubnt# save
 Saving configuration to '/config/config.boot'...
 Done
 [edit]
 root@ubnt# exit

Enable SIP ALG
^^^^^^^^^^^^^^^^^

To enable SIP ALG:

* Either click on the CLI button from the Ubiquiti EdgerouterX GUI or via you favorite SSH client to the EdgerouterX.
* **Then type:** configure
* **Then type:** set system conntrack modules sip enable-indirect-media
* **Then type:** set system conntrack modules sip enable-indirect-signalling
* **Then type:** commit
* **Then type:** save
* **Then type:** exit

::

 root@ubnt:/home/shwim# configure
 [edit]
 root@ubnt# set system conntrack modules sip enable-indirect-media
 [edit]
 root@ubnt# set system conntrack modules sip enable-indirect-signalling
 [edit]
 root@ubnt# commit
 [edit]
 root@ubnt# save
 Saving configuration to '/config/config.boot'...
 Done
 [edit]
 root@ubnt# exit

.. note::

   set system conntrack modules sip port <1-65535> will change the sip port number  

