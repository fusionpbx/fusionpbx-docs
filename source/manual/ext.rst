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

Registering Phones
==================

For most things your extension number is your username, and password is
[see above]. You'll also need to put your ip address, or DNS name in the
proper place.

Examples
--------

Polycom
~~~~~~~

Soundpoint IP 320P
^^^^^^^^^^^^^^^^^^

Identification

    Display Name: FusionPBX
    Address: ExtensionNumber
    Authentication User ID: ExtensionNumber
    Authentication Password: PASSWORD
    Label: ExtensionNumber or Whatever
    Type: Private
    Third Party Name: BLANK
    Number Of Line Keys: BLANK
    Calls Per Line: BLANK

Server 1

    Address: FusionBPX IP ADDRESS or DOMAIN NAME if doing multi-tenant
    Port: 5060
    Transport: DNSnaptr works or UDP or whatever
    Expires: default (30 works ok NATTED)
    Register: BLANK
    Retry Timeout: BLANK
    Retry Maximum Count: BLANK
    Line Seize Timeout: BLANK

Server 2

    leave alone

Call Diversion

    leave alone

Message Center

    Subscriber: BLANK
    Callback Mode: Contact
    Callback Contact: \*98

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

Notes on Toll Allow
===================

Toll Allow is a variable that can be set per extension. It allows you to
limit who can make what type of calls. Note that although the variable
is provided in the extension configuration, the default dialplan DOES
NOT make use of it. Therefore if you want to use it you need to add
statements to the dialplan to enable it.

The following are notes on Toll Allow that were captured from IRC
discussions on the topic. This needs to be updated by someone who
understands it or has used it:

| ``An example for the contents of the toll_allow variable would be:``
| 

| ``You can then add information to your dialplan to process this variable.  In the example XML below, if the valid allow value isn't present then``
| ``an extension shouldn't be able to dial out.  However extension -> extension should still work.``

| ``The following code are example XML for standard outbound routes (Dialplan->OutboundRoutes).  Effectively you are applying an additional  ``
| ``condition to EACH outbound route that you want to limit.  So in the FusionPBX GUI select an outbound route and add a condition, type  ``
| ``"${toll_allow}", data "local".  Order is important, this should be the FIRST condition of your outbound route.``
| ``You'll need to do that for all of your outbound routes, tag them local, domestic, or international depending on what they are.``
| ``On some installations this example file will be present in /usr/local/freeswitch/conf/dialplan/default/01_example.com.xml: ``

| 

::

   <include>
   <extension name="local.example.com">
   <condition field="${toll_allow}" expression="local"/>
   <condition field="destination_number" expression="^(\d{7})$">
     <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
     <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
     <action application="bridge" data="sofia/gateway/${default_gateway}/1${default_areacode}$1"/>
   </condition>
   </extension>

   <extension name="domestic.example.com">
   <condition field="${toll_allow}" expression="domestic"/>
   <condition field="destination_number" expression="^(\d{11})$">
     <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
     <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
     <action application="bridge" data="sofia/gateway/${default_gateway}/$1"/>
   </condition>
   </extension>

   <extension name="international.example.com">
   <condition field="${toll_allow}" expression="international"/>
   <condition field="destination_number" expression="^(011\d+)$">
     <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
     <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
     <action application="bridge" data="sofia/gateway/${default_gateway}/$1"/>
   </condition>
   </extension>
   </include>

| 

The above example is how to PERMIT calls. The example below takes the
opposite approach and is how to PREVENT calls. Effectively, the above
example assumes all calls are bad (except internal) unless they are
flagged as good by the value of the toll\_allow variable. The below
example takes the opposite approach - it assumes that all calls are good
unless they are flagged as bad.

| ``Put this in your advanced dialplan. In the toll allow of whatever extension you wanted to restrict put the value 'local'.  This example ``
| ``restricts from calling 10 or 11 digit numbers.``

| 

::

   <extension name="localcalls" >
   <condition field="${toll_allow}" expression="local"/>
   <condition field="destination_number" expression="(^\d{10}$|^\d{11}$)">
   <action application="hangup"/>
   </condition>
   </extension>
  
|
