#######
Avaya
#######

Using DHCP Option 242 to Deploy the Phone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

DHCP is an excellent option for phones deployed in a local office. Your Avaya phone can be removed from its box and simply plugged into the network. All the setting will be retrieved from the server.

Avaya phones look for DHCP option 242 for auto-provisioning. 242 needs to be of type _string_.

Here is a sample string: "HTTPSRVR=company.domain.com,HTTPDIR=/app/provision,FORCE_HTTP_AUTH_USERNAME=admin,FORCE_HTTP_AUTH_PASSWORD=password,DES_STAT=0"

Below is an explanation of all of the Key-values:

1. HTTPSRVR - The fqdn of the provisioning server
2. HTTPDIR - The folder that the phone should look for the provisioning files 
3. FORCE_HTTP_AUTH_USERNAME - HTTP username (optional)
4. FORCE_HTTP_AUTH_PASSWORD - HTTP password (optional)
5. DES_STAT - Set to 0 to disable Avaya's Device Enrollment Service


When a phone boots up and retrieves option 242, it will first begin looking for the `J100Supgrade.txt` file inside of the HTTPDIR. This file contains a pointer to the MAC specific file that has the extension settings.


Using DHCP Option 242 to Set the VLAN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One method of getting phones to switch to the voice vlan is through the use of DHCP.

Avaya looks for option 242 (string) for the VLAN ID that it should be on. This is accomplished by adding the following to option 242: "L2Q=1,L2QVLAN=11,VLANTEST=0"

Below is an explanation of all of the Key-values:

1. L2Q - This is a true (1) or false (0) as to if vlan tagging should be used.
2. L2QVLAN - This is the vlan id
3. VLANTEST - Specifies the number of seconds that the phone waits prior to failing back to a different VLAN ID if no response is received from the DHCP server

When a phone boots, if you have option 242 set to "xxx" where xxx is your vlan id, the phone will release it's address lease and request a new one with it's frames tagged with the vlan ID.

This option is needed on the default vlan DHCP scope to make the phone switch.