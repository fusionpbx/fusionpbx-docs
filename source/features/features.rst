**********
Features
**********


Announcements
---------------

Setup a recording for the auto attendant that provides announcement to callers. (See `IVR Menus`_ )

Authentication
----------------

Extendable with plugin support. Web interface authentication by default authenticates against the FusionPBX Database. LDAP is one and has also been tested with Microsoft Active Directory an OpenLDAP.

`Call Barge / Eavesdrop / Intercept`_
----------------------------------------

Listen into an active call from another extension.

`Call Block`_
---------------

Block inbound calls by the caller id.

`Call Broadcast`_
-------------------

Create a recording and select one or more groups to have the system call and play the recording.

`Call Center`_
---------------

Creates a robust call center environment with agent tiers.

`Call Detail Records`_
------------------------

Various reporting capabilities to see who called, when, call length, export to a csv file, and call detail statistics.

`Call Flows (Day Night Mode)`_ 
---------------------

Typically used with day night mode. To direct calls between two destinations. Can work with BLF on phone to show which direction call will be directed to.

`Call Forward`_
-----------------

Forward to another extension or to any phone number.

Call Monitoring
-----------------

View which extensions are currently in a call. (see `Active Extensions`_)

Call Pickup
-------------

For a particular extension or any extension that is currently ringing.

`Queues`_
--------------

Load calls into queues so they can be answered in the order they came into the queue.

`Call Recordings`_
-------------------

Record all or some calls or parts of the call.

`Call Routing`_
----------------

Send the call different directions or perform actions based on reading the caller id info or other call information. (see `Dialplan Manager`_)

Call Announced Transfer
--------------------------------

Transfer the active call to another internal or external call.  Also known as a warm transfer.

`Call Blind Transfer`_
---------------------------

Transfer a call like the call was going into a call queue or from an ivr.

`Call Transfer`_
----------------------

Transfer a call.

`Call Waiting`_
---------------------

A beep while on a call and to toggle between two different calls.

Caller ID
------------------

Support for customization and supporting providers.

`Conference`_
---------------------

Set up voice and video conference calls, is optionally secure with a PIN number, and can transfer current calls to a conference.  Interactive conference control provides ability to see the list of callers in the conference and manage the volume, see who is talking, kick, mute, unmute, deaf, undeaf, profiles and controls. (See `Conference`_)

`Conference Center`_
-------------------------

Unlimited conference rooms with moderator and paticipants, pin numbers, call recording, mute all, caller announce and more...

Configuration
---------------------

While the admin configures the system in the web interface. The data is saved to the database and can optionally be deliverd to FreeSWITCH via XML files, or on demand from the database.

`Contacts`_
-------------

Manage your contacts. Import contacts from Outlook CSV files. Export contacts to your cell phone with QR Codes. It is also possible to add additional features like time cards and invoices that can be related to the contacts.

`Command`_
-----------

Area to execute commands from the gui. Merged with SQL Query tool with a clip library.

`Dialplan Manager`_
---------------------

The dialplan is used to setup call destinations based on conditions and context. You can use the dialplan to send calls to gateways, auto attendants, external numbers, to scripts, or any destination. 

`Dial by Name`_ (\*\411)
------------------------

Search by first name or last name to find extension numbers on the system.

`Direct Inward System Access`_ (DISA)
-------------------------------------------

Gives ability to call into the system, put in a pin code, and then call back outbound.

`Device Provisioning`_
------------------------

From Advanced > Default Settings you can enable provisioning for devices. Contacts used as Directory for the phones, vendor list and functions can be enabled or disabled. Support for memory, expansion (side cars), and programmable keys. Configure SIP endpoints for Yealink, Polycom, Cisco, Aastra and several other brands.

`Do Not Disturb (DND)`_
-------------------------

Direct calls to voicemail by default however there is an option when using do not disturb to send the call to an alternative destination.

`Extensions`_
-----------

Create extensions for phones to register to and an option to receive emails on missed calls.

`Extension Summary`_
-------------------

Summary of extension activity per domain such as misssed calls, answered calls, no answer, inbound duration, outbound duration, number of outboud calls, number of inbound calls and Average length of Conversation (ALOC). The summarized information can be downloaded as a CSV file.

`Editor`_
-----------

File editor for PHP, XML, and Provisioning files. 

`Fax Server`_
----------------

A virtual fax machine that can send and receive faxes with advanced features.

`Follow Me`_
------------

Allows calling multiple extensions or external numbers.

`Gateways`_
-------------

Gateways provide access into other voice networks. These can be voice providers or other systems that require SIP registration.  `Check out the Youtube video <https://youtu.be/YKOTACDYQ3A>`_.

Hot Desking
---------------

A way to login to another phone device and temporarily or permanently become another extension. This is sometimes known as 'hoteling' and 'extension mobility'

`Inbound and Outbound Call Routing`_
----------------------------------

Routes used to receive or send calls in or out of FusionPBX.

`IVR Menus`_ (Auto Attendant)
------------------------------

Create a structured interactive voice prompt for callers to use. Uses FreeSWITCH IVR and delivered from Database on Demand. Cached to memcache with IVR Menu Options all editable at once. Also works with Text to Speech.

`Music on Hold`_
------------------

Allows multiple categories of music on hold that can be set globally or per domain. Can inject additional audio on intervals such as 'Your call is very important to us please stand by'.

`Multi-Tenant`_
--------------------------------------------

Domain based multi-tenant using subdomains such as red.pbxhosting.tld green.pbxhosting.tld blue.pbxhosting.tld

`Operator Panel`_
--------------------

A virtual panel that agents can drag and drop transfer calls. Adjust call state from available, on break, do not disturb and logged out. 

`Paging`_
--------

Page another extension with or without password

`Parking`_
---------

Send a call to an unused "park" extension.  The caller listens to music on hold until another extension connects to the call.

`Phrases`_
-----------

Using xml handler and xml from file system you can string together multiple voice files.

`Provider Setup`_
----------------

`Re-branding and Customize`_
-----------------------------

FusionPBX has unprecedented customizability which can be used to meet your needs or the needs of your customers. Customizable themes, menu, dialplan, and Hundreds of Default Settings to control the theme.

`Recordings`_
----------------

Create and manage personalized recordings.

`Ring Groups`_
-------------------

Make one extension ring several extensions and an option to receive emails on missed calls.

`Scalable and Redundant`_
--------------------

Can be configured for multi-master database replication, file replication. FusionPBX, Database, and FreeSWITCH can be distributed across multiple servers for large enterprise scale systems.

`Time Conditions`_
--------------------

A extension that can be timed to route calls based on domain select, global option, move to other domains, and holiday presets.

`User and Group Management`_
------------------------------

Edit, change or add users of all permission levels.

`Voicemail`_
-----------

Has ability to copy voicemails for other voicemail boxes when receiving a voicemail. Additional features include voicemail to email and voicemail IVR. Forward add intro, check box for multi-delete.


`Voicemail to Email`_
---------------------- 

Have voicemails sent to email.

`Voicemail Transcription`_
---------------------------

Converts voicemails to text.


`WebRTC`_
----------

Make and receive video calls with a web browser.


Additional Features
-------------------

This is not a comprehensive set of features. A complete list would be many times larger. More will be added as time permits.


.. _IVR Menus: ../applications/ivr.html
.. _Direct Inward System Access: ../dialplan/dialplan_details.html#disa
.. _Paging: ../dialplan/dialplan_details.html#page
.. _Voicemail to Email: ../getting_started/voicemail_to_email.html
.. _Inbound and Outbound Call Routing: ../dialplans.html
.. _Call Broadcast: ../applications/call_broadcast.html
.. _Extensions: ../accounts/extensions.html
.. _Call Flows (Day Night Mode): ../applications/call_flows.html
.. _Call Recordings: ../applications/call_recordings.html
.. _Operator Panel: ../applications/operator_panel.html
.. _Dial by Name: ../features/dial_by_name.html
.. _Follow Me: ../applications/follow_me.html
.. _Call Block: ../applications/call_block.html
.. _Call Barge / Eavesdrop / Intercept: ../additional_information/feature_codes.html
.. _Call Center: ../applications/call_center.html
.. _Call Transfer: ../additional_information/feature_codes.html
.. _Call Blind Transfer: ../additional_information/feature_codes.html
.. _Call Waiting: ../additional_information/feature_codes.html
.. _Call Detail Records: ../applications/call_detail_record.html
.. _Call Forward: ../applications/call_routing.html
.. _Call Flows: ../applications/call_flows.html
.. _Call Routing: ../applications/call_routing.html
.. _Contacts: ../applications/contacts.html
.. _Adminer: ../advanced/adminer.html
.. _Command: ../advanced/command.html
.. _Conference: ../applications/conference.html
.. _Contact Manager: http://docs.fusionpbx.com/en/latest
.. _Device Provisioning: ../applications/provision.html
.. _Provider Setup: ../accounts/providers.html
.. _Dialplan Manager: ../dialplan/dialplan_manager.html
.. _Do Not Disturb (DND): ../applications/call_routing.html
.. _Editor: ../advanced/editors.html
.. _Extension Summary: /en/latest/status/extension_summary.html
.. _Active Extensions: ../status/active_extensions.html
.. _Hot Desking: ../accounts/hot_desking.html
.. _Multi-Tenant: ../advanced/domains.html
.. _Music on Hold: ../applications/music_on_hold.html
.. _Phrases: ../applications/phrases.html
.. _Queues: ../applications/queues.html
.. _Active Calls: ../status/active_calls.html
.. _Conference Center: ../applications/conference_center.html
.. _Fax Server: ../applications/fax_server.html
.. _Gateways: ../accounts/gateways.html
.. _Time Conditions: ../applications/time_conditions.html
.. _Ring Groups: ../applications/ring_group.html
.. _Recordings: ../applications/recordings.html
.. _Voicemail: ../applications/voicemail.html
.. _Voicemail Transcription: ../applications/voicemail.html#voicemail-transcription
.. _and lots more...: ../features/features.html
.. _Scalable and Redundant: https://fusionpbx.com/app/www/training_detail.php
.. _User and Group Management: ../advanced/group_manager.html
.. _Parking: /en/latest/features/parking.html
.. _Re-branding and Customize: http://fusionpbx.com/support.php
.. _WebRTC: ../applications_optional/webrtc.html


