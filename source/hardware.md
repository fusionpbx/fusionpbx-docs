# Hardware

## Auto Provision Phones

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

::: {.toctree maxdepth="4"}
applications/provision/provision[auto_yealink.rst]{#auto_yealink.rst}
applications/provision/provision[auto_polycom.rst]{#auto_polycom.rst}
applications/provision/provision[auto_cisco.rst]{#auto_cisco.rst}
applications/provision/provision[auto_fanvil.rst]{#auto_fanvil.rst}
applications/provision/provision[auto_flyingvoice.rst]{#auto_flyingvoice.rst}
applications/provision/provision[auto_grandstream.rst]{#auto_grandstream.rst}
applications/provision/provision[auto_htek.rst]{#auto_htek.rst}
applications/provision/provision[auto_zoiper.rst]{#auto_zoiper.rst}
applications/provision/provision[auto_snom.rst]{#auto_snom.rst}
applications/provision/provision[auto_avaya.rst]{#auto_avaya.rst}
:::

## Manually Provision Phones

How to setup the device using the phone's web interface.

::: {.toctree maxdepth="4"}
applications/provision/provision[manual_yealink.rst]{#manual_yealink.rst}
applications/provision/provision[manual_polycom.rst]{#manual_polycom.rst}
applications/provision/provision[manual_cisco.rst]{#manual_cisco.rst}
applications/provision/provision[manual_fanvil.rst]{#manual_fanvil.rst}
applications/provision/provision[manual_flyingvoice.rst]{#manual_flyingvoice.rst}
applications/provision/provision[manual_grandstream.rst]{#manual_grandstream.rst}
applications/provision/provision[manual_htek.rst]{#manual_htek.rst}
applications/provision/provision[manual_zoiper.rst]{#manual_zoiper.rst}
applications/provision/phone[screen_capture.rst]{#screen_capture.rst}
:::

Provisioning Variables/Settings ==============================

Each phone has different Fusion Settings that can be applied to
configure the phones to the requirements.

::: {.toctree maxdepth="4"}
applications/provision/provision[variables_snom.rst]{#variables_snom.rst}
:::

## Firewall Devices

Firewall device settings that help with SIP connections.

::: {.toctree maxdepth="4"}
hardware/firewall[devices]{#devices}/asus[rt_ac66u.rst]{#rt_ac66u.rst}
#firewall/firewall[devices]{#devices}/asus[rt_ac66u_sip_alg.rst]{#rt_ac66u_sip_alg.rst}
firewall/firewall[devices]{#devices}/edgerouterx.rst
#firewall/firewall[devices]{#devices}/edgerouterx[alg.rst]{#alg.rst}
firewall/firewall[devices]{#devices}/pfsense.rst
firewall/firewall[devices]{#devices}/sonicwall[tz_soho.rst]{#tz_soho.rst}
#firewall/firewall[devices]{#devices}/sonicwall[tz_soho_sip_alg.rst]{#tz_soho_sip_alg.rst}
firewall/firewall[devices]{#devices}/zyxel.rst
#firewall/firewall[devices]{#devices}/zyxel[sip_alg.rst]{#sip_alg.rst}
firewall/firewall[devices]{#devices}/cisco[ea6500.rst]{#ea6500.rst}
:::
