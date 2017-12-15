##########
Fail2Ban
##########

| For information about Fail2Ban on FreeSWITCH, http://wiki.freeswitch.org/wiki/Fail2ban see their wiki.

| **Logs**
| This will log FusionPBX authentication failures to syslog (AUTH_LOG). This file can be in different places depending on how rsyslog, or syslog is configured.

|**Ubuntu**
| /var/log/auth.log

| **Examples**
| **GUI Login**

| incorrect username

::

 Feb  1 11:35:11 your_hostname FusionPBX: [w.x.y.z] authentication failed for login_username
 

| incorrect password
 
::
 
 Feb  1 12:07:27 your_hostname FusionPBX: [w.x.y.z] authentication failed for superadmin


| **Provisioning**
| Created from the code in /fusionpbx/mod/provision/index.php Please doublecheck this!

::

 Feb  1 12:07:27 your_hostname FusionPBX: [w.x.y.z] provision attempt bad password for AA:BB:CC:DD:EE:FF

| **Setting up Fail2Ban**
| **RegEx**
| You can test the regex with fail2ban-regex

::

 '[hostname] FusionPBX: \[<HOST>\] authentication failed'

|

| **Configuration**
| **Jail Options**

| Every jail can be customized by tuning the following options:

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Name                  | Default               |                                Description                                                                                        |
+=======================+=======================+===================================================================================================================================+
| filter                | Campground            | Name of the filter to be used by the jail to detect matches. Each single match by a filter increments the counter within the jail |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| logpath               | /var/log/messages     | Path to the log file which is provided to the filter                                                                              |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| maxretry              | 3                     | Number of matches (i.e. value of the counter) which triggers ban action on the IP.                                                |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| findtime              | 600 sec               | The counter is set to zero if no match is found within "findtime" seconds.                                                        |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| bantime               | 600 sec               | Duration (in seconds) for IP to be banned for.                                                                                    |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+


|

| **Filter Rules**
| vim /etc/fail2ban/filter.d/fusionpbx.conf

::

 # Fail2Ban configuration file
 #
 # Author: soapee01
 #
 
 [Definition]
 
 # Option:  failregex
 # Notes.:  regex to match the password failures messages in the logfile. The
 #          host must be matched by a group named "host". The tag "<HOST>" can
 #          be used for standard IP/hostname matching and is only an alias for
 #          (?:::f{4,6}:)?(?P<host>[\w\-.^_]+)
 # Values:  TEXT
 #
 #failregex = [hostname] FusionPBX: \[<HOST>\] authentication failed
 #[hostname] variable doesn't seem to work in every case. Do this instead:
 failregex = .* FusionPBX: \[<HOST>\] authentication failed for
           = .* FusionPBX: \[<HOST>\] provision attempt bad password for
 
 # Option:  ignoreregex
 # Notes.:  regex to ignore. If this regex matches, the line is ignored.
 # Values:  TEXT
 #
 ignoreregex =


| add the following to /etc/fail2ban/jail.local

::

 [fusionpbx]
 
 enabled  = true
 port     = 80,443
 protocol = tcp
 filter   = fusionpbx
 logpath  = /var/log/auth.log
 action   = iptables-allports[name=fusionpbx, protocol=all]
 #          sendmail-whois[name=FusionPBX, dest=root, sender=fail2ban@example.org] #no smtp server installed


| Add /etc/fail2ban/filter.d/freeswitch.conf with the contents:

::

 # Fail2Ban configuration file
 #
 # Author: Rupa SChomaker (first two regex)
 
 [Definition]
 
 # Option:  failregex
 # Notes.:  regex to match the password failures messages in the logfile. The
 #          host must be matched by a group named "host". The tag "<HOST>" can
 #          be used for standard IP/hostname matching and is only an alias for
 #          (?:::f{4,6}:)?(?P<host>[\w\-.^_]+)
 # Values:  TEXT
 #
 failregex = \[WARNING\] sofia_reg.c:\d+ SIP auth failure \(REGISTER\) on sofia profile \'\w+\' for \[.*\] from ip <HOST>
             \[WARNING\] sofia_reg.c:\d+ SIP auth failure \(INVITE\) on sofia profile \'\w+\' for \[.*\] from ip <HOST>
             \[WARNING\] sofia_reg.c:\d+ SIP auth challenge \(REGISTER\) on sofia profile \'\w+\' for \[.*\] from ip <HOST>
 
 # Option:  ignoreregex
 # Notes.:  regex to ignore. If this regex matches, the line is ignored.
 # Values:  TEXT
 #
 ignoreregex =


| Modify /etc/fail2ban/jail.conf. Add the following make sure the freeswitch.log file path is correct.

::

 [freeswitch-tcp]
 
 enabled  = true
 port     = 5060,5061,5080,5081
 protocol = tcp
 filter   = freeswitch
 logpath  = /usr/local/freeswitch/log/freeswitch.log
 action   = iptables-allports[name=freeswitch-tcp, protocol=all]
            sendmail-whois[name=FreeSwitch, dest=root, sender=fail2ban@example.org]
 
 [freeswitch-udp]
 
 enabled  = true
 port     = 5060,5061,5080,5081
 protocol = udp
 filter   = freeswitch
 logpath  = /usr/local/freeswitch/log/freeswitch/freeswitch.log
 action   = iptables-allports[name=freeswitch-udp, protocol=all]
            sendmail-whois[name=FreeSwitch, dest=root, sender=fail2ban@example.org]


| /var/log/fail2ban.log will log this after 3 missed logins.

::

 2011-02-01 12:32:18,151 fail2ban.actions: WARNING [fusionpbx] Ban 192.168.100.1
 

| hostname # iptables -n -L fail2ban-fusionpbx

::

 Chain fail2ban-fusionpbx (1 referecnes)
 target    prot opt source        destination
 DROP      all  --  192.168.100.1 anywhere
 RETURN    all  --  anywhere      anywhere


| **Important**
| **You can easily ban yourself, including current active ssh connections.**
| **To unban:**

::

 hostname # iptables -n -D fail2ban-fusionpbx 1

| **Keep yourself from getting banned.**
| add to /etc/fail2ban/jail.local

::

 [DEFAULT]
 
 # "ignoreip" can be an IP address, a CIDR mask or a DNS host
 ignoreip = 127.0.0.1 192.168.0.99
 bantime  = 600
 maxretry = 3


| **Errors**
| If you're seeing something like this in your fail2ban logfile:

::
 
 2011-02-27 14:11:42,326 fail2ban.actions.action: ERROR  iptables -N fail2ban-freeswitch-tcp


| add the time.sleep(0.1) to /usr/bin/fail2ban-client

::

 def __processCmd(self, cmd, showRet = True):
 beautifier = Beautifier()
 for c in cmd:
 '''time.sleep(0.1)'''
 beautifier.setInputCmd(c)

| or

::

 sed -i -e s,beautifier\.setInputCmd\(c\),'time.sleep\(0\.1\)\n\t\t\tbeautifier.setInputCmd\(c\)', /usr/bin/fail2ban-client

| http://www.fail2ban.org/wiki/index.php/Fail2ban_talk:Community_Portal#fail2ban.action.action_ERROR_on_startup
