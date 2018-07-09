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

`Sngrep <https://github.com/irontec/sngrep>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since March 2017 Sngrep is installed on all systems by default.  This is a very useful tool to help troubleshoot all types of sip related issues.

If you installed FusionPBX prior to March 2017 you can still manually install Sngrep.

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


