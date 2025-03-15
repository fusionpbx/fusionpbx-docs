# Hardware

## Auto Provision Phones

Auto provisioning is disabled by default. This is to give a chance to secure provisioning server with HTTP Authentication or CIDR. HTTP Authentication requires the phone to send hash of the combined username and password in order to get configuration. CIDR is an IP address restriction that can be used to restrict which IP addresses are allowed to get the device configuration. An example of CIDR is xxx.xxx.xxx.xxx/32 the /32 represents a single IP address. To set one of these values go to Advanced > Default Settings and find the Provision category from there used the edit button to set a value. After this is done it is safe to set enabled equal to true.

```{toctree}
:maxdepth: 4
  
applications/provision/provision_auto_yealink.md
applications/provision/provision_auto_polycom.md
applications/provision/provision_auto_cisco.md
applications/provision/provision_auto_fanvil.md
applications/provision/provision_auto_flyingvoice.md
applications/provision/provision_auto_grandstream.md
applications/provision/provision_auto_htek.md
applications/provision/provision_auto_zoiper.md
applications/provision/provision_auto_snom.md
applications/provision/provision_auto_avaya.md
```

## Manually Provision Phones

How to setup the device using the phone’s web interface.

```{toctree}
:maxdepth: 4
  
applications/provision/provision_manual_yealink.md
applications/provision/provision_manual_polycom.md
applications/provision/provision_manual_cisco.md
applications/provision/provision_manual_fanvil.md
applications/provision/provision_manual_flyingvoice.md
applications/provision/provision_manual_grandstream.md
applications/provision/provision_manual_htek.md
applications/provision/provision_manual_zoiper.md
applications/provision/phone_screen_capture.md
```

## Provisioning Variables/Settings

Each phone has different Fusion Settings that can be applied to configure the phones to the requirements.

```{toctree}
:maxdepth: 4
  
applications/provision/provision_variables_snom.md
```

## Firewall Devices

Firewall device settings that help with SIP connections.

```{toctree}
:maxdepth: 4
   
hardware/firewall_devices/asus_rt_ac66u.md
#firewall/firewall_devices/asus_rt_ac66u_sip_alg.md
firewall/firewall_devices/edgerouterx.md
#firewall/firewall_devices/edgerouterx_alg.md
firewall/firewall_devices/pfsense.md
firewall/firewall_devices/sonicwall_tz_soho.md
#firewall/firewall_devices/sonicwall_tz_soho_sip_alg.md
firewall/firewall_devices/zyxel.md
#firewall/firewall_devices/zyxel_sip_alg.md
firewall/firewall_devices/cisco_ea6500.md
```
