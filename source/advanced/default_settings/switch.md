# Switch

Switch specific default settings. These defaults will change depending
if you compiled the SWITCH source or used the newest default of
packages.

+------------+---------+---------------+----------+-----------------+
| default[se | d       | default[sett  | de       | defau           |
| tting_subc | efault[ | ing_value]{#s | fault[se | lt[setting_desc |
| ategory]{# | setting | etting_value} | tting_en | ription]{#setti |
| setting_su | _name]{ |               | abled]{# | ng_description} |
| bcategory} | #settin |               | setting_ |                 |
|            | g_name} |               | enabled} |                 |
+============+=========+===============+==========+=================+
| bin        | dir     |               | TRUE     | > Server path   |
|            |         |               |          | > for bin.      |
+------------+---------+---------------+----------+-----------------+
| base       | dir     | /usr          | TRUE     | > Server path   |
|            |         |               |          | > for base.     |
+------------+---------+---------------+----------+-----------------+
| c          | dir     | /etc          | FALSE    | > Server path   |
| all[center |         | /freeswitch/a |          | > for Call      |
| ]{#center} |         | utoload[confi |          | > Center.       |
|            |         | gs]{#configs} |          |                 |
+------------+---------+---------------+----------+-----------------+
| conf       | dir     | /e            | TRUE     | > Server path   |
|            |         | tc/freeswitch |          | > for Conf      |
|            |         |               |          | > files.        |
+------------+---------+---------------+----------+-----------------+
| db         | dir     | /var/lib/     | TRUE     | > Server path   |
|            |         | freeswitch/db |          | > for sqlite db |
|            |         |               |          | > files.        |
+------------+---------+---------------+----------+-----------------+
| dialplan   | dir     | /etc/freesw   | FALSE    | > Server path   |
|            |         | itch/dialplan |          | > for xml       |
|            |         |               |          | > dialplan      |
+------------+---------+---------------+----------+-----------------+
| extensions | dir     | /etc/freeswi  | FALSE    | > Server path   |
|            |         | tch/directory |          | > for extension |
|            |         |               |          | > directory.    |
+------------+---------+---------------+----------+-----------------+
| grammar    | dir     | /us           | TRUE     | > Server path   |
|            |         | r/share/frees |          | > for grammar   |
|            |         | witch/grammar |          | > xml.          |
+------------+---------+---------------+----------+-----------------+
| log        | dir     | /var/l        | TRUE     | > Server path   |
|            |         | og/freeswitch |          | > for SWITCH    |
|            |         |               |          | > logs.         |
+------------+---------+---------------+----------+-----------------+
| mod        | dir     | /usr/lib/f    | TRUE     | > Server path   |
|            |         | reeswitch/mod |          | > for SWITCH    |
|            |         |               |          | > mod\'s.       |
+------------+---------+---------------+----------+-----------------+
| phrases    | dir     | /etc/fr       | TRUE     | > Server path   |
|            |         | eeswitch/lang |          | > for SWITCH    |
|            |         |               |          | > xml phrases.  |
+------------+---------+---------------+----------+-----------------+
| recordings | dir     | /var          | TRUE     | > Server path   |
|            |         | /lib/freeswit |          | > for SWITCH    |
|            |         | ch/recordings |          | > recordings.   |
+------------+---------+---------------+----------+-----------------+
| scripts    | dir     | /us           | TRUE     | > Server path   |
|            |         | r/share/frees |          | > for SWITCH    |
|            |         | witch/scripts |          | > scripts.      |
+------------+---------+---------------+----------+-----------------+
| sip[       | dir     | /             | FALSE    | > Server path   |
| profiles]{ |         | etc/freeswitc |          | > for SWITCH    |
| #profiles} |         | h/sip[profile |          | > xml sip       |
|            |         | s]{#profiles} |          | > profiles.     |
+------------+---------+---------------+----------+-----------------+
| sounds     | dir     | /u            | TRUE     | > Server path   |
|            |         | sr/share/free |          | > for SWITCH    |
|            |         | switch/sounds |          | > sounds.       |
+------------+---------+---------------+----------+-----------------+
| storage    | dir     | /             | TRUE     | > Server path   |
|            |         | var/lib/frees |          | > for SWITCH    |
|            |         | witch/storage |          | > storage.      |
+------------+---------+---------------+----------+-----------------+
| voicemail  | dir     | /var/lib/fr   | TRUE     | Server path for |
|            |         | eeswitch/stor |          | SWITCH          |
|            |         | age/voicemail |          | voicemails.     |
+------------+---------+---------------+----------+-----------------+
