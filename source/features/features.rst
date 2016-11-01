**********
Features
**********

Adminer
---------

Integrated for an administrator in the superadmin group to enable easy database access.

Announcements
---------------

Setup a recording for the auto attendant that provides announcement to callers. (See `IVR Menus`_ )

Authentication
----------------

Extendable with plugin support. Web interface authentication by default authenticates against the FusionPBX Database. LDAP is one and has also been tested with Microsoft Active Directory an OpenLDAP.

Call Barge / Eavesdrop / Intercept
-----------------------------------

Listen into an active call from another extension.

Call Block
---------------

Block inbound calls by the caller id.

Call Broadcast
-------------------

Create a recording and select one or more groups to have the system call and play the recording.

Call Center
------------

Creates a robust call center environment with agent tiers.

Call Detail Records
------------------------

Various reporting capabilities to see who called, when, call length, export to a csv file, and call detail statistics.

Call Flows (Day Night Mode)
--------------------------------

Typically used with day night mode. To direct calls between two destinations. Can work with BLF on phone to show which direction call will be directed to.

Call Forward
-----------------

Forward to another extension or to any phone number.

Call Monitoring
-----------------

View which extensions are currently in a call. (see Active Extensions)

Call Pickup
-------------

For a particular extension or any extension that is currently ringing.

Call Queuing
--------------

Load calls into queues so they can be answered in the order they came into the queue. (see `Queues`_)

Call Recordings
-----------------

Record all or some calls or parts of the call.

Call Routing
--------------

Send the call different directions or perform actions based on reading the caller id info or other call information. (see `Dialplan Manager`_)

Call Announced Transfer
--------------------------------

Transfer the active call to another internal or external call.  Also known as a warm transfer.

Call Blind Transfer
---------------------------

Transfer a call like the call was going into a call queue or from an ivr.

Call Transfer
----------------------

Transfer a call.

Call Waiting
---------------------

A beep while on a call and to toggle between two different calls.

Caller ID
------------------

Support for customization and supporting providers.

Conferencing
---------------------

Set up voice and video conference calls, is optionally secure with a PIN number, and can transfer current calls to a conference.  Interactive conference control provides ability to see the list of callers in the conference and manage the volume, see who is talking, kick, mute, unmute, deaf, undeaf, profiles and controls. (See `Conferences`_)

Conference Center
-------------------------

Unlimited conference rooms with moderator and paticipants, pin numbers, call recording, mute all, caller announce and more...

Configuration
---------------------

While the admin configures the system in the web interface. The data is saved to the database and can optionally be deliverd to FreeSWITCH via XML files, or on demand from the database.

Contacts
-----------

Manage your contacts. Import contacts from Outlook CSV files. Export contacts to your cell phone with QR Codes. It is also possible to add additional features like time cards and invoices that can be related to the contacts.

Command
--------

Area to execute commands from the gui. Merged with SQL Query tool with a clip library.

Dialplan
-----------

Dial by Name
--------------------

Search by first name or last name to find extension numbers on the system.

Direct Inward System Access (DISA)
-------------------------------------------

Gives ability to call into the system, put in a pin code, and then call back outbound.

Device Provisioning
--------------------

From Advanced > Default Settings you can enable provisioning for devices. Contacts used as Directory for the phones, vendor list and functions can be enabled or disabled. Support for memory, expansion (side cars), and programmable keys. Configure SIP endpoints for Yealink, Polycom, Cisco, Aastra and several other brands.

Do Not Disturb (DND)
----------------------

Direct calls to voicemail by default however there is an option when using do not disturb to send the call to an alternative destination.

`Extensions`_
-----------

Create extensions for phones to register to and an option to receive emails on missed calls.

Extension Summary
-------------------

Summary of extension activity per domain such as misssed calls, answered calls, no answer, inbound duration, outbound duration, number of outboud calls, number of inbound calls and Average length of Conversation (ALOC). The summarized information can be downloaded as a CSV file.

Editor
-------

File editor for PHP, XML, and Provisioning files. 

`Fax Server`_
----------------

A virtual fax machine that can send and receive faxes with advanced features.

Follow-Me
------------

Allows calling multiple extensions or external numbers.

Hot Desking
------------

A way to login to another phone device and temporarily or permanently become another extension. This is sometimes known as 'hoteling' and 'extension mobility'


`Inbound and Outbound Call Routing`_
----------------------------------

Routes used to receive or send calls in or out of FusionPBX.

`IVR Menus`_ (Auto Attendant)
------------------------------

Create a structured interactive voice prompt for callers to use. Uses FreeSWITCH IVR and delivered from Database on Demand. Cached to memcache with IVR Menu Options all editable at once. Also works with Text to Speech.


Queues
--------

Like Call Center but more flexable.

Music on Hold
--------------

Allows multiple categories of music on hold that can be set globally or per domain. Can inject additional audio on intervals such as 'Your call is very important to us please stand by'.

Multi-Tenant
--------------------------------------------

Domain based multi-tenant using subdomains such as red.pbxhosting.tld green.pbxhosting.tld blue.pbxhosting.tld

Operator Panel
---------------

A virtual panel that agents can drag and drop transfer calls. Adjust call state from available, on break, do not disturb and logged out. 

Paging
--------

Page another extension with or without password

Parking
---------

Park calls.

Phrases
--------

Using xml handler and xml from file system you can string together multiple voice files.


Provider Setup
----------------

Re-branding and Customize
--------------------------

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

User and Group Management
--------------------------

Edit, change or add users of all permission levels.

Voicemail
-----------

Has ability to copy voicemails for other voicemail boxes when receiving a voicemail. Additional features include voicemail to email and voicemail IVR. Forward add intro, check box for multi-delete.


Voicemail to Email
-------------------

Have voicemails sent to email.

WebRTC
-------

Make and receive video calls with a web browser.


.. _IVR Menus: http://docs.fusionpbx.com/en/latest/applications/ivr.html
.. _Inbound and Outbound Call Routing: http://docs.fusionpbx.com/en/latest/gateway_inbound_outbound/gateway.html
.. _Call Broadcast: http://docs.fusionpbx.com/en/latest
.. _Extensions: http://docs.fusionpbx.com/en/latest/extensions_ivr/extensions.html
.. _Call Block: http://docs.fusionpbx.com/en/latest
.. _Call Detail Records: http://docs.fusionpbx.com/en/latest
.. _Call Forward: http://docs.fusionpbx.com/en/latest
.. _Call Flows: http://docs.fusionpbx.com/en/latest
.. _Contact Manager: http://docs.fusionpbx.com/en/latest
.. _Dialplan Manager: http://docs.fusionpbx.com/en/latest/manual/dialplan.html?#dialplan-manager
.. _Active Extensions: http://docs.fusionpbx.com/en/latest
.. _Queues: http://docs.fusionpbx.com/en/latest
.. _Recordings: http://docs.fusionpbx.com/en/latest/applications/recordings.html
.. _Active Calls: http://docs.fusionpbx.com/en/latest
.. _Conferences: http://docs.fusionpbx.com/en/latest
.. _Fax Server: http://docs.fusionpbx.com/en/latest/applications/fax_server.html
.. _Time Conditions: http://docs.fusionpbx.com/en/latest/applications/time_conditions.html
.. _Ring Groups: http://docs.fusionpbx.com/en/latest/applications/ring_groups.html
.. _Recordings: http://docs.fusionpbx.com/en/latest/applications/recordings.html
.. _and lots more...: http://docs.fusionpbx.com/en/latest/features/features.html
.. _Scalable and Redundant: https://fusionpbx.com/app/www/training_detail.php
