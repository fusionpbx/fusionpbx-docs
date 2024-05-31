*****************
Iptables
*****************

|

After The install is complete please keep the login details from the install in a safe and secure place.  Just in case you need them later.

iptables
===========

Basic Rules
===========

| ``iptables -A INPUT -i lo -j ACCEPT``
| ``iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 22 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 80 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 443 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 5060 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 5060 -j ACCEPT``
| ``iptables -A INPUT -p tcp --dport 5080 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 5080 -j ACCEPT``
| ``iptables -A INPUT -p udp --dport 16384:32768 -j ACCEPT``
| ``iptables -P INPUT DROP``
| ``iptables -P FORWARD DROP``
| ``iptables -P OUTPUT ACCEPT``

Optional Rules
===============

| OPENVPN: ``iptables -A INPUT -p udp --dport 1194 -j ACCEPT`` 
| SYSLOG: ``iptables -A INPUT -p udp --dport 514 -j ACCEPT`` 
| ICMP: ``iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT``

Friendly Scanner
================

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


Show iptable rules
==================

``iptables -L -v``

Show line numbers
=================

``iptables -L -n -v --line-numbers``

Delete a line
=============

Delete line 2

``iptables -D INPUT 2``

Clear iptables rules
================

| ``iptables -P INPUT ACCEPT``
| ``iptables -F``
| ``iptables -X``

Block IP address
================

``iptables -I INPUT -s 62.210.245.132 -j DROP``

Save Changes
============

Debian / Ubuntu

| ``iptables-save > /etc/iptables/rules.v4``

or

| ``apt-get install iptables-persistent``
| ``service iptables-persistent save``
| ``dpkg-reconfigure iptables-persistent``

Iptables Configuration
======================

Debian / Ubuntu

| ``cd /etc/iptables``

Activate rules.v4 file changes
==============================

| ``iptables-restore < /etc/iptables/rules.v4``
