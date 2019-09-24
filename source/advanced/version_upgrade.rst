#################
Version Upgrade
#################

Version Upgrade can take several steps to perform. Below will show how to upgrade from specific versions.

4.4 to Master (what will become 4.6)
^^^^^^^^^^^^^^^^^^

1. Switch branches

::

 mv /var/www/fusionpbx /var/www/fusionpbx-4.4
 cd /var/www && git clone https://github.com/fusionpbx/fusionpbx.git
 chown -R www-data:www-data /var/www/fusionpbx

2. Try Advanced -> Upgrade Schema if that fails use the the command line.

::

 cd /var/www/fusionpbx
 php /var/www/fusionpbx/core/upgrade/upgrade.php

3. Refresh the browser if there are issues then logout and then back in.

4. Update the following Dialplans.

If you have made any changes to these make notes on the changes before you delete them. So that the changes could be added back. For example valet park could have custom music on hold or a custom timeout for the valet park.

::

 user_exists
 is_loopback
 is_local
 user_record
 agent_status
 group_intercept
 extension-to-voicemail
 vmain
 vmain_user
 tone_stream
 recordings
 valet_park
 call_screen
 call_forward_not_registered
 local_extension
 voicemail

- Update these Dialplans by first selecting and deleting their entries from within the Dialplan Manager for all domains. Then, run Advanced -> Upgrade -> App Defaults to retrieve the new versions of the diaplans.

5. If you have customized any provisioning templates makes sure to copy them from /var/www/fusionpbx-4.4/resources/templates/provision and copy them into the right vendor directory in /var/www/fusionpbx/resources/templates/provision. I you haven't customized the provisioning templates you can skip this step.


Version 4.2 to 4.4
^^^^^^^^^^^^^^^^^^

1. Switch branches

::

 mv /var/www/fusionpbx /var/www/fusionpbx-4.2
 cd /var/www && git clone -b 4.4 https://github.com/fusionpbx/fusionpbx.git
 chown -R www-data:www-data /var/www/fusionpbx

.. note::
       Depending on when you installed the path /etc/fusionpbx might need created.  A good way to tell is once you move the fusionpbx folder in step one and the FusionPBX is on a page with flags.
   
::

 **Only** do this step if the folder **doesn't** already exist.

 mkdir -p /etc/fusionpbx

 mv /var/www/fusionpbx-4.2/resources/config.php /etc/fusionpbx
 chown -R www-data:www-data /etc/fusionpbx/
 
- Then go to Advanced -> Upgrade and update the Source Code, Schema, Menu Defaults and Permission Defaults.

.. note::

 config.lua needs to be read and write by the webserver in order for advanced > default settings to update config.lua with new path information. Make sure config.lua and config.php are in /etc/fuionpbx/ . Don't miss this step chown -R www-data:www-data /etc/fusionpbx/ 

2. Update the following Dialplans.

::

 user_exists
 user_record
 call_forward_all
 local_extension

- Update these Dialplans by first selecting and deleting their entries from within the Dialplan Manager for all domains. Then, run Advanced -> Upgrade -> App Defaults to retrieve the new versions of the diaplans.

3. In the menu go to Status then SIP Status and press 'Flush Cache'.

4. Update old recordings set the record_name and record_path.

::

 cd /usr/src
 wget https://raw.githubusercontent.com/fusionpbx/fusionpbx-scripts/master/upgrade/record_path.php
 php record_path.php
 
5. Resave all Call Center Queues to update each call center queue dialplan. Then restart mod call center or FreeSWITCH.

6. Advanced > Default Settings

The email section in Advanced > Default settings, changes have been made.

*  You will find duplicates with a blank value.  The duplicates must be updated with the existing info from the originals. These duplicates are the new and correct settings.  You'll have to update these blank ones with the existing values (like smtp server info) to the new default ones.  Then delete the original ones.

*  Don't delete the blank entries.  The code behind them are for version 4.4+ and the original ones are not.

.. note::

 If you already deleted the blank ones, you'll have to delete the email section then run Advanced > Upgrade > App Defaults check box.  Then go back to Advanced > Default settings and set the email section back up.


Version 4.0 to 4.2
^^^^^^^^^^^^^^^^^^

1. Update the source code. 
From the web interface go to the Menu -> Advanced > Upgrade page. Check the source box and the press execute. If you see a red bar it indicates there was a git conflict and you will need to update from console instead. If you don't see the source box then you will need to update from the console.

::

 cd /var/www/fusionpbx
 git stash
 git pull
 chown -R www-data:www-data /var/www/fusionpbx

2. If the page goes blank type in the url http://domain.com/logout.php  This should bring you back to the login screen.  


3. Udate the Schema. Advanced -> Upgrade Check the Schema box and then then press execute.
https://domain.com/core/upgrade/index.php


4. Check the box for App Defaults and run execute.


5. Check the box for Menu Defaults and run execute. This will update the menu to the default menu. The menu should now look like this.


.. image:: ../_static/images/fusionpbx_new_menu.jpg
        :scale: 85%


6. Check the box for Permission Defaults and run execute. Permissions are store in a session to get new permissions logout and back in.


7. Goto Dialplan > Dialplan Manager and delete "local_extension".  Then goto Advanced > Upgrade and only check box App Defaults and click execute. This will regenerate the new local_extension version.


8. Go to Applications > Conference profiles. Edit each profile and replace $${hold_music} with local_stream://default


9. Goto Advanced > Variables hold_music. Make sure it's value is set as local_stream://default

::

 Check Applications > Music On Hold to see if music is listed properly.
 You should see in red default for the category and the kHz sub categories should be in blue.
 If not, do the following
 
 * Edit (Pencil icon on the right) the Category names to reflect default for 8, 16, 32, and 48kHz.
 * After you click the pencil icon choose at the bottom the domain for the rates and click save.
 * If the category is blank, you may have missed running Advanced > check box app defaults > execute or you may not have renamed autoload_configs/local_stream.conf.xml file to local_stream.conf.
 * For custom music on hold check the path for the domain name and set select for the domain name to match the domain used in the path.


10. Remove .xml from the end of the following file names

::

 **Before**
 autoload_configs/callcenter.conf.xml
 autoload_configs/conference.conf.xml
 autoload_configs/local_stream.conf.xml


::

 **After**
 autoload_configs/callcenter.conf
 autoload_configs/conference.conf
 autoload_configs/local_stream.conf


11. Edit autoload_configs/lua.conf.xml adding "languages". Restart of FreeSWITCH is required.

::

 <param name="xml-handler-bindings" value="configuration,dialplan,directory,languages"/>


12. Update Time Conditions (Bug Fix)
 
::
 
 Goto Advanced > Upgrades page.  Check box Update Source, execute. 
 Goto Advanced > Default settings > Category > delete the category: time condition presets.
 Goto Advanced > Upgrade >  check box App Defaults, execute.
 Goto Advanced > Default settings. Click "Reload" at the top right. (This will get the new presets)

Next steps are for existing Time Conditions

::

 Goto Apps > Time Conditions and edit the time conditions remove all holidays and hit save.
 Select the holidays over again.


.. note::

  Many of the provisioning templates were updated.  If you use custom provisioning templates you should consider updating them with the new versions. 


Version 3.8 to 4.0
^^^^^^^^^^^^^^^^^^


Remove the comments from the script-directory in **/usr/local/freeswitch/conf/autoload_configs/lua.conf.xml**

If using the FreesWITCH package then remove $${base_dir} and set the full path to the scripts directory. 


::
 
 before:  <!--<param name="script-directory" value="$${base_dir}/scripts/?.lua"/>-->
   
 after:   <param name="script-directory" value="/usr/local/freeswitch/scripts/?.lua"/>

Rebooting FreeSWITCH is required for this to take effect.


Version 3.6 to 3.8
^^^^^^^^^^^^^^^^^^


| **Note: Upgrading can get very complex. If the production system is critical or you are intimidated from these upgrade instructions you may want FusionPBX paid support at http://www.fusionpbx.com/support.php**

| A standard 'upgrade' procedure should always be followed:
| (1. Make a Backup!, 2. Advanced > Upgrade steps, 3. Update switch scripts, 4. Restart FreeSWITCH).

Beyond the standard upgrade procedure just described, the following will also need to be performed:

::

 uncomment: <param name="script-directory" value="$${base_dir}/scripts/?.lua"/>
 in: /usr/local/freeswitch/conf/autoload_configs/lua.conf.xml 


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

