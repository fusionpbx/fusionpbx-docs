*************
Menu Add-ons
*************

  Menu add-ons are apps thats are either not in the menu by default or archived and could be deprecated.  https://github.com/fusionpbx/fusionpbx-apps
  
|

Acl
----

Move the acl to the optional Apps directory as it isn't completed yet

cdr
----

Content placeholder

content
-------

fifo_agents
-----------

get_call_details
----------------

hot_desking
-----------

Code integrated starting version 4.0.0 (Goto Accounts > Devices for current hot_desking) 

hunt_groups
-----------

invoices
--------

languages
---------

php_service
-----------

profiles
--------

roku
-----

schemas
-------

servers
-------

signup
-------

sipml5
-------

soft_phone
-----------

tickets
--------

users_bulk_add
---------------

voicemail_msgs
--------------

voicemail_status
----------------

xmpp
----

zoiper
-------

| QR and app provisioning with Zoiper

| This menu add-on will enable the abliity to do QR provisioning from IOS or android Zoiper app.  Zoiper has designed the process in a way that is cross platform.  Fusionpbx has the ability to click the extension you want to provision and a link wil open to either download the app on multiple platforms or if you have the app installed on a mobile device you can use the QR code scanner to scan a QR image and the mobile is ready to use.

| We will walk through the process

* **Zoiper.com account setup**

| There are two parts to make this function. http://oem.zoiper.com and Fusionpbx menu add-on.

| This all adds a one-click install for both the Desktop and Mobile Zoiper APPs in the User Portal. The page is accessible by end users.

| This can be done with the FREE Zoiper OEM account or can use the paid versions for more customization like branding.

| Go to: https://oem.zoiper.com/
| Sign up for Login
| Configure your Desktop and Mobile Apps with the information you want.
| Then click "CONFIGURE" Under Desktop. 
| This will give you a LINK with a PAGE ID:
| https://www.zoiper.com/en/page/MYPAGEID?u=&h=&p=&o=&t=&x=&a=&tr="
| Copy the page ID

|

* **Zoiper menu add-on for Fusionpbx**

| On your server

::

 git clone https://github.com/fusionpbx/fusionpbx-apps
 cp -R fusionpbx-apps/zoiper /var/www/fusionpbx/app
 chown -R www-data:www-data /var/www/fusionpbx/app/zoiper

| 1. Log into the FusionPBX webpage
| 2. Advanced -> Upgrade
| 3. Menu Defaults and Permission Defaults.
| 4. Log out and back in

| Advanced -> Default Settings

::

 Add a Default Setting
 Category: zoiper
 Subcategory: page_id
 Type: text
 Value: MYPAGEID
 Enabled: True
 Save

| Goto Apps -> Zoiper
| Superadmin will see a list of ALL USER EXTENSIONS
| Users will only see the extensions assigned to them.

| Click on a link and it will take you to the Zoiper Site. Follow instructions there to download and install.

