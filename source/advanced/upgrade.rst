##########
Upgrade
##########


The FusionPBX code is constantly evolving. Bug fixes being submitted, additions to improve security, making FusionPBX look nicer, to be more flexible, and best of all new features. A complete summary of the changes can be found on the github code page https://github.com/fusionpbx/fusionpbx/commits/master .  Initially google code svn was the place to download code from but since that has closed github is where the code now lives.  

|

Maintenance Upgrade
--------------------

|
A Maintenance Upgrade can be done daily depending on development activity.  This is typically for bug fixes, added features, security patches or small version upgrades.

|
.. image:: ../_static/images/fusionpbx_upgrade.jpg
        :scale: 85%



Version Upgrade
------------------

|

Version Upgrade can take several steps to perform. Below will show how to upgrade from specific versions.

Release Revisions

* r0001 is 1.0 release - 6 Nov 2009
* r2523 is 3.0 release - 3 May 2012
* r2585 is 3.0.4 release - 24 May 2012
* r2757 is 3.1 release - 18 Aug 2012
* r2777 is 3.1.1 release - 26 Aug 2012
* r2827 is 3.1.2 release - 12 Sep 2012
* r2897 is 3.1.3 release - 26 Sep 2012
* r2907 is 3.1.4 release - 27 Sep 2012
* r3694 is 3.2 release - 19 Jan 2013
* r3978 is 3.3 release - 1 May 2013
* r4605 is 3.4 release - 28 Sep 2013
* r6747 is 3.6.1 release - 22 Aug 2014
* r8481 is 3.8.3 release - 11 May 2014
* r793d386 is 4.0 release - Aug 2015
* r4fdb6e9 is 4.1 release - Dec 2015

|
Version 4.0 to 4.1
^^^^^^^^^^^^^^^^^^

|

|

Version 3.8 to 4.0
^^^^^^^^^^^^^^^^^^

|
Remove the comments from the script-directory in **/usr/local/freeswitch/conf/autoload_configs/lua.conf.xml**

If using the FreesWITCH package then remove $${base_dir} and set the full path to the scripts directory. 
|

::
 
 before:  <!--<param name="script-directory" value="$${base_dir}/scripts/?.lua"/>-->
   
 after:   <param name="script-directory" value="/usr/local/freeswitch/scripts/?.lua"/>

Rebooting FreeSWITCH is required for this to take effect.

|

Version 3.6 to 3.8
^^^^^^^^^^^^^^^^^^

|
**Note: Upgrading can get very complex. If the production system is critical or you are intimidated from these upgrade instructions you may want FusionPBX paid support at http://www.fusionpbx.com/support.php**

|A standard 'upgrade' procedure should always be followed:
|(1. Make a Backup!, 2. Advanced > Upgrade steps, 3. Update switch scripts, 4. Restart FreeSWITCH).

Beyond the standard upgrade procedure just described, the following will also need to be performed:

::

 uncomment: <param name="script-directory" value="$${base_dir}/scripts/?.lua"/>
 in: /usr/local/freeswitch/conf/autoload_configs/lua.conf.xml 
|

Version 3.5 to 3.6
^^^^^^^^^^^^^^^^^^

|

|

Version 3.4 to 3.5
^^^^^^^^^^^^^^^^^^

|

|

Version 3.3 to 3.4
^^^^^^^^^^^^^^^^^^

|

|

Version 3.2 to 3.3
^^^^^^^^^^^^^^^^^^

|

|

Version 3.1.4 to 3.2
^^^^^^^^^^^^^^^^^^^^

|

|

Version 2 to 3.0
^^^^^^^^^^^^^^^^

|
|LESS than or EQUAL to revision 1877, use the migration tool. https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade
|If greater than revision 1877, use latest. 

::



|

