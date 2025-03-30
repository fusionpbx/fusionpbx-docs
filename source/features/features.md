# Features

Explore the powerful capabilities of FusionPBX, organized into categories below. Each feature links to detailed documentation where available.

---

## Call Management
:::{table}
:widths: auto
:align: center

| **Feature**                    | **Description**                                                  | **Documentation**                                    |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Announcements                 | Set up auto attendant<br> recordings for caller announcements        | [IVR Menus](../applications/ivr.md)               |
| Barge/Eavesdrop/Intercept| Listen into active calls from another extension                  | [Feature Codes](../additional_information/feature_codes.md) |
| Call Block                    | Block inbound calls by caller ID                                 | [Call Block](../applications/call_block.md)         |
| Call Broadcast                | Create a recording and select one or more groups<br>to have the system call and play the recording                  | [Call Broadcast](../applications/call_broadcast.md) |
| Call Forward                  | Forward calls to extensions or external numbers                  | [Call Routing](../applications/call_routing.md)     |
| Call Monitoring               | View which extensions are currently in a call<br>(see [Active Extensions](../status/active_extensions.md))                                   |             |
| Call Pickup                   | Answer an extension that is currently ringing                |                                      |
| Call Recordings               | Record all calls, some calls or parts of the call                                    | [Call Recordings](../applications/call_recordings.md) |
| Call Routing                  | Send the call to multiple directions or perform<br>actions based on caller id and other information<br> (see [Dialplan Manager](../dialplan/dialplan_manager.md))                 | [Call Routing](../applications/call_routing.md)     |
| Call Announced Transfer       | Transfer the active call to another internal<br>or external call. Also known as a warm transfer                       |                                                      |
| Call Blind Transfer           | Transfer calls like a queue or IVR handoff                       | [Feature Codes](../additional_information/feature_codes.md) |
| Call Transfer                 | General call transfer functionality                              | [Feature Codes](../additional_information/feature_codes.md) |
| Call Waiting                  | Toggle between calls with a beep notification                    | [Feature Codes](../additional_information/feature_codes.md) |
| Do Not Disturb (DND)          | Direct calls to voicemail by default<br>or send to an alternate destination              | [Call Routing](../applications/call_routing.md)     |
| Follow Me                     | Ring multiple extensions or external numbers                     | [Follow Me](../applications/follow_me.md)         |
| Parking                       | Park calls on hold for pickup by another extension               | [Parking](../features/parking.md)         |
| Queues                        | Load calls into queues to answer in join order    | [Queues](../applications/queues.md)                 |
| Ring Groups                   | Ring multiple extensions from one extension<br>with an option to receive emails on missed calls                 | [Ring Groups](../applications/ring_group.md)      |
:::

---

## Conferencing
:::{table}
:widths: auto
:align: center

| **Feature**                    | **Description**                                                  | **Documentation**                                    |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Conference                    | Voice/video conference calls, optionally PIN-secured<br>Transfer calls in with interactive conference controls<br>Show callers, manage volume, see talking status,<br>options to kick/mute/unmute/deaf/undeaf members   | [Conference](../applications/conference.md)       |
| Conference Center             | Unlimited rooms with moderation, PINs, and recording             | [Conference Center](../applications/conference_center.md) |
:::

---

## Reports & Tools
:::{table}
:widths: auto
:align: center

| **Feature**                    | **Description**                                                  | **Documentation**                                    |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Call Detail Records           | Detailed call reports, exportable to CSV                         | [Call Detail Records](../applications/call_detail_record.md) |
| Command                       | Execute commands and SQL queries via GUI                         | [Command](../advanced/command.md)                 |
| Editor                        | Edit PHP, XML, and provisioning files                            | [Editor](../advanced/editors.md)                  |
| Extension Summary             | Show activity per domain, such as misssed calls<br>answered calls, no answer, inbound duration,<br>outbound duration, amount of outbound/inbound calls<br>and Average length of Conversation (ALOC)<br>Export Summarized information as an CSV file             | [Extension Summary](../status/extension_summary.md) |
:::

---

## System Config
:::{table}
:widths: auto
:align: center

| **Feature**                    | **Description**                                                  | **Documentation**                                    |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Authentication                | Web interface with plugin support (LDAP, AD)                     |                                                      |
| Configuration                 | While the admin configures the system in the web<br>interface. The data is saved to the database and<br>can optionally be deliverd to FreeSWITCH<br> via XML files, or on demand from the database                 |   [Contacts](../applications/contacts.md)                                                   |
| Contacts                | Manage your contacts. Import from Outlook CSV<br> Export contacts to your cell phone with QR Codes<br> Additional features such as time cards and<br>invoices that can be related to the contacts                     |                                                      |
| Device Provisioning           | Provision devices with contacts as phone directories<br>Enable and disable vendors, Set memory,<br>expansion (sidecars), and programmable keys<br>Setup endpoints for Yealink, Polycom, Cisco, etc            | [Device Provision](../applications/provision.md) |
| Dialplan Manager              | The dialplan is used to setup call destinations based<br>on conditions and context. You can use the<br>dialplan to send calls to gateways, auto attendants,<br>external numbers, to scripts, or any destination                    | [Dialplan Manager](../dialplan/dialplan_manager.md) |
| Gateways                      | Gateways provide access into other voice networks<br>These can be voice providers or other systems<br>that require SIP registration. [See Video](https://youtu.be/YKOTACDYQ3A)                      | [Gateways](../accounts/gateways.md)               |
| Multi-Tenant                  | Domain based multi-tenant using subdomains<br>e.g. red.pbxhosting.tld or blue.pbxhosting.tld                  | [Multi-Tenant](../advanced/domains.md)            |
| Scalable and Redundant        | Configurable for multi-master database replication,<br>file replication, FusionPBX, and FreeSWITCH<br>Multi-server distribution for enterprise scalability                       | [Training](https://fusionpbx.com/training) |
| Manage Users/Groups     | Manage permissions levels and users                                     | [Group Manager](../advanced/group_manager.md)     |
:::

---

## Advanced Features
:::{table}
:widths: auto
:align: center

| **Feature**                    | **Description**                                                  | **Documentation**                                    |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Call Flows (Day/Night Mode)   | To direct calls between two destinations.<br>Direction can be displayed on phones BLF                   |                                                      |
| Caller ID                     | Customize and support provider caller ID                         |                                                      |
| Call Center               | Create a robust call center environment                      |   [Call Centers](../applications/call_center.md)                                                     |
| Dial by Name (*411)           | Search extensions by first or last name                                        | [Dial by Name](../additional_information/dial_by_name.md)       |
| Direct Inward System Access   | Gives ability to call into the system, put<br>in a pin code, and then call back outbound                     | [Dialplan Details](../dialplan/dialplan_details.md#disa) |
| Extensions                    | Create extensions for phone registration<br>and options to send an email on<br> missed calls to one or multiple contacts                      | [Extensions](../accounts/extensions.md)           |
| Fax Server                    | Send/receive faxes with advanced features                        | [Fax Server](../applications/fax_server.md)       |
| Hot Desking                   | Login to another phone device to become<br>an extension temporarily or permanently<br>Also know as hoteling or extension mobility                       |                                                      |
| Inbound/Outbound Call Routing | Routes to receive or send calls in or out                                | [Dialplans](../dialplans.md)                      |
| IVR Menus (Auto Attendant)    | Interactive voice prompts with TTS support                       | [IVR Menus](../applications/ivr.md)               |
| Music on Hold                 | Allows multiple categories of music on hold<br> that can be set globally or per domain. Can<br>inject additional audio on intervals such as<br>‘Your call is very important to us<br>please stand by’                          | [Music on Hold](../applications/music_on_hold.md) |
| Operator Panel                | A virtual panel that agents can drag and<br>drop transfer calls. Set agents to available,<br>on break, do not disturb and logged out                          | [Operator Panel](../applications/operator_panel.md) |
| Paging                        | Page extensions with optional password                           | [Dialplan Details](../dialplan/dialplan_details.md#page) |
| Phrases                       | Use xml handler and xml from file system<br>you can string together multiple voice files                                   | [Phrases](../applications/phrases.md)             |
| Provider Setup                | Configure voice providers                                        |          |
| Re-branding and Customize     | With unprecedented customizability you<br>can meet your needs or the needs of your<br>customers. Customize themes, menus,<br>and hundreds of theme adjustments                         | [Support](http://fusionpbx.com/support.php)         |
| Recordings                    | Create and manage personalized recordings                                   | [Recordings](../applications/recordings.md)       |
| Time Conditions               | Time-based call routing with domain,<br>global options and holiday presets                         | [Time Conditions](../applications/time_conditions.md) |
| Voicemail                     | Advanced voicemail with email and IVR                       | [Voicemail](../applications/voicemail.md)         |
| Voicemail to Email            | Have voicemails sent to email                                 | [Voicemail to Email](../getting_started/voicemail_to_email.md) |
| Voicemail Transcription       | Convert voicemails to text                                       | [Voicemail](../applications/voicemail.md#voicemail-transcription) |
| WebRTC                        | Make/Receive video calls in a web browser                                  | [WebRTC](../applications_optional/webrtc.md)      |
:::

---

## Additional Features
This list is not exhaustive—FusionPBX offers many more capabilities. Stay tuned as we expand this documentation!
