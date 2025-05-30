# Cisco

## SPA

The following information can be used to provisioning Cisco SPA phones.

## Basic URL

An example URL for provisioning URL for a Cisco SPA.

<http://mydomain.com/app/provision/?mac=$MA>

## HTTP Authentication

Phone web interface -\> Provision - \> Profile Rule

    [--uid myUser --pwd myPass]http://mydomain.com/app/provision/?mac=$MA

## HTTPS

Requires a Cisco Certificate that you will likely need to obtain from a
Cisco distributor.

## Browser Command

Use your web browser to send the following command to pass the provision
the phone now and this will pass URL to the phone so it has the location
neeeded for provisioning the device. In this example 192.168.1.5 is the
IP address of the phone and domain.com needs updated to use the correct
tenant domain name.

**No HTTP Authentication**

<http://192.168.1.5/admin/resync?http://your.domain.com/app/provision/?mac=$MA>

**With HTTP Authentication**

<http://192.168.1.4/admin/resync?%5B--uid+admin+--pwd+555%5Dhttp://your.domain.com/app/provision/?mac=$MA>

## DHCP Option

Use the DHCP Option 66 to deliver the provisioning URL to the phones
without using the web interface.

**ISC DHCP**
```
/etc/dhcp/dhcpd.conf
```
Add the following. Make sure to update the IP range of 192.168.1.0 to match your network and your FusionPBX domain name or IP address.
```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.120;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 8.8.4.4;
  default-lease-time 600;
  max-lease-time 7200;
  option www-server 192.168.1.11;
  option tftp-server-name "http://192.168.1.11/app/provision/?mac=$MA";
}
```

## Additional Information

More information can also be found at
<https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/csbpvga/spa100-200/provisioning/guide/SPA100-200_Provisioning.pdf>
