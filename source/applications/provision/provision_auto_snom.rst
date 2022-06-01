#######
SNOM
#######



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

http://voice.example.com/fusionpbx/app/provision/index.php?mac=00041326B92B

Replace the mac address and domain with your own. 


From your SNOM phone
^^^^^^^^^^^^^^^^^^^^^^

Snom like most IP phone has a web admin interface to configure and monitor the phone. Usually, it's best to be up-to-date with firmware.  If you have issues with provisioning check that the device is up-to-date.  Sometimes 1 or 2 versions back are needed also depending on firmware bugs.

1. To find the IP address of the phone, press the menu button on the phone (on the 7XX or 8XX series, or the settings button on the 3xx series) and press "4" for network then "1" for IP Settings and at the DHCP screen, press "X" for no. The IP address will appear on the screen.

2. Type the IP address into your web browser and select "Setup > Advanced" from the left menu and select the "Update" tab from the top.

3. Under "Update Policy", select "Update Automatically"

4. Under "Setting URL" add in the setting URL as:

http://www.example.com/app/provision/index.php?mac={mac}

The hostname should be replaced with your FusionPBX domain name. Note that we have replaced the domain name with {mac}. This is a special Snom variable to put the phones Mac address in without having to specify it.

5. Select the "Apply" button and then the "Reboot" button and confirm to reboot the phone.

When the phone reboots, it will be provisioned with your appropriate settings 



Using DHCP Option 66 to Deploy the Phone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DHCP is an excellent option for phones deployed in a local office. Your Snom phone can be removed from its box and simply plugged into the network. All the setting will be retrieved from the server. Be careful to not open up your FusionPBX to the internet though. Someone who knows your url and a MAC address of a phone can easily retrieve your phone settings including its password.

Each DHCP Server is different. At Helia we use Cradlepoint MBR 1400 and Cradlepoint MBR 95. Each of these allow you to setup DHCP option 66. Setting up DHCP directly on the voice server is also an option.

1. On the Cradlepoint MBR 1400 router, select "Network Settings" and " WiFi / Local Networks".

2. Select the appropriate "Local IP Networks", and select the "Edit" button.

3. On the "Local Network Editor" window, select the "DHCP Server" tab

4. Ensure the "DHCP Enable" checkbox is checked and click the "Add" button to add an option.

5. For "option" select "66 Server Name" and for the value, add the provisioning URL:

hxxp://www.example.com/app/provision/index.php?mac={mac} (Be sure to replace hxxp:// with http://)

The hostname should be replaced with your FusionPBX domain name. Note that we have replaced the domain name with {mac}. This is a special Snom variable to put the phones Mac address in without having to specify it.

With the DHCP information added, the provisioning template will be applied to the phone next time it fetches a new IP address - usually on its next reboot. 




