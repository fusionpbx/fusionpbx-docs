Each phone on the PBX is setup to register to one or more extension
numbers.

Basic Setup
===========

-  To add an extension go to the Menu -> Accounts -> Extensions and
   press the add button.
-  Set an extension number
-  the rest of the defaults are fine for a basic example.
-  Press save.
-  Hover over the password input, it will allow you to see/copy the
   password

Passwords
---------

FusionBPX automatically generates a password for the extension. It is
randomly created (symbols, letters, numbers). You can find this password
after you create the extension.

-  Menu -> Accounts -> Extensions

   -  click 'e' to edit the extension you need to see

      -  find the password field
      -  click inside the field of bullets

         -  FusionPBX will display the password to you so you can see it
            and copy/paste on the line below.

-  Alternatively, you can do:

   -  less
      [freeswitch\_config\_dir]/directory/default/v\_ExtensionNumber.xml



Options
=======

| **Extension** What is used to register the phone (typically your
  extension number but can be any alphanumeric) used to register phone
  in the field user ID, username etc.
|  **Number Alias** The number you can dial to get this extension if the
  extension is non numerical.

| **Range** used to setup one or more extensions. In other words this
  can be used to create extension in bulk from 1 to 1000 extensions.
| If the checkbox for Auto-generate user with extension as login name is
  checked, User List is ignored, and a user is created and linked to the
  extension.
| A printable List of usernames and randomly generated passwords is
  dumped to screen so can capture them for later.

| **``Effective`` ``Caller`` ``ID``
  ``Name:``**\ `` is used when calling internal numbers. ( ``\ **```effective_caller_id_name`` <http://wiki.freeswitch.org/wiki/Variable_effective_caller_id_name>`__**\ `` - FreeSWITCH variable )``
| **``Effective`` ``Caller`` ``ID``
  ``Number:``**\ `` is used when when calling internal numbers. ( ``\ **```effective_caller_id_number`` <http://wiki.freeswitch.org/wiki/Variable_effective_caller_id_number>`__**\ `` - FreeSWITCH variable )``
| ``The Effective Caller Name and Number are also used to populate the voicemail Subject line information.``

| **``Outbound`` ``Caller`` ``ID``
  ``Name:``**\ `` is used when calling external numbers. ( ``\ *```outbound_caller_id_name`` <http://lists.freeswitch.org/pipermail/freeswitch-users/2010-February/053648.html>`__*\ `` - General variable )``
| **``Outbound`` ``Caller`` ``ID``
  ``Number:``**\ `` is used when calling external numbers. ( ``\ *```outbound_caller_id_number`` <http://lists.freeswitch.org/pipermail/freeswitch-users/2010-February/053648.html>`__*\ `` - General variable )``

| ``Caller ID notes:``
| ``Effective caller id is the real caller id however people tend to like and internal caller id for extensions and an external caller id when calling ``
| ``out the gateways so when calling out a gateway if you were to look at the outbound route in the edit window as a superadmin users you would see``
| ``that when going out the gateway it sets the outbound caller id to the effective caller id the effect is this on the extension you set the effective``
| ``caller id to the internal caller id info the number as the extension number then you set the outbound caller id as the external caller id.  This is``
| ``used to set the outbound caller ID effective_caller_id_name=${outbound_caller_id_name}.  The Outbound caller ID variable doesn't exist in FreeSWITCH,``
| ``it is a feature of FusionPBX.  You can set the caller id either on an outbound route or on an extension.``

**Account Code** - this is not used anywhere in the default dialplan but
is provided in FreeSwitch and therefore is provided in FusionPBX for
full compatibility. It sets a variable for the extension that could be
used in a condition. See `Variable
accountcode <http://wiki.freeswitch.org/wiki/Variable_accountcode>`__
for more information. Note that it can be used to affect the operation
of CDR.

``Functionality for phone provisioning is now provided on this screen, but has not yet been documented here.``

*' Directory Full Name*' This is the name that will be used for a \*411
or Company Directory lookup as often used in IVR.

Notes
=====

The password is set automatically using a combination of random
characters that are:

-  upper and lower case letters,
-  numbers
-  symbols

Rather than changing the password to something simple it is much wiser
to keep it as it was automatically set and to use that password to
connect the phone with. To view the password that has been automatically
set, open the extension page again and click on the obfuscated password
in the password field. The actual password will be revealed just below
the password field.

