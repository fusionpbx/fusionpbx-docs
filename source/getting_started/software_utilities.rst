********************
Software Utilities
********************

There are several software utilities one can use to troubleshoot voip issues and guage quality.  Below are a list of some of the common ones.

Packet Capture
----------------

`tcpdump <https://www.tcpdump.org/>`_
^^^^^^^^

Install
~~~~~~~~~

::

 apt-get install tcpdump

**Command**

::

 tcpdump -nq -s 0 -A -vvv -i eth0 port 5060

.. tip::

      you can change the command to suite the proper ethernet device eth0 with what is on your system.  Port 5060 can be changed also if you are using a different port.

`sngrep <../additional_information/sngrep.html>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since March 2017 Sngrep is installed on all systems by default.  This is a very useful tool to help troubleshoot all types of sip related issues.

If you installed FusionPBX prior to March 2017 you can still manually install sngrep.

Manual Install
~~~~~~~~~~~~~~~

From your FusionPBX install SSH window or console window

::

 cd /usr/src
 git clone https://github.com/fusionpbx/fusionpbx-install.sh.git
 cd /usr/src/fusionpbx-install.sh/debian/resources/
 ./sngrep.sh

**Command**

::

 sngrep


**sngrep:** https://github.com/irontec/sngrep




Call Quality and Monitoring
-----------------------------

Call quality can be a nuisance in the voip world.  Having a way to track and make reports is a very needed tool.

`Homer <https://github.com/sipcapture/homer/wiki/Examples%3A-FreeSwitch>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Homer is well known to help track and graph quality issues with SIP, like utilizing QoS Reports.

Quote:

      *HOMER is a robust, carrier-grade, scalable SIP Capture system and VoiP Monitoring Application offering HEP/EEP, IP Proto4 (IPIP) encapsulation & port mirroring/monitoring support right out of the box, ready to process & store insane amounts of signaling, logs and statistics with instant search, end-to-end analysis and drill-down capabilities for ITSPs, VoIP Providers and Trunk Suppliers using SIP signaling protocol.*


To install and configure Homer visit https://github.com/sipcapture/homer

