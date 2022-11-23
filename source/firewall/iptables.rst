*****************
Iptables
*****************

Iptables are used in the Debian install script.

Basic Rules
^^^^^^^^^^^^

| ``iptables -A INPUT -i lo -j ACCEPT``
| ``iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 22 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 80 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 443 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 5060:5069 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 5060:5069 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 5080 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 5080 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 16384:32768 -j ACCEPT``
| ``iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 1194 -j ACCEPT``
| ``iptables -P INPUT DROP``
| ``iptables -P FORWARD DROP``
| ``iptables -P OUTPUT ACCEPT``

Optional Rules
^^^^^^^^^^^^^^^^

| OPENVPN: ``iptables -A INPUT -p udp --dport 1194 -j ACCEPT`` 
| ICMP: ``iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT``

Friendly Scanner
^^^^^^^^^^^^^^^^^^

Rules to block not so friendly scanner

| ``iptables -I INPUT -j DROP -p tcp --dport 5060 -m string --string "friendly-scanner" --algo bm``
| ``iptables -I INPUT -j DROP -p tcp --dport 5080 -m string --string "friendly-scanner" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5060 -m string --string "friendly-scanner" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5080 -m string --string "friendly-scanner" --algo bm``

| *Optional*


| ``iptables -I INPUT -j DROP -p tcp --dport 5060 -m string --string "VaxSIPUserAgent" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5060 -m string --string "VaxIPUserAgent" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5080 -m string --string "VaxSIPUserAgent" --algo bm``
| ``iptables -I INPUT -j DROP -p tcp --dport 5080 -m string --string "VaxIPUserAgent" --algo bm``

| ``iptables -I INPUT -j DROP -p tcp --dport 5060 -m string --string "VaxSIPUserAgent/3.1" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5060 -m string --string "VaxSIPUserAgent/3.1" --algo bm``
| ``iptables -I INPUT -j DROP -p udp --dport 5080 -m string --string "VaxSIPUserAgent/3.1" --algo bm``
| ``iptables -I INPUT -j DROP -p tcp --dport 5080 -m string --string "VaxSIPUserAgent/3.1" --algo bm``


Add DSCP rules
^^^^^^^^^^^^^^
iptables -t mangle -A OUTPUT -p udp -m udp --sport 16384:32768 -j DSCP --set-dscp 46
iptables -t mangle -A OUTPUT -p udp -m udp --sport 5060:5091 -j DSCP --set-dscp 26
iptables -t mangle -A OUTPUT -p tcp -m tcp --sport 5060:5091 -j DSCP --set-dscp 26


Show iptable rules
^^^^^^^^^^^^^^^^^^^

``sudo iptables -L -v``

Show line numbers
^^^^^^^^^^^^^^^^^^

``iptables -L -v -n --line-numbers``

Show DSCP rules
^^^^^^^^^^^^^^^
iptables -vL -t mangle


Delete a line
^^^^^^^^^^^^^^

Delete line 2

``iptables -D INPUT 2``

Flush Out Iptables
^^^^^^^^^^^^^^^^^^^

| ``iptables -P INPUT ACCEPT``
| ``iptables -P FORWARD ACCEPT``
| ``iptables -P OUTPUT ACCEPT``
| ``iptables -F``

Open a Port for a Specific IP Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| ``iptables -A INPUT -j ACCEPT -p tcp --dport 5432 -s x.x.x.x/32``

Block IP address
^^^^^^^^^^^^^^^^^

| ``iptables -I INPUT -s 62.210.245.132 -j DROP``

Restore Rules from rules.v4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This reads the file rules.v4 and saved iptables rules back into active memory.
| ``iptables-restore < /etc/iptables/rules.v4``

Flush iptables
^^^^^^^^^^^^^^^^^
How to flush iptables without loosing access to ssh.

| ``iptables -P INPUT ACCEPT``
| ``iptables -F``

Save Changes
^^^^^^^^^^^^^

Debian / Ubuntu

| ``apt-get install iptables-persistent``
| ``service iptables-persistent save``
| ``dpkg-reconfigure iptables-persistent``
| ``iptables-save > /etc/iptables/rules.v4``
| ``ip6tables-save > /etc/iptables/rules.v6``
