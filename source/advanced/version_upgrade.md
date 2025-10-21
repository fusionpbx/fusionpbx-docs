# Version Upgrade

Version Upgrade can take several steps to perform. Below will show how   
to upgrade from specific versions.

<br>

## Upgrade from 5.4 to 5.5
---

### Pre-release instructions

This is a pre-release, and so these instructions can be changed up to the 5.5 release.

>

### Update source code, then run upgrade.php

>

Run the following commands when connected to your server over SSH.

```
cd /var/www/fusionpbx
git stash
git pull
git branch
git pull
```

**Upgrade Commands**
```
mkdir /var/run/fusionpbx
chown -R www-data:www-data /var/run/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php --schema
php /var/www/fusionpbx/core/upgrade/upgrade.php --defaults
php /var/www/fusionpbx/core/upgrade/upgrade.php --types
php /var/www/fusionpbx/core/upgrade/upgrade.php --optional
php /var/www/fusionpbx/core/upgrade/upgrade.php --permissions
php /var/www/fusionpbx/core/upgrade/upgrade.php --services
```

<br>

## Upgrade from 5.3 to 5.4
---

### Minimum Requirement PHP 7.1 or higher

You can check your version of PHP from Status -> System Status or the command line with the following command.
```nginx -t && nginx -s reload
php -v
```

>

### Update source code, then run upgrade.php

>

Run the following commands when connected to your server over SSH.

**Change to the 5.4 release**
```
cd /var/www/fusionpbx
git stash
git pull
git checkout 5.4
git branch
git pull
```

**Upgrade Commands**
```
mkdir /var/run/fusionpbx
chown -R www-data:www-data /var/run/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php --schema
php /var/www/fusionpbx/core/upgrade/upgrade.php --defaults
php /var/www/fusionpbx/core/upgrade/upgrade.php --permissions
php /var/www/fusionpbx/core/upgrade/upgrade.php --service
nginx -t && nginx -s reload
```

---

###Domains member feature.

The latest FusionPBX code requires a new version of the Domains member feature. If this member feature has been installed, then use the following command line to remove it.

These commands could be used to remove the app/domains feature.
```
rm -R /var/www/fusionpbx/app/domains
```

Use the application manager to re-install the domains member feature.

---

### Dialplan

The **user_record** dialplan has been updated to support call recordings in stereo.
- Go to Dialplan -> Dialplan Manager
- Add this **user_record** to the search.
- Press the SEARCH button
- Press the SHOW ALL button
- Use the Checkbox next to Domain to select all of the Dialplans 
- Then press the DELETE button.
- Go to Advanced -> Upgrade
- Put a checkmark in the App Defaults checkbox
- Press the EXECUTE button.
- Go to Status -> SIP Status
- Press the FLUSH CACHE button.

---

>

### Users

If the users list is empty at Accounts -> Users. A change was made to the user's database view. Upgrade App Defaults will update this view. If you have already run App Defaults or the upgrade.php commands above, then the list should work.

- Go to Advanced -> Upgrade
- Put a checkmark in the App Defaults checkbox
- Press the EXECUTE button.
- Go to Status -> SIP Status

---

### Websockets

Ensure the folder where the PID file is saved is owned by www-data using the command:
```
chown -R www-data:www-data /var/run/fusionpbx
```

This command will attempt to add websockets to the ssl 443 section of your nginx config file. If websockets will not connect (denoted by a red circle in the active call count), please use the manual update method below.
```
php /var/www/fusionpbx/core/upgrade/upgrade.php --service
```

To test the changes and apply them, run this command.
```
nginx -t && nginx -s reload
```

### **Update the Menu**

You can restore the Default Menu with the Restore Default button in Advanced -> Menu Manager. 

Or you can update the menu manually by using the following instructions to update the active calls path.

- Go to Advanced -> Menu Manager
- Edit the default menu
- Find Active Calls
- Click on Active Calls to edit its settings
- Change the link to 
```
/app/active_calls/active_calls.php
```
- Then press the SAVE button
- After this, press the RELOAD button or log out and back in.

---

>

---


### **Optional Manual Method**
Install the WebSocket services and NGINX settings. If you ran upgrade.php --service then in most cases you shouldn't need to do this.

**Configure NGINX**

**Manual**

Add the following to the 
```
nano /etc/nginx/sites-enabled/fusionpbx
```

Open the file and add this, find the section for 443, and just above dehydrated, add the following settings.

```
        #redirect websockets to port 8080
        location /websockets/ {
                 proxy_pass http://127.0.0.1:8080;
                 proxy_http_version 1.1;
                 proxy_set_header Upgrade $http_upgrade;
                 proxy_set_header Connection "upgrade";
                 proxy_set_header Host $host;
        }
```

Reload the NGINX config without restarting the service.
```
nginx -t && nginx -s reload
```
This commit shows you where to put this in the file.
- https://github.com/fusionpbx/fusionpbx-install.sh/commit/e25129c99aeb8164fe05ac04cbb52528608c9625

<br>

## Version 5.2 to 5.3

These instructions for upgrade are also relevant to versions of   
FusionPBX 5.2.0 and higher.

- Run (Install) Upgrades

```
    cd /var/www/fusionpbx
    git stash
    git pull
    git checkout 5.3
    git branch
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```
- Upgrade Schema -> Data Types
    - Navigate to the Upgrade page **Advanced** -> **Upgrade**.   
    - Select both **Schema** and **Data Types**, then click **Execute**.

- Restart Services

```
    systemctl restart email_queue
    systemctl restart fax_queue
    systemctl restart event_guard
```

### Update Dashboard

These instructions will update your dashboard to the new defaults.

-   Login to the web interface
-   From the dashboard press the **SETTINGS** button.
-   If you changed the groups assigned in the **Dashboard**,   
    print the page and save it to a PDF for reference later.
-   Select the first checkbox this will select all the ones below it.
-   Then press the **DELETE** button
-   Open the dropdown menu and navigate to **Advanced** -> **Upgrade**.
-   Select **App Defaults** then press  **Execute**.
-   In your browser press **ctrl + f5** to flush the browser cache.
-   If you need to customize the permission use the **SETTINGS** button and   
    update permissions.
    -   If you saved a PDF of previous changes use it to help assign the   
        groups to the Dashboard Widgets.

**background_color_enabled**

This is a new setting to enable or disable the background color. If you   
have a custom background image, then you may want to set this **value**   
to **false** and enabled to set it to true.

**Install Transcribe and Speech (Optional)**

```
    cd /var/www/fusionpbx/app
    git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
    git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
    chown -R www-data:www-data /var/www/fusionpbx
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```

Transcribe details need to be moved from the default settings category   
voicemail to transcribe. 

- **Openai** easy to setup enable setting and set the api_key
- **Watson** requires api_url in the transcribe category
- **Google** requires api_url
- **Azure** language en-US api_url used for the region

Speech is defined in the default settings category speech this feature   
is used for Text-to-Speech - Make sure to set enable the settings -   
openai - elevenlabs

<br>

## Version 5.1 to 5.2

These instructions for upgrade are also relevant to versions of   
FusionPBX 5.1.0 and higher.

:::{note}

When this upgrade.php is run from the root, it will   
write the /etc/fusionpbx/config.conf file by reading information from   
the database and config.php and config.lua.   
:::

- Run (Install) Upgrades

```
    cd /var/www/fusionpbx
    git stash
    git pull
    git checkout 5.2
    git branch
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```

- Upgrade Schema -> Data Types
    - Navigate to the Upgrade page **Advanced** -> **Upgrade**.   
    - Select **Data Types**, then click **Execute**.

- Restart Services

```
    systemctl restart email_queue
    systemctl restart fax_queue
    systemctl restart event_guard
```

:::{note}

If the fax_queue is not installed it will show an error.   
This is only a problem if you are using fax. If you are using fax then   
you will want to install the fax_queue service.   
:::

```
    cp /var/www/fusionpbx/app/fax_queue/resources/service/debian.service /etc/systemd/system/fax_queue.service
    systemctl enable fax_queue
    systemctl start fax_queue
    systemctl daemon-reload
```

**XML CDR Import**

- Open the file

```
    nano /etc/freeswitch/autoload_configs/xml_cdr.conf.xml
```

- Comment out the url parameter.

```
    <!-- the url to post to if blank web posting is disabled  -->
    <!--<param name="url" value="http://127.0.0.1/app/xml_cdr/xml_cdr_import.php"/>-->

    fs_cli -x 'reloadxml'
    fs_cli -x 'reload mod_xml_cdr'
```

- Install the xml_cdr Service

```
    - This service is optional. However it helps add the CDR records faster than the cron job that is [documented here](https://www.fusionpbx.com/app/pages/page.php?id=2291d3c8-c714-49a6-bfd9-3365885ae526)
    - Install the service
```

### Debian or Ubuntu

```
    cp /var/www/fusionpbx/app/xml_cdr/resources/service/debian.service /etc/systemd/system/xml_cdr.service
    systemctl enable xml_cdr
    systemctl start xml_cdr
    systemctl daemon-reload
```

### CentOS

```
    cp /var/www/fusionpbx/app/xml_cdr/resources/service/debian.service /usr/lib/systemd/system/xml_cdr.service
    systemctl daemon-reload
    systemctl enable xml_cdr
    systemctl start xml_cdr
```

**Menu Manager**

**Restore Default**

-   If the menu has not been customized then to update run the RESTORE   
    DEFAULT button.

**Manual Update**

To manually update the menu, you need to edit the default menu.

- Remove the **Email Logs** Menu (No longer used).
- Add the **Destination Summary** Menu
   - Title: Destination Summary Link: /app/destinations/destination_summary.php
   - Parent Menu: Status Groups: admin, superadmin

<br>

## Version 5.0 to 5.1

These instructions for upgrade are also relevant to versions of   
FusionPBX 5.0.3 to 5.0.10 and higher.

:::{note}

When this upgrade.php is run from the root, it will write the   
/etc/fusionpbx/config.conf file by reading information from the database   
and config.php and config.lua.   
:::

- Run (Install) Upgrades

```
    cd /var/www/fusionpbx
    git stash
    git pull
    git checkout 5.1
    git branch
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```

Make sure to also update group permission from Advanced -> Group
Manager -> RESTORE DEFAULT button

Navigate to the Upgrade page **Advanced** -> **Upgrade**.   
Select **Data Types**, then click **Execute**.

- Flush Templates

PHP Smarty version 4.3.1 was updated. This requires clearing files in   
the temp directory.

```
rm -R -f /tmp/\*.php
```

- New Global Dialplans

The following dialplans are need to be deleted for all domains. As these   
are now global dialplans.

call-direction is_local agent_status agent_status_id agent-status-break call_privacy
send_to_voicemail vmain xfer_vm vmain_user delay_echo echo is_zrtp_secure milliwatt
is_secure tone_stream hold_music do-not-disturb call-forward follow-me
freeswitch_conference clear_sip_auto_answer call_return dx att_xfer directory
redial call_return dx att_xfer is_transfer cf please_hold talking_clock_date

- Then run this command to get the new default global dialplans.

```
    cd /var/www/fusionpbx
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```

- Restart Services

```
    systemctl restart email_queue
    systemctl restart fax_queue
    systemctl restart event_guard
```

- Install the Event Guard Service
    - Upgrade to the latest FusionPBX 5.0.2 or higher.
    - Install the service

### Debian or Ubuntu

```
 cp   
 /var/www/fusionpbx/app/event_guard/resources/service/debian.service   
 /etc/systemd/system/event_guard.service systemctl   
 enable event_guard systemctl start event_guard   
 systemctl daemon-reload
```

### CentOS

```
 cp   
 /var/www/fusionpbx/app/event_guard/resources/service/debian.service   
 /usr/lib/systemd/system/event_guard.service systemctl
 daemon-reload systemctl enable event_guard systemctl start   
 event_guard
```

- Remove Old Config Files

The config.conf and config.php files are deprecated. These files were   
combined into the config.conf file.

```
    rm -f /etc/fusionpbx/config.php
    rm -f /etc/fusionpbx/config.lua
```

**Config File Ownership**

The /etc/fusionpbx/config.conf file should be owned by the root user    
like other files in the /etc directory.

### Debian / Ubuntu / CentOS

```
chown -R root:root /etc/fusionpbx
```

### FreeBSD

```
chown -R root:root /usr/local/etc/fusionpbx
```

**Destination Number**

For many years the inbound phone number (DID/DDI) would show up in the   
dialplan as **\*destination_number**\* variable for most VoIP providers.   

For some VoIP providers, the number would be found in   
**\*sip_to_user***, and in some cases,***sip_req_user**\* is needed.

Recently Diversion header has become more widely used, and sip   
**\*sip_to_user**\* and, in some cases, **\*sip_req_user**\* may be   
required. 

For example, a call forwarded from a mobile phone to one of   
your numbers in FusionPBX. The destination variable in the dialplan   
category can change which variable is used.

```
    Category: dialplan
    Subcategory: destination
    Type: text
    Value: destination_number
    Description: Options: destination_number (default), ${sip_to_user}, ${sip_req_user}
```

- Update Fail2ban, if Used

```
cd /usr/src/fusionpbx-install.sh/debian/resources git stash git pull
./fail2ban.sh
```

- Error Reporting in config.conf

The error reporting in the bottom of the config.conf was changed to look   
like this. If this is different then it should be updated to what is   
shown below.

- Use this command to look at the bottom of the config.conf file.

```
    cat /etc/fusionpbx/config.conf | grep error
```

**Old version**

```
    #error reporting hide show all errors except notices and warnings
    error.reporting = 'E_ALL ^ E_NOTICE ^ E_WARNING'
```

**New version**

#error reporting options: user,dev,all error.reporting = user

If its different then use nano, vi, vim or some other editor to update   
the error reporting.

```
    nano /etc/fusionpbx/config.conf
```

Confirm that the values have been updated using this command.

```
    cat /etc/fusionpbx/config.conf | grep error
```

- Clear the cache

```
    rm -f /var/cache/fusionpbx/*
```

## 4.4 to 5.0

- Switch branches

```
    mv /var/www/fusionpbx /var/www/fusionpbx-4.4
    cd /var/www && git clone https://github.com/fusionpbx/fusionpbx.git
    chown -R www-data:www-data /var/www/fusionpbx
```

- Update **Schema** under **Advanced** -> **Upgrade**, run this command if it fails.

```
    cd /var/www/fusionpbx
    php /var/www/fusionpbx/core/upgrade/upgrade.php
```

- Refresh the browser if there are issues then logout and then back in.
- Update the following Dialplans.

:::{note}

If you have made any changes, make notes before you delete them.   
So changes can be added back. For example, valet park could have custom   
music on hold or a custom timeout for the valet park.   
:::

```
    user_exists
    call-direction
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
    speed_dial
    call-forward-all
    call_screen
    call_forward_not_registered
    local_extension
    voicemail
```

- Update these Dialplans by first selecting and deleting their entries   
  from within the Dialplan Manager for all domains. Then, run Advanced   
  -> Upgrade -> App Defaults to retrieve the new versions of the   
  diaplans.

- If you have customized any provisioning templates makes sure to copy   
  them from /var/www/fusionpbx-4.4/resources/templates/provision and   
  copy them into the right vendor directory in   
  /var/www/fusionpbx/resources/templates/provision. I you haven't   
  customized the provisioning templates you can skip this step.   
- Update the language phrases. If you have added custom phrases be   
  careful here not the case for most people.

```
    rm -R -f /etc/freeswitch/lang
    rm -R -f /etc/freeswitch/languages
    cp -R /var/www/fusionpbx/resources/templates/conf/languages /etc/freeswitch
    chown -R www-data:www-data /etc/freeswitch
    fs_cli -x "reloadxml"
```

- New Follow Me does not use the extension dial string. Use the   
  following SQL command to remove the extension dial string.

```
    update v_follow_me set dial_string = null;
    update v_extensions set dial_string = null, follow_me_destinations = null where dial_string <> 'error/user_busy';
    update v_extensions set follow_me_enabled = 'true' where follow_me_uuid in (select follow_me_uuid from v_follow_me where follow_me_enabled = 'true');
    \q
    exit
```

- Rename the variables dialplan to domain-variables

```
    su postgres
    psql fusionpbx
    update v_dialplans set dialplan_name = 'domain-variables' where dialplan_name = 'variables';
    \q
    exit
```

- Duplication in Default Settings

Go to **Advanced** -> **Default Settings** after running App Defaults to check   
for any duplicates. If you see duplicates that are not type of array   
this may have been caused from older versions of FusionPBX before we   
started using a Preset ID for each Default Settings. 

If you hover over the setting it says then says Default this is the    
default setting with the correct ID. If it says custom this is a   
unique UUID. Make sure to delete only duplicates that say custom otherwise   
when you run App Defaults again it will put the default setting back with   
the correct preset UUID\>

### FAX Queue install

-   <https://docs.fusionpbx.com/en/latest/status/fax_queue.html>
-   Install as a service

```
    cp /var/www/fusionpbx/app/fax_queue/resources/service/debian.service /etc/systemd/system/fax_queue.service
    systemctl enable fax_queue
    systemctl start fax_queue
    systemctl daemon-reload
```

-   or run as a cron job

```
    crontab -e
    * * * * * cd /var/www/fusionpbx && php /var/www/fusionpbx/app/fax_queue/resources/job/fax_queue.php
```

### Email Queue install

-   <https://docs.fusionpbx.com/en/latest/status/email_queue.html>
-   Install as a service

```
    cp /var/www/fusionpbx/app/email_queue/resources/service/debian.service /etc/systemd/system/email_queue.service
    systemctl enable email_queue
    systemctl start email_queue
    systemctl daemon-reload
```

-   or run as a cron job

```
    crontab -e
    * * * * * cd /var/www/fusionpbx && /usr/bin/php /var/www/fusionpbx/app/email_queue/resources/service/email_queue.php
```

<br>

## Version 4.2 to 4.4

- Switch branches

```
    mv /var/www/fusionpbx /var/www/fusionpbx-4.2
    cd /var/www && git clone -b 4.4 https://github.com/fusionpbx/fusionpbx.git
    chown -R www-data:www-data /var/www/fusionpbx
```

:::{note}

Depending on when you installed the path /etc/fusionpbx might need   
created. A good way to tell is once you move the fusionpbx folder in   
step one and the FusionPBX is on a page with flags.   
:::

<br>

**Only** do this step if the folder doesn't already exist.

```
    mkdir -p /etc/fusionpbx

    mv /var/www/fusionpbx-4.2/resources/config.php /etc/fusionpbx
    chown -R www-data:www-data /etc/fusionpbx/
```

-   Then go to **Advanced** -> **Upgrade** and run **Source Code**, **Schema**,   
    **Menu Defaults** and **Permission Defaults**.

:::{note}

config.lua needs to be read and write by the webserver in order   
for advanced default settings to update config.lua with new path information.   
Make sure config.lua and config.php are in /etc/fuionpbx/ .   
And be sure to run this command.    
:::

```
chown -R www-<data:www-data> /etc/fusionpbx/
```

- Update the following Dialplans.

```
    user_exists
    user_record
    call_forward_all
    local_extension
```

-   Update these Dialplans by first selecting and deleting their entries   
    from within the **Dialplan Manager** for all domains. Then, navigate to   
    **Advanced** -> **Upgrade** and run **App Defaults** to retrieve the new   
    dialplan versions

-  In the menu go to **Status** -> **SIP Status**, then press **Flush Cache**.

-  Update old recordings set the record_name and   
    record_path].

```
    cd /usr/src
    wget https://raw.githubusercontent.com/fusionpbx/fusionpbx-scripts/master/upgrade/record_path.php
    php record_path.php
```

-   Resave all Call Center Queues to update each call center queue   
    dialplan. Then restart mod call center or FreeSWITCH.

Changes have been made in the **Email** section in **Advanced** -> **Default settings**

-   You will find duplicates with a blank value. The duplicates must be   
    updated with the existing info from the originals. These duplicates   
    are the new and correct settings. You'll have to update these blank   
    ones with the existing values (like smtp server info) to the new   
    default ones. Then delete the original ones.

-   Don't delete the blank entries. The code behind them are for   
    version 4.4+ and the original ones are not.

:::{note}

If you already deleted the blank ones, you'll have to delete the email   
section, run App Defaults under **Advanced** -> **Upgrade**. Then navigate   
back to **Advanced** -> **Default settings** and set the email section back up.   
:::

<br>

## Version 4.0 to 4.2

1.  Update **Source Code**. From the web interface go to the Menu ->
    **Advanced** -> **Upgrade** page. Check the source box and the press execute. If
    you see a red bar it indicates there was a git conflict and you will
    need to update from console instead. If you don't see the source box
    then you will need to update from the console.
    
```
    cd /var/www/fusionpbx
    git stash
    git pull
    chown -R www-data:www-data /var/www/fusionpbx
```

2.  If the page goes blank type in the url   
    <http://domain.com/logout.php> This should bring you back to the    
    login screen.

3. Udate Schema. Advanced -> Upgrade then run Schema.   
   <https://domain.com/core/upgrade/index.php>

5.  Check the box for App Defaults and run execute.   
6.  Check the box for Menu Defaults and run execute. This will update   
    the menu to the default menu. The menu should now look like this.

![image](../_static/images/fusionpbx_new_menu.jpg)

6.  Check the box for Permission Defaults and run execute. Permissions   
    are store in a session to get new permissions logout and back in.
7.  Goto **Dialplan** -> **Dialplan Manager** and delete   
    \"local_extension\". Then goto **Advanced** -> **Upgrade** and   
    run **App Defaults**. This will regenerate he new local_extension version.
9.  Go to Applications \> Conference profiles. Edit each profile and   
    replace \$\${hold_music} with   
    local_stream://default
10.  Goto Advanced \> Variables hold_music. Make sure it\'s   
    value is set as local_stream://default

```
    Check Applications > Music On Hold to see if music is listed properly.
    You should see in red default for the category and the kHz sub categories should be in blue.
    If not, do the following

    * Edit (Pencil icon on the right) the Category names to reflect default for 8, 16, 32, and 48kHz.
    * After you click the pencil icon choose at the bottom the domain for the rates and click save.
    * If the category is blank, you may have missed running Advanced > check box app defaults > execute or you may not have renamed autoload_configs/local_stream.conf.xml file to local_stream.conf.
    * For custom music on hold check the path for the domain name and set select for the domain name to match the domain used in the path.
```

10. Remove .xml from the end of the following file names.

```
    **Before**
    autoload_configs/callcenter.conf.xml
    autoload_configs/conference.conf.xml
    autoload_configs/local_stream.conf.xml

    **After**
    autoload_configs/callcenter.conf
    autoload_configs/conference.conf
    autoload_configs/local_stream.conf
```

11. Edit autoload_configs/lua.conf.xml adding \"languages\".
    Restart of FreeSWITCH is required.

```
    <param name="xml-handler-bindings" value="configuration,dialplan,directory,languages"/>
```

12. Update Time Conditions (Bug Fix).

```
    Goto Advanced > Upgrades page.  Check box Update Source, execute. 
    Goto Advanced > Default settings > Category > delete the category: time condition presets.
    Goto Advanced > Upgrade >  check box App Defaults, execute.
    Goto Advanced > Default settings. Click "Reload" at the top right. (This will get the new presets)
```

Next steps are for existing Time Conditions.

    Goto Apps > Time Conditions and edit the time conditions remove all holidays and hit save.
    Select the holidays over again.


:::{note}

Many of the provisioning templates were updated.   
If you use custom provisioning templates you should consider   
updating them with the new versions.   
:::

<br>

## Version 3.8 to 4.0

- Remove the comments from the script-directory in   
  **/usr/local/freeswitch/conf/autoload_configs/lua.conf.xml**

- If using the FreesWITCH package then remove \$\${base_dir} and   
  set the full path to the scripts directory.

```
    before:  <!--<param name="script-directory" value="$${base_dir}/scripts/?.lua"/>-->

    after:   <param name="script-directory" value="/usr/local/freeswitch/scripts/?.lua"/>
```

Rebooting FreeSWITCH is required for this to take effect.

<br>

## Version 3.6 to 3.8

:::{note}

Upgrading can get very complex. If the production system is   
critical or you are intimidated from these upgrade instructions you   
may want FusionPBX paid support at http://www.fusionpbx.com/support.php   
:::

A standard upgrade procedure should always be followed:

- Make a Backup
- Advanced -> Upgrade steps
- Update switch scripts
- Restart FreeSWITCH.

Beyond the standard upgrade procedure just described, the following will
also need to be performed:

    uncomment: <param name="script-directory" value="$${base_dir}/scripts/?.lua"/>
    in: /usr/local/freeswitch/conf/autoload_configs/lua.conf.xml 

Rebuild All Time Conditions after you edit a particular time condition, click the Dialplan button on the top right to see what was there originally.

Delete the following dialplans from each domain, then run Advanced -> Upgrade -> App Defaults.
If using XML handler for the dialplan, flush memcache.
If using dialplans XML on the file system, resave one of the dialplans to have FusionPBX rewrite the XML files.

Dialplan Changes:
user_exists: call_timeout variable was added.
extension-intercom: It has been renamed to page-extension.
eavesdrop: Change *[88][ext] to *[33][ext] so that it doesn’t conflict with page-extension at *[8][ext].
user_status: Has been renamed to agent_status.
page: Dialplan has been simplified.
valet_park_out: Changed regex variable from $1 to $2.
local_extension: Failure handler was added to support call forward on busy and no answer.
If using call center feature code *[22], edit each agent and add an agent ID and password (pin number).


Delete any dialplan with the features context. These have been moved into the dialplan domain contexts.

If using App -> XMPP, Content Manager, or Schema, they have been moved to dev -> branches -> apps directory. Need to pull files from there if you want to use any of them.

Single Tenant Systems
For single tenant systems, default context is no longer used by default.
Easiest way to update your system:
Go to Advanced -> Domains and edit your domain.
Copy your current domain name, then change the name to default and save the change.
Now edit the domain name again and paste your original domain name or IP address (whatever the domain originally was) and save the changes.
Go to Accounts -> Extensions and save one extension. (Not needed if using the XML handler)
Go to Dialplan Manager and save one of the dialplans. (Not needed if using the XML handler)
FAX Configuration
(May require adjusting the paths and web server user account to match your server; www-data is used in this example)

Delete all previous FAX dialplans.
Resave each fax server in the GUI.

Run the following commands:

```
cd /var/www/fusionpbx/app/fax
wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/fax_import.php
chown -R www-data:www-data fax_import.php
```

Log in to the GUI and use this path in your browser:
```
http://<domain-or-ip>/app/fax/fax_import.php
```

Then after you can remove the script.

```
rm /var/www/fusionpbx/app/fax/fax_import.php
```

Groups and Permissions

- If you go to Advanced Group Manager -\> And you see what looks like   
  duplicates of user, admin and superadmin groups then you need do the   
  following instructions.

- Remove permissions associated with all domain groups with names that   
  match default global groups\...

- Go to **Advanced** -> **SQL Query tool** and run the following.
```
    delete from v_group_permissions where domain_uuid is not null
       and (
           group_name = 'user'
           or group_name = 'admin'
           or group_name = 'superadmin'
           or group_name = 'agent'
           or group_name = 'public'
       )
```

- Remove all domain groups having the same names as the default global groups   
  (retains any custom domain groups)...
  
```
       delete from v_groups where
       domain_uuid is not null
       and (
           group_name = 'user'
           or group_name = 'admin'
           or group_name = 'superadmin'
           or group_name = 'agent'
           or group_name = 'public'
       )
```

  Empty the group_uuid field for any group user with a group_name value having
  the same name as the default global groups (retains user assignments to custom domain groups)...

```
       update v_group_users set group_uuid = null where
       group_name = 'user'
       or group_name = 'admin'
       or group_name = 'superadmin'
       or group_name = 'agent'
       or group_name = 'public'
```

- For group users with a null group_uuid, insert the
  group_uuid of the global group that matches the
  group_name value\...
  
- Run this code from **Advanced** -> **Command** -> **PHP Command**.

```
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
```

### Apps menu disappeared

- If your apps menu disappeared check that it wasn\'t set to protected
  in the menu manager.

- **Advanced** -> **Menu Manager**. If protected is true, it won't show up.

<br>

## Version 3.5 to 3.6

:::{note}

When running **Schema**   
If you see **ALTER TABLE v_xml_cdr ADD json json;** every time you run it, 
then you likely have an old version of Postgres. To fix this either
upgrade to the latest Postgres server or run the following
SQL statement from **Advanced** -> **SQL Query.**
:::

```
    ALTER TABLE v_xml_cdr ADD json text;
```

See <https://github.com/fusionpbx/fusionpbx/issues/655> for more details.

**Potential issue with call recording after upgrading/switch to latest 3.6 stable.**

- After upgrading to 3.6 stable from 3.5 dev I noticed that calls were
  no longer being recorded. This was due to the file extension being
  missing from the recording path. If this is happening to you it is an
  easy fix.

- Go to Advanced -\> variables -\> category default and add the variable
  record_ext and set it to either wav or mp3. Choosing mp3
  depends upon whether or not you have mod_shout installed and
  enabled.

<br>

## Version 3.4 to 3.5

- Gateways now use the gateway_uuid as the name that is used   
  when interacting with FreeSWITCH. 
  
- This script is needed to help change   
  the gateway names used in the outbound routes.

- You may need to remove the old gateway file names
  from the conf/sip_profiles/external directory.

```
    cd /var/www/fusionpbx
    wget http://fusionpbx.googlecode.com/svn/branches/dev/scripts/upgrade/gateway_uuid.php
    http://x.x.x.x/gateway_uuid.php
    rm gateway_uuid.php
```

- Go To **Advanced** -> **Default Settings** -> **Switch Category** -> **Sub
  Category** gateways change to sip_profiles.

  **Permissions Issues**

  (access denied errors)
- Due to changes which improve consistency throughout the product, some   
  Users have had problem with superadmin receiving "access denied"   
  errors after the upgrade.


- Go To **Advanced -\> Group Manager**,   
  on **superadmin** click **Permissions** and then **Restore Default**

:::{note}

You may need to execute this operation for each group.   
:::

 **Default Settings**
 
- In the **switch category change gateways to sip_profiles**

<br>

## Version 3.3 to 3.4

- Update the source as described on this page, menu manager **restore   
  default**, group manager edit a group **restore default**, **Advanced**   
  -> **Upgrade** and run **Schema**.

- FusionPBX 3.4 hunt groups have been deprecated. Use the following
  script run it only one time to move existing hunt groups to ring
  groups.

```
    cd /var/www/fusionpbx
    wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/hunt_group_export.php
    http://x.x.x.x/hunt_group_export.php
    rm -r hunt_group_export.php
```

- Ring groups were expanded to add ability to call external numbers and
  match other missing hunt group features. A new table was created to
  accomodate this.

```
    cd /var/www/fusionpbx
    wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/ring_group_extensions.php
    http://x.x.x.x/ring_group_extensions.php
    rm ring_group_extensions.php
```

<br>

## Version 3.2 to 3.3

- FreeSWITCH changed the syntax to connect to the database so numerous   
  LUA scripts had to be updated.

- If you customized any of the lua scripts make a backup of the FreeSWITCH   
  scripts directory.

- Then remove the contents of the **freeswitch/scripts directory** and then run   
  **Advanced** -> **Upgrade** and run **Schema** (which will detect the missing scripts   
  and replace them).

<br>

## Version 3.1.4 to 3.2

**Ubuntu/Debian**

```
    cd /var/www/fusionpbx
    git pull
    Advanced -> Upgrade Schema
```

**Menu**

- If you cant see the menu after upgrading try the following in your   
  browser replace x.x.x.x with your ip or domain name.

```
    x.x.x.x/core/menu/menu.php
    Edit the menu make sure the language is set to en-us.
    Press **Restore Default**
```

**Default settings**

```
    x.x.x.x/core/default_settings/default_settings.php
    category: language 
    type: code 
    value: en-us
```

**Email**

- Migrating email to the new FusionPBX native voicemail.

```
    wget https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade/voicemail_export.php
```

- Run from the browser it will take the voicemail data from the   
  FreeSWITCH database and copy the information into the FusionPBX   
  database.

```
    http://x.x.x.x/voicemail_export.php
```

- Remove the export file

```
    rm voicemail_export.php
```

**Call Forward / Follow Me**

- No longer using hunt groups. So the backend has changed so keep in
  mind that you need to reset call forward and follow me settings. They
  are still listed in **App** -> **Hunt Groups**.
  
- After updating the info
  in call forward/follow me, you should delete the hunt group.

<br>

## Version 2 to 3.0


- LESS than or EQUAL to revision 1877, use the migration tool.
  <https://github.com/fusionpbx/fusionpbx-scripts/tree/master/upgrade>
    - If greater than revision 1877, use latest.

:::{note}

When upgrading from previous versions, you may encounter the following issues:    
:::

- **Changes to your dial plan or extensions don\'t take effect**   
- Go to the **Advanced -\> Default Settings** page   
- Remove **\"/default\"** from the end of your dialplan and   
  extensions directories

**Missing menus**

- Go to <hxxps://yourdomain.com/core/menu/menu.php>
- Click the edit (e) button beside default
- Click the Restore Default button
- Check that all the entries in the list are accessible by the   
  appropriate groups

**Emails not being sent for voicemail or fax**

- Double check the SMTP settings on the **System** -> **Settings** page
- Save it, even if you haven't changed anything

### Release Revisions

-   r0001 is 1.0 release - 6 Nov 2009
-   r2523 is 3.0 release - 3 May 2012
-   r2585 is 3.0.4 release - 24 May 2012
-   r2757 is 3.1 release - 18 Aug 2012
-   r2777 is 3.1.1 release - 26 Aug 2012
-   r2827 is 3.1.2 release - 12 Sep 2012
-   r2897 is 3.1.3 release - 26 Sep 2012
-   r2907 is 3.1.4 release - 27 Sep 2012
-   r3694 is 3.2 release - 19 Jan 2013
-   r3978 is 3.3 release - 1 May 2013
-   r4605 is 3.4 release - 28 Sep 2013
-   r6747 is 3.6.1 release - 22 Aug 2014
-   r8481 is 3.8.3 release - 11 May 2014
-   r793d386 is 4.0 release - Aug 2015
-   r4fdb6e9 is 4.1 release - Dec 2015
-   rxxxxxxx is 4.2 release - xxx 2016

<br>

## SQLite

SQLite is the FreeSWITCH default. Databases are located in the
freeswitch/db directory.

<br>

## ODBC

<http://wiki.freeswitch.org/wiki/ODBC>

<br>

## Postgres

Postgres native support will be in FreeSWITCH 1.2.4 but has been
available in the Main GIT branch.

<br>

## Dependencies

libpq and the associated dev packages are required

<br>

## Configure

To enable PostgresSQL as a native client in FreeSWITCH you must enable
it during the build when running configure. \*\* ./configure
\--enable-core-pgsql-support \*\*

<br>

## switch.conf.xml

Under the Settings area insert the following line

```
     \<param name=\"core-db-dsn\" value=\"pgsql;hostaddr=127.0.0.1
     dbname=freeswitch user=freeswitch password=\'\' options=\'-c
     client_min_messages=NOTICE\'
     application_name=\'freeswitch\'\" /\>
```
