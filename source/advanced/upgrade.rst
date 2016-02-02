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

| * Rebuild all time conditions. 
| *After you edit a particular time condition, click the Dialplan button on the top right to see what was there originally. 
| * Delete the following dialplans from each domain then run Advanced -> Upgrade -> App Defaults. If using XML handler for the dialplan flush memcache. If using dialplans XML on the file system resave one of the dialplans to have FusionPBX rewrite the XML files. 
| * user_exists - call_timeout variable was added
| * extension-intercom - It has been renamed to 'page-extension'
| * eavesdrop - Change *88[ext] to *33[ext] so that it doesn't conflict with page-extension at *8[ext] 
| * user_status - Has been renamed to 'agent_status'
| * page - Dialplan has been simplified.
| * valet_park_out - Changed regex variable from $1 to $2
| * local_extension - failure handler was added to support call forward on busy and no answer
| * If using call center feature code *22 edit each agent and add an agent id and password (pin number)
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
|LESS than or EQUAL to revision 1877, use the migration tool. https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade
|If greater than revision 1877, use latest. 

::



|

