##########
Upgrade
##########


The FusionPBX code is constantly evolving. Bug fixes being submitted, additions to improve security, making FusionPBX look nicer, to be more flexible, and best of all new features. A complete summary of the changes can be found on the github code page https://github.com/fusionpbx/fusionpbx/commits/master .  Initially google code svn was the place to download code from but since that has closed github is where the code now lives.  

|

Maintenance Upgrade
####################


| A Maintenance Upgrade can be done daily depending on development activity.  This is typically for bug fixes, added features, security patches or small version upgrades.


.. image:: ../_static/images/fusionpbx_upgrade.jpg
        :scale: 85%

|

| **Update the source from command line**

::

 * cd /var/www/fusionpbx 
 git pull
 chown -R www-data:www-data *


| **Back to the GUI**

::

 *Upgrade Database with advanced -> upgrade schema
 *Update permissions
 *Update the menu
 *Logout and back in


How to Upgrade
##############

.. image:: ../_static/images/fusionpbx_upgrade_green.jpg
        :scale: 100%

|

| To upgrade you will need to get the latest source code. Depending on how extreme the changes have been or the version you currently are on since your last update, you may need to follow version specific upgrade instructions to bring your install up to date.


**Step 1: Update FusionPBX Source**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| 1. GUI -> Advanced -> Upgrade (doesn't update all files)

Used to update FusionPBX to the latest release.

**Upgrade the code via Github/GIT**

| Login into the web interface with a user account assigned to the superadmin group.
| Login to the console with either the ssh, the locally.
| Backup It's a good idea to make a backup. If using sqlite, your backup will easily include the SQL database.
 
::

 mkdir /etc/fusionpbx
 mv /var/www/fusionpbx/resources/config.php /etc/fusionpbx
 mv /usr/local/freeswitch/scripts/resources/config.lua /etc/fusionpbx
 cd /var/www
 cp -R fusionpbx fusionpbx_backup
 Change the directory''' to the FusionPBX directory
 cd /var/www/fusionpbx

**Update the source code** (example assumes fusionpbx is in /var/www/fusionpbx)
 
::

 cd /var/www/fusionpbx
 git pull
 
| **Permissions**
| Reset the permissions on the fusionpbx directory tree. When you do **git pull** it sets the permissions on any updated files to match the account that you are running **git pull** with. If that account is different to the web server account it will result in some files no longer being accessible and a red bar error at the top of the upgrade screen on the GUI.  To fix this you should reapply the permissions in fusionpbx and recursively in all directories inside it.
|
| The example assumes the web server runs as user 'www-data' and fusionpbx is installed to /var/www/fusionpbx. (chown -Rv Ownername:GroupName /var/www/fusionpbx)

::

 cd /var/www/fusionpbx
 chown -R www-data:www-data *


**Step 2: Update Freeswitch Scripts**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| NOTE: As of FusionPBX 3.8.3 (Stable Branch), the scripts should be automatically updated when updating the Source Code, using the **Advanced > Upgrade** page. Any customized scripts, having the same name as the default scripts, **will be overwritten.** (An option to disable this default behavior is available using **Default Setting: switch > scripts_update > false**) Missing scripts will be restored, and any additional files within the scripts folder will remain untouched.


| FusionPBX is a fast moving project where features are constantly being added and bugs are being fixed on a daily basis so I would also suggest upgrading the Freeswitch scripts directory as part of any normal upgrade process.

**Update Freeswitch** 

| Use github to get the updated files. **You have to do this from an empty directory**.
 
::

 cp -R /usr/local/freeswitch/scripts /usr/local/freeswitch/scripts-bak
 rm -Rf /usr/local/freeswitch/scripts/
 cd /usr/src
 git clone https://github.com/fusionpbx/fusionpbx.git
 cp -R /var/www/fusionpbx/resources/install/scripts /usr/local/freeswitch
 chown -R www-data:www-data /usr/local/freeswitch/scripts
 cp -R /usr/local/freeswitch/scripts-bak/resources/config.lua /usr/local/freeswitch/scripts/resources/config.lua

(The last step above is not required if your config.lua file is being stored in a different location, such as the /etc/fusionpbx folder.)

| **Clean out this scripts directory**
| An alternative is to remove the Lua scripts. **Only do this if you haven't customized any LUA scripts**

::

 cp -R /usr/local/freeswitch/scripts /usr/local/freeswitch/scripts-bak
 rm -rf /usr/local/freeswitch/scripts/*


| **Pull the most recent scripts down**

| Here you need to go directly to step 3 and make sure you run upgrade schema from the GUI immediately otherwise your calls will not complete.

| **Restore the config.lua file (IMPORTANT!!)**

| If your config.lua file was located in scripts/resources/, then you'll need to restore it (from the backup previously performed) to scripts/resources/config.lua.

**Step 3: Upgrade Schema**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Many updates have changes to the database and to the Freeswitch scripts. The upgrade_schema script 

| **Upgrade from the GUI** 

| From the GUI, run **Advanced -> Upgrade Schema** which will add any needed newer tables or columns.
| Then run **App Defaults**. *If you removed the scripts on Step 2 then run this* **twice**.

.. image:: ../_static/images/fusionpbx_upgrade_schema_data_types.jpg
        :scale: 85%

|

| **Upgrade from the Command Line**
| An alternative to running upgrade_schema.php from the GUI is to run the upgrade.php from the command line. It was designed to make the upgrade easier. If you did not login when updating the FusionPBX source code then you will need to run the upgrade.php file from the command line. Make sure to use the full path to the PHP file.

| As root run the following
 
::
 
 cd /var/www/fusionpbx
 /usr/bin/php /var/www/fusionpbx/core/upgrade/upgrade.php

| If your screen was nicely formatted with a fusionpbx theme, and suddenly now goes to a black and white screen with familiar text but no theme, it is because you were using a theme which no longer exists in the latest version of the code.  If this happens to you navigate to:

::

 http://domain_or_ip/mod/users/usersupdate.php
 
| Then scroll down to where it says **"Template"** and select one of the valid templates from the drop down list.  Then press Save.  It will be fixed now and you can continue with the remaining steps below.
| (Note that any users who have invalid templates selected will also have the same problem you did. You can fix them from the user manager option in the accounts menu)

**Step 4: Apply permissions and Restart Freeswitch**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| **Make sure that the freeswitch directory has the correct permissions**

::

 chown -Rv www-data:www-data /usr/local/freeswitch/

| **Restart Freeswitch**

::

 systemctl restart freeswitch

**Step 5: Menu**
^^^^^^^^^^^^^^^^^

| Needed if your menu disappeared.
| **v1 and v2**
| Now update the menu to the latest version.

::

 http://domain_or_ip/core/menu/menu_restore_default.php


| Press 'Restore Default' on the top right.
| **v3**
| https://your.ip/core/menu/menu.php
| click 'e' next to the default menu
| click the restore default button.
| https://your.ip/logout.php
| https://your.ip/login.php

**Step 6: Re-generate Settings**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Sometimes variable names changes. In rev 1877 **v_config_cli.php** variable names changed which caused no fax to email emails or voicemail emails to be sent. Problem was the SMTP details did not exist.

| Go to **Advanced -> Settings** and then **click save**. This will re-generate v_config_cli.php and any other needs config files.




Version Upgrade
################

|

Version Upgrade can take several steps to perform. Below will show how to upgrade from specific versions.

|

Version 4.0 to 4.2
^^^^^^^^^^^^^^^^^^

1. Update code from the GUI. Advanced > Upgrade page (Only check this box then click execute)


.. note::
 
  If you get a red bar error at the top when trying to upgrade you will need SSH access to the install and run these commands.


::

 cd /var/www/freeswitch
 git stash
 git pull
 chown -R www-data:www-data *
 
2. Check box Schema (Only check this box then click execute)

|

3. You will notice a big difference in the menu. (Logo can be placed above the menu also)

.. image:: ../_static/images/fusionpbx_new_menu.jpg
        :scale: 85%

|

4. Check box Default Settings. (Only check this box then click execute)

|

5. If the page goes blank type in the url http://domain.tld/logout.php  This should bring you back to the login screen. Login.

|

6. Goto Dialplan > Dialplan Manager and delete "local_extension".  Then goto Advanced > Upgrade and only check box App Defaults and click execute. This will regenerate the new local_extension version.

|

7. Goto Applications > Conference profiles. Edit each profile and replace $${hold_music} with local_stream://default

|

8. Goto Advanced > Variables hold_music. Make sure it's value is set as local_stream://default

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


| **Note: Upgrading can get very complex. If the production system is critical or you are intimidated from these upgrade instructions you may want FusionPBX paid support at http://www.fusionpbx.com/support.php**

| A standard 'upgrade' procedure should always be followed:
| (1. Make a Backup!, 2. Advanced > Upgrade steps, 3. Update switch scripts, 4. Restart FreeSWITCH).

Beyond the standard upgrade procedure just described, the following will also need to be performed:

::

 uncomment: <param name="script-directory" value="$${base_dir}/scripts/?.lua"/>
 in: /usr/local/freeswitch/conf/autoload_configs/lua.conf.xml 

|

| * Rebuild all time conditions. 
| * After you edit a particular time condition, click the Dialplan button on the top right to see what was there originally. 
| * Delete the following dialplans from each domain then run Advanced -> Upgrade -> App Defaults. If using XML handler for the dialplan flush memcache. If using dialplans XML on the file system resave one of the dialplans to have FusionPBX rewrite the XML files. 
| * user_exists - call_timeout variable was added
| * extension-intercom - It has been renamed to 'page-extension'
| * eavesdrop - Change '*'88[ext] to '*'33[ext] so that it doesn't conflict with page-extension at '*'8[ext] 
| * user_status - Has been renamed to 'agent_status'
| * page - Dialplan has been simplified.
| * valet_park_out - Changed regex variable from $1 to $2
| * local_extension - failure handler was added to support call forward on busy and no answer
| * If using call center feature code '*'22 edit each agent and add an agent id and password (pin number)
| * Delete any dialplan with the 'features' context. These have been moved into the dialplan domain contexts.
| * If using App -> XMPP, Content Manager, or Schema they have been moved dev -> branches -> apps directory need to pull files from there if you want to use any of them.
| * For single tenant systems 'default' context is no longer used by default. 
| * Easiest way to update your system is go to Advanced -> Domains and edit your domain.
| * Copy your current domain name then change the name to default then save the change.
| * Now edit the domain name again and paste your original domain name or IP address whatever the domain originally was and save the changes
| * Go to accounts extensions and save one extension. (not needed if using the XML handler)
| * Go to Dialplan Manager and save one of the dialplans. (not needed if using the XML handler)
| * FAX ( may require adjusting the paths and web server user account to match your server 'www-data' is used in this example)
| * Delete all previous FAX dialplans
| * Resave each fax server in the GUI.
| * cd /var/www/fusionpbx/app/fax
| * wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/fax_import.php
| * chown -R www-data:www-data fax_import.php
| * Login into the GUI and use this path in your browser http://<domain-or-ip>/app/fax/fax_import.php
| * rm /var/www/fusionpbx/app/fax/fax_import.php
| * Groups and Permissions
| If you go to Advanced Group Manager -> And you see what looks like duplicates of user, admin and superadmin groups then you need do the following instructions.

|

| Remove permissions associated with all domain groups with names that match default global groups...

| Use the **Advanced -> SQL Query tool** to do the following.

::

 delete from v_group_permissions where domain_uuid is not null
    and (
        group_name = 'user'
        or group_name = 'admin'
        or group_name = 'superadmin'
        or group_name = 'agent'
        or group_name = 'public'
    )

 Remove all domain groups having the same names as the default global groups
 (retains any custom domain groups)...

    delete from v_groups where
    domain_uuid is not null
    and (
        group_name = 'user'
        or group_name = 'admin'
        or group_name = 'superadmin'
        or group_name = 'agent'
        or group_name = 'public'
    )

 Empty the group_uuid field for any group user with a group_name value having
 the same name as the default global groups (retains user assignments to custom domain groups)...

    update v_group_users set group_uuid = null where
    group_name = 'user'
    or group_name = 'admin'
    or group_name = 'superadmin'
    or group_name = 'agent'
    or group_name = 'public'
 
|
| For group users with a null group_uuid, insert the group_uuid of the global group that matches the group_name value...
| Run this code from **Advanced -> Command -> PHP Command.**

::

 $sql = "select group_user_uuid, group_name ";
    $sql .= "from v_group_users where group_uuid is null";
    $prep_statement = $db->prepare(check_sql($sql));
    $prep_statement->execute();
    $result = $prep_statement->fetchAll(PDO::FETCH_NAMED);
    $result_count = count($result);
    unset($prep_statement);
    if ($result_count > 0) {
        foreach($result as $field) {
            //note group user uuid
                $group_user_uuid = $field['group_user_uuid'];
                $group_name = $field['group_name'];
            //get global group uuid
                $sql = "select group_uuid from v_groups ";
                $sql .= "where domain_uuid is null ";
                $sql .= "and group_name = '".$group_name."' ";
                $prep_statement = $db->prepare($sql);
                $prep_statement->execute();
                $sub_result = $prep_statement->fetch(PDO::FETCH_ASSOC);
                $sub_result_count = count($sub_result);
                unset ($prep_statement);
            //set group uuid
                if ($sub_result_count > 0) {
                    $sql = "update v_group_users ";
                    $sql .= "set group_uuid = '".$sub_result['group_uuid']."' ";
                    $sql .= "where group_user_uuid = '".$group_user_uuid."' ";
                    $count = $db->exec(check_sql($sql));
                    unset($sql);
                }
        }
    }

|
| **Apps menu disappeared**

| If your apps menu disappeared check that it wasn't set to protected in the menu manager.
| **(advanced -> menu manager)**. If protected is true, it won't show up.

 
Version 3.5 to 3.6
^^^^^^^^^^^^^^^^^^

|
| When running **Upgrade -> Schema**
| If you see **ALTER TABLE v_xml_cdr ADD json json;** every time you run the upgrade schema then you likely have an old version of Postgres. To fix this either upgrade to the latest Postgres server or run the following **SQL statement from advanced -> sql query.**

::

 ALTER TABLE v_xml_cdr ADD json text;


| See https://github.com/fusionpbx/fusionpbx/issues/655 for more details.
|

| **Potential issue with call recording after upgrading/switch to latest 3.6 stable.**

| After upgrading to 3.6 stable from 3.5 dev I noticed that calls were no longer being recorded. This was due to the file extension being missing from the recording path. If this is happening to you it is an easy fix.

| Go to Advanced -> variables -> category default and add the variable record_ext and set it to either wav or mp3. Choosing mp3 depends upon whether or not you have mod_shout installed and enabled.

Version 3.4 to 3.5
^^^^^^^^^^^^^^^^^^

|
| Gateways now use the gateway_uuid as the name that is used when interacting with FreeSWITCH. This script is needed to help change the gateway names used in the outbound routes. You may need to remove the old gateway file names from the conf/sip_profiles/external directory.

::

 cd /var/www/fusionpbx
 wget http://fusionpbx.googlecode.com/svn/branches/dev/scripts/upgrade/gateway_uuid.php
 http://x.x.x.x/gateway_uuid.php
 rm gateway_uuid.php

| * Go To **Advanced -> Default Settings -> Switch Category -> Sub category gateways change to sip_profiles**

| **Permissions Issues** - (access denied errors)
| Due to changes which improve consistency throughout the product, some Users have had problem with superadmin receiving "access denied" errors after the upgrade.   

|

| * Go To **Advanced -> Group Manager**
| * On **superadmin** click **Permissions** and then **Restore Default**

|

| You may need to execute this operation for each group.

| **Default Settings**'
| In the **switch category change gateways to sip_profiles**

|

Version 3.3 to 3.4
^^^^^^^^^^^^^^^^^^

|

| Update the source as described on this page, menu manager **restore default**, group manager edit a group **restore default**, advanced -> upgrade schema.

|

| FusionPBX 3.4 hunt groups have been deprecated. Use the following script run it only one time to move existing hunt groups to ring groups.

::

 cd /var/www/fusionpbx
 wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/hunt_group_export.php
 http://x.x.x.x/hunt_group_export.php
 rm -r hunt_group_export.php

|

| Ring groups were expanded to add ability to call external numbers and match other missing hunt group features. A new table was created to accomodate this.

::

 cd /var/www/fusionpbx
 wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/ring_group_extensions.php
 http://x.x.x.x/ring_group_extensions.php
 rm ring_group_extensions.php

|

Version 3.2 to 3.3
^^^^^^^^^^^^^^^^^^

|
| FreeSWITCH changed the syntax to connect to the database so numerous LUA scripts had to be updated. If you customized any of the lua scripts make a backup of the FreeSWITCH scripts directory. Then remove the contents of the **freeswitch/scripts directory** and then run **advanced -> upgrade schema** (which will detect the missing scripts and replace them).
|

Version 3.1.4 to 3.2
^^^^^^^^^^^^^^^^^^^^

|
| Ubuntu/Debian

::

 cd /var/www/fusionpbx
 git pull
 Advanced -> Upgrade Schema

| **Menu**

| If you cant see the menu after upgrading try the following in your browser replace x.x.x.x with your ip or domain name.
 
::

 x.x.x.x/core/menu/menu.php
 Edit the menu make sure the language is set to en-us.
 Press **Restore Default**

| **Default settings**

::

 x.x.x.x/core/default_settings/default_settings.php
 category: language 
 type: code 
 value: en-us

| **Email**

Migrating email to the new FusionPBX native voicemail.

::

 wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/voicemail_export.php


| Run from the browser it will take the voicemail data from the FreeSWITCH database and copy the information into the FusionPBX database.

::

 http://x.x.x.x/voicemail_export.php

Remove the export file

::

 rm voicemail_export.php


| **Call Forward / Follow Me**

| No longer using hunt groups. So the backend has changed so keep in mind that you need to reset call forward and follow me settings. They are still listed in **app -> hunt groups**. After updating the info in call forward, follow me you should delete the hunt group.
|

Version 2 to 3.0
^^^^^^^^^^^^^^^^

|
| LESS than or EQUAL to revision 1877, use the migration tool. https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade
| If greater than revision 1877, use latest. 

::

| When upgrading from previous versions, you may encounter the following issues:

| **Changes to your dial plan or extensions don't take effect**
| * Go to the **Advanced -> Default Settings** page
| * Remove **"/default"** from the end of your dialplan and extensions directories

|

| **Missing menus**
| * Go to hxxps://yourdomain.com/core/menu/menu.php
| * Click the edit (e) button beside default
| * Click the Restore Default button
| * Check that all the entries in the list are accessible by the appropriate groups

| **Emails not being sent for voicemail or fax**
| * Double check the SMTP settings on the System -> Settings page
| * Save it, even if you haven't changed anything

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
* rxxxxxxx is 4.2 release - xxx 2016

|

SQLite
^^^^^^

SQLite is the FreeSWITCH default. Databases are located in the freeswitch/db directory.

ODBC
^^^^^

http://wiki.freeswitch.org/wiki/ODBC

Postgres
^^^^^^^^^

Postgres native support will be in FreeSWITCH 1.2.4 but has been available in the Main GIT branch.

Dependencies
^^^^^^^^^^^^^

libpq and the associated dev packages are required

Configure
^^^^^^^^^^

To enable PostgresSQL as a native client in FreeSWITCH you must enable it during the build when running configure.
** ./configure --enable-core-pgsql-support **

switch.conf.xml
^^^^^^^^^^^^^^^^^

Under the Settings area insert the following line

 <param name="core-db-dsn" value="pgsql;hostaddr=127.0.0.1 dbname=freeswitch user=freeswitch password='' options='-c client_min_messages=NOTICE' application_name='freeswitch'" />

Additional Information
^^^^^^^^^^^^^^^^^^^^^^^^

http://wiki.freeswitch.org/wiki/PostgreSQL_in_the_core
