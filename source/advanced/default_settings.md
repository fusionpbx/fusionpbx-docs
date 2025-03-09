# Default Settings

Default Settings used for all domains. Branding can be done in this section, [see here to adjust](../advanced/domains.html#override-a-default-setting-for-one-domain) or copy settings to specific domains.

![FusionPBX Advanced Default Settings](../_static/images/advanced/fusionpbx_advanced_default_settings.jpg)

Default Settings have several different categories. Click on the category to view more details.

## [Cache](default_settings/cache.html)

Option to use file cache for XML and not memcache.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description     |
|-----------------------------|----------------------|-----------------------|-------------------------|---------------------------------|
| method                      | text                 | memcache              | TRUE                    | Cache methods file or memcache. |
| location                    | text                 | /tmp                  | TRUE                    | Location for the file cache.    |

## [Call Center](default_settings/call_center.html)

FusionPBX menu [Apps > Call Center](../applications/call_center.html)

Defaults for the amount of agent rows for Call Center.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description    |
|-----------------------------|----------------------|-----------------------|-------------------------|--------------------------------|
| agent_add_rows              | numeric              | 5                     | TRUE                    | Number of default "add" rows.  |
| agent_edit_rows             | numeric              | 1                     | TRUE                    | Number of default "edit" rows. |

## [CDR](default_settings/cdr.html)

FusionPBX menu [Apps > CDR](../applications/call_detail_record.html)

CDR Stat hour limit, call leg, format, limit, http_enabled, archive database, and storage type settings can be set here.

| Default Setting Subcategory   | Default Setting Name   | Default Setting Value   | Default Setting Enabled   | Default Setting Description          |
|-------------------------------|------------------------|-------------------------|---------------------------|--------------------------------------|
| stat_hours_limit              | numeric                | 24                      | FALSE                     |                                      |
| b_leg                         | array                  | outbound                | FALSE                     |                                      |
| b_leg                         | array                  | inbound                 | FALSE                     |                                      |
| b_leg                         | array                  | local                   | FALSE                     |                                      |
| format                        | text                   | json                    | TRUE                      |                                      |
| limit                         | numeric                | 800                     | TRUE                      |                                      |
| http_enabled                  | boolean                | TRUE                    | TRUE                      |                                      |
| archive_database_driver       | text                   | pgsql                   | FALSE                     | Archive Database Driver              |
| archive_database_host         | text                   |                         | FALSE                     | IP/Hostname of Archive Database      |
| archive_database_password     | text                   |                         | FALSE                     | Archive Database Password            |
| archive_database_port         | text                   | 5432                    | FALSE                     | Archive Database Port                |
| archive_database_username     | text                   |                         | FALSE                     | Archive Database Username            |
| storage                       | text                   | db                      | TRUE                      |                                      |
| archive_database              | boolean                | FALSE                   | FALSE                     | Enable Dedicated CDR Database Access |
| archive_database_name         | text                   | fusionpbx               | FALSE                     | Archive Database Name                |

## [Dashboard](default_settings/dashboard.html)

FusionPBX menu [Home > Dashboard](../home/dashboard.html)

Different user level settings that control what is seen and not seen on the dashboard for each user access level.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description                                                        |
|-----------------------------|----------------------|-----------------------|-------------------------|------------------------------------------------------------------------------------|
| admin                       | array                | voicemail             | TRUE                    | Enable Dashboard Voicemail block for users in the admin group.                     |
| admin                       | array                | missed                | TRUE                    | Enable Dashboard Missed Calls block for users in the admin group.                  |
| admin                       | array                | recent                | TRUE                    | Enable Dashboard Recent Calls block for users in the admin group.                  |
| admin                       | array                | limits                | FALSE                   | Enable Dashboard Domain Limits block for users in the admin group.                 |
| admin                       | array                | counts                | TRUE                    | Enable Dashboard Domain Counts block for users in the admin group.                 |
| admin                       | array                | ring_groups           | TRUE                    | Enable Dashboard Ring Group Forwarding controls for users in the admin group.      |
| admin                       | array                | caller_id             | FALSE                   | Enable changing Caller ID name and number.                                         |
| superadmin                  | array                | voicemail             | TRUE                    | Enable Dashboard Voicemail block for users in the superadmin group.                |
| superadmin                  | array                | missed                | TRUE                    | Enable Dashboard Missed Calls block for users in the superadmin group.             |
| superadmin                  | array                | recent                | TRUE                    | Enable Dashboard Recent Calls block for users in the superadmin group.             |
| superadmin                  | array                | limits                | FALSE                   | Enable Dashboard Domain Limits block for users in the superadmin group.            |
| superadmin                  | array                | counts                | TRUE                    | Enable Dashboard System Counts block for users in the superadmin group.            |
| superadmin                  | array                | call_routing          | TRUE                    | Enable Dashboard Call Routing controls for users in the superadmin group.          |
| superadmin                  | array                | caller_id             | FALSE                   | Enable changing Caller ID name and number.                                         |
| superadmin                  | array                | ring_groups           | TRUE                    | Enable Dashboard Ring Group Forwarding controls for users in the superadmin group. |
| user                        | array                | voicemail             | TRUE                    | Enable Dashboard Voicemail block for users in the users group.                     |
| user                        | array                | missed                | TRUE                    | Enable Dashboard Missed Calls block for users in the users group.                  |
| user                        | array                | recent                | TRUE                    | Enable Dashboard Recent Calls block for users in the users group.                  |
| user                        | array                | call_routing          | TRUE                    | Enable Dashboard Call Routing controls for users in the users group.               |
| user                        | array                | ring_groups           | TRUE                    | Enable Dashboard Ring Group Forwarding controls for users in the users group.      |
| user                        | array                | caller_id             | FALSE                   | Enable changing Caller ID name and number.                                         |
| admin                       | array                | call_routing          | TRUE                    | Enable Dashboard Call Routing controls for users in the admin group.               |
| superadmin                  | array                | system                | TRUE                    | Enable Dashboard System Status block for users in the superadmin group.            |
| agent                       | array                | call_center_agents    | TRUE                    | Enable Dashboard Call Center Agent Status block for users in the agent group.      |

## [Destinations](default_settings/destinations.html)

FusionPBX menu [Dialplan > Destinations](../dialplan/destinations.html)

Destinations specific defaults.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description |
|-----------------------------|----------------------|-----------------------|-------------------------|-----------------------------|
| dialplan_details            | boolean              | TRUE                  | TRUE                    |                             |

## [Domains](default_settings/domain.html)

FusionPBX menu [Advanced > Domains](../advanced/domains.html)

Domain specific defaults.

| Default Setting Subcategory | Default Setting Name | Default Setting Value                                                                                                           | Default Setting Enabled | Default Setting Description                                         |
|-----------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------|
| dial_string                 | text                 | {sip_invite_domain=${domain_name},leg_timeout=${call_timeout},presence_id=${dialed_user}@${dialed_domain}}${sofia_contact(*/${dialed_user}@${dialed_domain})} | TRUE                    | The dial string used                                               |
| template                    | name                 | default                                                                                                                       | TRUE                    | The template used                                                  |
| menu                        | uuid                 | b4750c3f-2a86-b00d-b7d0-345c14eca286                                                                                          | TRUE                    | The menu uuid                                                      |
| language                    | code                 | en-us                                                                                                                         | TRUE                    | Choose the language                                                |
| cidr                        | array                |                                                                                                                               | FALSE                   | Allow only specific ip addresses access                            |
| country                     | code                 | us                                                                                                                            | TRUE                    | The country code                                                   |
| bridge                      | text                 | outbound                                                                                                                      | TRUE                    | outbound,loopback,lcr                                               |
| paging                      | numeric              | 100                                                                                                                           | TRUE                    | Set the maximum number of records displayed per page. (Default: 50) |
| time_zone                   | name                 | America/Los_Angeles                                                                                                           | TRUE                    | Time zone used. Follows UNIX format                                 |

## [Editor](default_settings/domain.html)

FusionPBX menu Advanced > php editor, grammar editor, provision editor, and xml editor.

Editor specific defaults.
| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description                                               |
|-----------------------------|----------------------|-----------------------|-------------------------|---------------------------------------------------------------------------|
| indent_guides               | boolean              | FALSE                 | FALSE                   | Set the default visibility of indent guides for Editor.                   |
| invisibles                  | boolean              | FALSE                 | FALSE                   | Set the default state of invisible characters for Editor.                 |
| line_numbers                | boolean              | FALSE                 | FALSE                   | Set the default visibility of line numbers for Editor.                    |
| theme                       | text                 | Cobalt                | FALSE                   | Set the default theme.                                                    |
| font_size                   | text                 | 14px                  | FALSE                   | Set the default text size for Editor.                                     |
| live_previews               | boolean              | FALSE                 | FALSE                   | Enable or disable live previewing of syntax, text size and theme changes. |

## [Email](default_settings/email.html)

This is where you configure email settings to receive email notifications of voicemail, missed calls, and fax.

Here are some example settings for some of the most common email providers:

- [SMTP2GO](http://docs.fusionpbx.com/en/latest/advanced/default_settings/smtp2go.html)
- [GMAIL](http://docs.fusionpbx.com/en/latest/advanced/default_settings/gmail.html)

| Default Setting Subcategory | Default Setting Name | Default Setting Value          | Default Setting Enabled | Default Setting Description                                                       |
|-----------------------------|----------------------|--------------------------------|-------------------------|-----------------------------------------------------------------------------------|
| smtp_host                   | text                 | mail.server.provider.com       | TRUE                    | email providers server address                                                    |
| smtp_from                   | text                 | emailexample@emailprovider.com | TRUE                    | smtp from email address                                                           |
| smtp_port                   | numeric              | 587                            | TRUE                    | port number of the mail server provider                                           |
| smtp_from_name              | text                 | Voicemail                      | TRUE                    | smtp from name                                                                    |
| smtp_auth                   | text                 | TRUE                           | TRUE                    | If smtp auth is required                                                          |
| smtp_username               | text                 | user name                      | TRUE                    | typically the email user name                                                     |
| smtp_password               | text                 | supersecurepassword!           | TRUE                    | typically the email password                                                      |
| smtp_secure                 | text                 | tls                            | TRUE                    | tls or ssl depending on the provider                                              |
| smtp_validate_certificate   | boolean              | TRUE                           | TRUE                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
| method                      | text                 | smtp                           | TRUE                    | smtp\|sendmail\|mail\|qmail                                                       |

Error log for failed or successfully sent messages:

- [Email Log](http://docs.fusionpbx.com/en/latest/advanced/default_settings/email_error_log.rst)

## [Fax](default_settings/fax.html)

[Apps > Fax Server](../applications/fax_server.html)

Specific default settings for fax server.

| Default Setting Subcategory       | Default Setting Name | Default Setting Value           | Default Setting Enabled | Default Setting Description                                                                    |
|-----------------------------------|----------------------|---------------------------------|-------------------------|------------------------------------------------------------------------------------------------|
| cover_logo                        | text                 |                                 | TRUE                    | Path to image/logo file displayed in the header of the cover sheet.                            |
| allowed_extension                 | array                | .pdf                            | TRUE                    | Allowed extension to send .pdf                                                                 |
| allowed_extension                 | array                | .tif                            | TRUE                    | Allowed extension to send .tif                                                                 |
| allowed_extension                 | array                | .tiff                           | TRUE                    | Allowed extension to send .tiff                                                                |
| cover_header                      | text                 |                                 | FALSE                   | Default information displayed beneath the logo in the header of the cover sheet.               |
| page_size                         | text                 | letter                          | TRUE                    | Set the default page size of new faxes.                                                        |
| resolution                        | text                 | fine                            | TRUE                    | Set the default transmission quality of new faxes.                                             |
| variable                          | array                | fax_enable_t38=true             | TRUE                    | Enable T.38.                                                                                   |
| variable                          | array                | fax_enable_t38_request=false    | TRUE                    | Send a T38 reinvite when a fax tone is detected.                                               |
| variable                          | array                | ignore_early_media=true         | TRUE                    | Ignore ringing to improve fax success rate.                                                    |
| keep_local                        | boolean              | TRUE                            | TRUE                    | Keep the file after sending or receiving the fax.                                              |
| send_mode                         | text                 | queue                           | FALSE                   | Send mode. queue is default.                                                                   |
| send_retry_limit                  | numeric              | 5                               | TRUE                    | Number of attempts to send fax (count only calls with answer).                                 |
| send_retry_interval               | numeric              | 15                              | TRUE                    | Delay before we make next call after answered call.                                            |
| send_no_answer_retry_limit        | numeric              | 3                               | TRUE                    | Number of unanswered attempts in sequence.                                                     |
| send_no_answer_retry_interval     | numeric              | 30                              | TRUE                    | Delay before we make next call after no answered call.                                         |
| send_no_answer_limit              | numeric              | 3                               | TRUE                    | Give up reaching the destination after this number of sequences.                               |
| send_no_answer_interval           | numeric              | 300                             | TRUE                    | Delay before next call sequence.                                                               |
| storage_type                      | text                 | base64                          | FALSE                   | Store FAX in base64.                                                                           |
| smtp_from                         | text                 |                                 | TRUE                    | SMTP from address.                                                                             |
| smtp_from_name                    | text                 |                                 | TRUE                    | SMTP from name. Depends on the server, can be full email or everything before the @ sign.      |
| cover_font                        | text                 | times                           | FALSE                   | Font used to generate cover page. Can be full path to .ttf file or font name already installed.|
| cover_footer                      | text                 |                                 | TRUE                    | Notice displayed in the footer of the cover sheet.                                             |

## [Follow Me](default_settings/follow_me.html)

FusionPBX menu [Apps > Follow Me](../applications/follow_me.html)

Specific defaults for Follow Me.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description                       |
|-----------------------------|----------------------|-----------------------|-------------------------|---------------------------------------------------|
| max_destinations            | numeric              | 5                     | FALSE                   | Set the maximum number of Follow Me Destinations. |
| timeout                     | numeric              | 30                    | FALSE                   | Set the default Follow Me Timeout value.          |

## [IVR Menu](default_settings/ivr_menu.html)

FusionPBX menu [Apps > IVR Menus](../applications/ivr.html)

Specific default for IVR Menu.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description    |
|-----------------------------|----------------------|-----------------------|-------------------------|--------------------------------|
| option_add_rows             | numeric              | 5                     | TRUE                    | Number of default "add" rows.  |
| option_edit_rows            | numeric              | 1                     | TRUE                    | Number of default "edit" rows. |

## [Limit](default_settings/limit.html)

Limit specific default settings.

| Default Setting Subcategory | Default Setting Name | Default Setting Value | Default Setting Enabled | Default Setting Description        |
|-----------------------------|----------------------|-----------------------|-------------------------|------------------------------------|
| call_center_queues          | numeric              | 3                     | FALSE                   | Limit used in Call Center Queues.  |
| destinations                | numeric              | 3                     | FALSE                   | Limit used in Destinations.        |
| devices                     | numeric              | 3                     | FALSE                   | Limit used in Devices.             |
| extensions                  | numeric              | 3                     | FALSE                   | Limit used in Extensions.          |
| gateways                    | numeric              | 3                     | FALSE                   | Limit used in Gateways.            |
| ivr_menus                   | numeric              | 3                     | FALSE                   | Limit used in IVR Menus.           |
| ring_groups                 | numeric              | 3                     | FALSE                   | Limit used in Ring Groups.         |
| users                       | numeric              | 3                     | FALSE                   | Limit used in Users.               |

## [Login](default_settings/login.html)

Login specific default settings.

| Default Setting Subcategory | Default Setting Name | Default Setting Value      | Default Setting Enabled | Default Setting Description                                                             |
|-----------------------------|----------------------|----------------------------|-------------------------|-----------------------------------------------------------------------------------------|
| password_reset_key          | text                 | 9pG6sgerhuh5hetjnsrtjrjrdW | FALSE                   | Display a Reset Password link on the login box (requires smtp_host be defined).         |
| domain_name_visible         | boolean              | TRUE                       | FALSE                   | Displays a domain input or select box (if domain_name array defined) on the login box.  |
| domain_name                 | array                | pbx1.yourdomain.com        | FALSE                   | Domain select option displayed on the login box.                                        |
| message                     | text                 | Welcome to FusionPBX!      | TRUE                    | Display a message at login.                                                             |


