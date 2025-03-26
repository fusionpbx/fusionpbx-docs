# Provision

## Automatic

Auto provisioning is disabled by default. This is to give a chance to
secure provisioning server with HTTP Authentication or CIDR. HTTP
Authentication requires the phone to send hash of the combined username
and password in order to get configuration. CIDR is an IP address
restriction that can be used to restrict which IP addresses are allowed
to get the device configuration. An example of CIDR is
xxx.xxx.xxx.xxx/32 the /32 represents a single IP address. To set one of
these values go to Advanced \> Default Settings and find the Provision
category from there used the edit button to set a value. After this is
done it is safe to set enabled equal to true.

-   [Yealink](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_yealink.html)
-   [Polycom](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_polycom.html)
-   [Cisco](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_cisco.html)
-   [Fanvil](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_fanvil.html)
-   [Grandstream](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_grandstream.html)
-   [Htek](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_htek.html)
-   [Zoiper](http://docs.fusionpbx.com/en/latest/applications/provision/provision_auto_zoiper.html)

## Manual

How to setup the device using the phone\'s web interface.

-   [Yealink](https://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_yealink.html)
-   [Polycom](https://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_polycom.html)
-   [Cisco](http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_cisco.html)
-   [Fanvil](https://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_fanvil.html)
-   [Grandstream](https://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_grandstream.html)
-   [Htek](http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_htek.html)
-   [SNOM](http://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_snom.html)
-   [Zoiper](https://docs.fusionpbx.com/en/latest/applications/provision/provision_manual_zoiper.html)

## Advanced \> Default Settings

In the [Provisioning
section](../advanced/default_settings.md#id17), there are a
few key options that have to be set in order to turn auto provisioning
on.

-   **enabled** Must be enabled and set to **value true** and **enabled
    True**. It is disabled by default.
-   **http_auth_username** Must be enabled and set to **value true** and
    **enabled True**. It is disabled by default. Be sure to use a strong
    username.
-   **http_auth_password** Must be enabled and set to **value true** and
    **enabled True**. It is disabled by default. Be sure to use a strong
    password.
-   **cidr** Optional security option to allow configuration request
    limited to specific IP version 4 ranges. Type array allows multiple
    ranges of IP addresses.

## Phone Screen Capture

-   [Screen
    Capture](https://docs.fusionpbx.com/en/latest/applications/provision/phone_screen_capture.html)

:::: note
<p class="admonition-title">Note</p>

[Click here to view how to add a
device](../accounts/devices.md).
::::

## Phone Book

Remote phone book (Address Book) are based on the FusionPBX [Contacts
App](./contacts.md).

### Phone Book Settings

In order to use the phone book a few steps are needed.

-   Assign the device to a user.
-   Create or import the
    [Contacts](./contacts.md).
-   Set **Enabled** as **True** in [Default
    Settings](../advanced/default_settings.md).

![image](../_static/images/provision/fusionpbx_remote_phonebook1.png)

-   Set **Enabled True** for contact_extensions, contact_users and contact_groups in [Default
    Settings](../advanced/default_settings.md).

![image](../_static/images/provision/fusionpbx_phone_book2.png)

-   From the phone, go into the menu to update the phone book.
