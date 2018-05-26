###################
Default Settings
###################


Settings used for all domains.  Branding can be done in this section and also adjust or copy settings to specific domains.


.. image:: ../_static/images/advanced/fusionpbx_advanced_default_settings.jpg
        :scale: 85%



Default Settings have several different categories.


Adminer
^^^^^^^^^

FusionPBX version 4.2+ has Adminer disabled by default.  To use Adminer, you must enable this option with True. 

+--------------+----------------------------------------------------------------------------+
|auto_login    |  Set whether to auto-login to Adminer, or require a username and password. |
+--------------+----------------------------------------------------------------------------+

Cache
^^^^^^^

Option to use file cache for xml and not memcache.

+--------------+-------+----------------------------------+
|location      |  /tmp | Location for the file cache.     |
+--------------+-------+----------------------------------+
|method        |  file | Cache methods file and memcache. |
+--------------+-------+----------------------------------+

Call Center
^^^^^^^^^^^^^

Defaults for the amount of agent rows for Call Center.

+------------------+----+
| agent_add_rows   |  5 |
+------------------+----+
| agent_edit_rows  |  1 |
+------------------+----+


CDR
^^^^^


Dashboard
^^^^^^^^^^^





Destinations
^^^^^^^^^^^^^^^



Domain
^^^^^^^



Editor
^^^^^^^^



Email
^^^^^^^



Fax
^^^^^^^



Follow Me
^^^^^^^^^^



Ivr Menu
^^^^^^^^^^


Limit
^^^^^^^


Login
^^^^^^^


`Provision <http://docs.fusionpbx.com/en/latest/advanced/default_settings/provision.html>`_
^^^^^^^^^^^

In the Provisioning section, there are a few key options that have to be set in order to turn auto provisioning on.

* **enabled** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default.
* **http_auth_username** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default. Be sure to use a strong username.
* **http_auth_password** Must be enabled and set to **value true** and **enabled True**.  It is disabled by default. Be sure to use a strong password.

Recordings
^^^^^^^^^^^



Ring Group
^^^^^^^^^^^^


Security
^^^^^^^^^^



Server
^^^^^^^^




Switch
^^^^^^^^


Theme
^^^^^^^



Time Conditions
^^^^^^^^^^^^^^^^


User
^^^^^


Voicemail
^^^^^^^^^^^



