#######
SNOM
#######



Snom Provisioning URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In versions of FusionPBX older than 5.3, Snom phones used a different provisioning URL. This has been changed in version 5.3 to make the URL compatible with other vendors.

The new method requires changes to your nginx config file to use.

Old Method: https://voice.example.com/app/provision/index.php?mac=00041326B92B

New Method: https://voice.example.com/app/provision/

This URL can also have HTTP Auth credentials added to it by doing the following:

https://admin:password@voice.example.com/app/provision/




From your FusionPBX Install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. From the Accounts menu, select extensions and select an extension to be provisioned. If no extension exists, create one.

2. Click the triangle beside **Device Provisioning** field then enter the mac address of the phone device into **MAC Address** field.

3. A barcode scanner can be used or type in the mac address 00041326B92B manually.

4. From the template dropdown list, select the proper make and model of the phone.

5. Click the Save button.

6. The mac address should be a clickable link now. Click that then continue to set up line keys or adjust any other phone settings.

.. note::

        The provisioning template can be tested by opening up a web browser and entering the provisioning url. The provisioning url is:

http://voice.example.com/app/provision/index.php?mac=00041326B92B

Replace the mac address and domain with your own. 




Manual Method via Web Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Snom like most IP phone has a web admin interface to configure and monitor the phone. Usually, it's best to be up-to-date with firmware.  If you have issues with provisioning check that the device is up-to-date.  Sometimes 1 or 2 versions back are needed also depending on firmware bugs.

1. Type the IP address into your web browser and select "Setup > Advanced" from the left menu and select the "Update" tab from the top.

2. Under "Update Policy", select "Update Automatically"

3. Under "Setting URL" add in the setting URL as:

https://voice.example.com/app/provision/

Note: The hostname should be replaced with your FusionPBX domain name.

4. Select the "Apply" button.

5. If using HTTP Auth, go to "Setup > Advanced > QoS / Security"

In HTTP Client, enter the username found in `http_auth_username` and the password found in `http_auth_password`.

6. Click the "Reboot" button and confirm to reboot the phone.

When the phone reboots, it will be provisioned with your appropriate settings.




Using DHCP Option 66 to Deploy the Phone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DHCP is an excellent option for phones deployed in a local office. Your Snom phone can be removed from its box and simply plugged into the network. All the setting will be retrieved from the server. Be careful when exposing your FusionPBX server to the internet. You should always have the `http_auth_username` and `http_auth_password` default settings enabled and with strong settings.

Your DHCP option should look something like this:

https://http_auth_username:http_auth_password@voice.example.com/app/provision/




Using DHCP Option 132 to Set the VLAN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One method of getting phones to switch to the voice vlan is through the use of DHCP.

Snom looks for option 132 (string) for the VLAN ID that it should be on.

When a phone boots, if you have option 132 set to "xxx" where xxx is your vlan id, the phone will release it's address lease and request a new one with it's frames tagged with the vlan ID.

This option is needed on the default vlan DHCP scope to make the phone switch.
