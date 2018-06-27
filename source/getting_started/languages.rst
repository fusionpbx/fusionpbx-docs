***************
Languages
***************

FusionPBX has multilingual capabilities.  This will allow for different languages to be used in your FusionPBX installation.  Languages can be set globally, per tenant and per user. In addition to your FusionPBX installation web interface, there are options to upload audio files for FreeSWITCH to use via command line.

Fusionpbx Settings
^^^^^^^^^^^^^^^^^^^


Global
--------

**Advanced > Default Settings**

Setting the language from here will set the language for the entire FusionPBX installation.

.. image:: ../_static/images/getting_started/fusionpbx_global_language.jpg
        :scale: 85%



Domain (Tenant)
-------------------

**Advanced > Domains** then click the plus at the bottom right and fill in the required fields.

Setting the language from here will set the language for the entire domain (tenant) in your FusionPBX installation. This can override the Global language settings.

.. image:: ../_static/images/getting_started/fusionpbx_domain_language.jpg
        :scale: 85%



User
------

**Accounts > Users** then edit the user.

Setting the language from here will set the language for this specific user and will override Global and Domain language settings.

.. image:: ../_static/images/getting_started/fusionpbx_user_language.jpg
        :scale: 85%



FreeSWITCH Sound Files  
^^^^^^^^^^^^^^^^^^^^^^^

FreeSWITCH sound files location are dependent on operating system and installation method.

**Package Install**
-----------------------

* Most if not all recent installations of FusionPBX are using packages for FreeSWITCH.

* **File system location:** 

::

 /usr/share/freeswitch/sounds/en/us/

**Source Install**
--------------------

* Older installs, custom installs, or personal preference are using source compiled versions.

* **File system location:**

::

 /usr/local/freeswitch/sounds/en/us/


**Where to get language sounds**
----------------------------------


* **Free:** https://freeswitch.org/stash/projects/FS/repos/freeswitch-sounds/browse

