# Provision

In the Provisioning section, there are a few key options that have to be
set in order to turn auto provisioning on.

-   **enabled:** Must be enabled and set to **value true** and **enabled
    True**. It is disabled by default.
-   **http_auth_username:** Must be enabled and set to your desired
    admin username and **enabled True**. It is disabled by default. Be
    sure to use a strong username.
-   **http_auth_password:** Must be enabled and set to your desired
    admin password and **enabled True**. It is disabled by default. Be
    sure to use a strong password.

+--------+---+----------------------+---+-----------------------------+
| D      | D | Default Setting      | D | Default Setting Description |
| efault | e | Value                | e |                             |
| S      | f |                      | f |                             |
| etting | a |                      | a |                             |
| Subca  | u |                      | u |                             |
| tegory | l |                      | l |                             |
|        | t |                      | t |                             |
|        | S |                      | S |                             |
|        | e |                      | e |                             |
|        | t |                      | t |                             |
|        | t |                      | t |                             |
|        | i |                      | i |                             |
|        | n |                      | n |                             |
|        | g |                      | g |                             |
|        | N |                      | E |                             |
|        | a |                      | n |                             |
|        | m |                      | a |                             |
|        | e |                      | b |                             |
|        |   |                      | l |                             |
|        |   |                      | e |                             |
|        |   |                      | d |                             |
+========+===+======================+===+=============================+
| fanvi  | t | -20                  | T | Time zone ranges            |
| l[time | e |                      | R |                             |
| _zone] | x |                      | U |                             |
| {#time | t |                      | E |                             |
| _zone} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | t | UTC-5                | T | Time zone name example      |
| vil[ti | e |                      | R | United States-Eastern Time  |
| me_zon | x |                      | U |                             |
| e_name | t |                      | E |                             |
| ]{#tim |   |                      |   |                             |
| e_zone |   |                      |   |                             |
| _name} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | n | 4                    | T | Used with time zone and     |
| vil[lo | u |                      | R | time zone name              |
| cation | m |                      | U |                             |
| ]{#loc | e |                      | E |                             |
| ation} | r |                      |   |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | t | enter a value        | F | enter a value               |
| vil[re | e |                      | A |                             |
| alm]{# | x |                      | L |                             |
| realm} | t |                      | S |                             |
|        |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | t | FusionPBX            | T | Name at top left of screen  |
| vil[gr | e |                      | R | 0\~12 characters            |
| eeting | x |                      | U |                             |
| ]{#gre | t |                      | E |                             |
| eting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fanvi  | n | 3                    | T | value 0-13 Date Format      |
| l[date | u |                      | R |                             |
| _displ | m |                      | U |                             |
| ay]{#d | e |                      | E |                             |
| ate_di | r |                      |   |                             |
| splay} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fanvi  | n | 1                    | T | 1=12hr 0=24hr               |
| l[time | u |                      | R |                             |
| _displ | m |                      | U |                             |
| ay]{#t | e |                      | E |                             |
| ime_di | r |                      |   |                             |
| splay} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | n | 0                    | T | 1=on 0=off                  |
| vil[wi | u |                      | R |                             |
| fi_ena | m |                      | U |                             |
| ble]{# | e |                      | E |                             |
| wifi_e | r |                      |   |                             |
| nable} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fanvi  | n | 3478                 | T | enter a stun port number    |
| l[stun | u |                      | R |                             |
| _port] | m |                      | U |                             |
| {#stun | e |                      | E |                             |
| _port} | r |                      |   |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 0                    | T | Call Waiting 0=enabled      |
| dstrea | e |                      | R | 1=disable                   |
| m[call | x |                      | U |                             |
| _waiti | t |                      | E |                             |
| ng]{#c |   |                      |   |                             |
| all_wa |   |                      |   |                             |
| iting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| cont   | b | TRUE                 | F | Enable Address Book for     |
| act[gr | o |                      | A | Grandstream based on users  |
| andstr | o |                      | L | and groups assigned to      |
| eam]{# | l |                      | S | contact.                    |
| grands | e |                      | E |                             |
| tream} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | auto                 | T | See provision profile for   |
| tream[ | e |                      | R | codes.                      |
| gxp_ti | x |                      | U |                             |
| me_zon | t |                      | E |                             |
| e]{#gx |   |                      |   |                             |
| p_time |   |                      |   |                             |
| _zone} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | 1                    | T | GXV Android phones - fix    |
| andstr | e |                      | R | auto-ring bug.              |
| eam[ch | x |                      | U |                             |
| eck_si | t |                      | E |                             |
| p_user |   |                      |   |                             |
| _id]{# |   |                      |   |                             |
| check_ |   |                      |   |                             |
| sip_us |   |                      |   |                             |
| er_id} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | none                 | F | mydomain.com/app/provision  |
| dstrea | e |                      | A | to Fusionpbx provisioning.  |
| m[conf | x |                      | L | Phones will use firmware    |
| ig_ser | t |                      | S | url if this is set to: none |
| ver_pa |   |                      | E |                             |
| th]{#c |   |                      |   |                             |
| onfig_ |   |                      |   |                             |
| server |   |                      |   |                             |
| _path} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | mydoma               | T | Grandstream firmware and    |
| tream[ | e | in.com/app/provision | R | provision.                  |
| firmwa | x |                      | U |                             |
| re_pat | t |                      | E |                             |
| h]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _path} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 1                    | F | Default VLAN for phone LAN  |
| tream[ | e |                      | A | port.                       |
| lan_po | x |                      | L |                             |
| rt_vla | t |                      | S |                             |
| n]{#la |   |                      | E |                             |
| n_port |   |                      |   |                             |
| _vlan} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 1                    | F | Default VLAN for phone PC   |
| dstrea | e |                      | A | port.                       |
| m[pc_p | x |                      | L |                             |
| ort_vl | t |                      | S |                             |
| an]{#p |   |                      | E |                             |
| c_port |   |                      |   |                             |
| _vlan} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | dc=mydomain,dc=com   | F | Base DN                     |
| dstrea | e |                      | A |                             |
| m[ldap | x |                      | L |                             |
| _base_ | t |                      | S |                             |
| dn]{#l |   |                      | E |                             |
| dap_ba |   |                      |   |                             |
| se_dn} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | givenName sn title   | F | Which named attributes to   |
| andstr | e |                      | A | display on device. Must be  |
| eam[ld | x |                      | L | pulled in through           |
| ap_dis | t |                      | S | grandstream[ldap_n          |
| play_n |   |                      | E | ame_attr]{#ldap_name_attr}. |
| ame]{# |   |                      |   |                             |
| ldap_d |   |                      |   |                             |
| isplay |   |                      |   |                             |
| _name} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | mail                 | F | Mail attribute returned to  |
| andstr | e |                      | A | phone                       |
| eam[ld | x |                      | L |                             |
| ap_mai | t |                      | S |                             |
| l_attr |   |                      | E |                             |
| ]{#lda |   |                      |   |                             |
| p_mail |   |                      |   |                             |
| _attr} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | (mail=%)             | F | Search filter for mail      |
| tream[ | e |                      | A | lookups                     |
| ldap_m | x |                      | L |                             |
| ail_fi | t |                      | S |                             |
| lter]{ |   |                      | E |                             |
| #ldap_ |   |                      |   |                             |
| mail_f |   |                      |   |                             |
| ilter} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | givenName sn title   | F | The NAME attributes         |
| andstr | e | mail                 | A | returned in the LDAP search |
| eam[ld | x |                      | L | result available to device  |
| ap_nam | t |                      | S |                             |
| e_attr |   |                      | E |                             |
| ]{#lda |   |                      |   |                             |
| p_name |   |                      |   |                             |
| _attr} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | (cn=%)               | F | Search filter for name      |
| tream[ | e |                      | A | lookups                     |
| ldap_n | x |                      | L |                             |
| ame_fi | t |                      | S |                             |
| lter]{ |   |                      | E |                             |
| #ldap_ |   |                      |   |                             |
| name_f |   |                      |   |                             |
| ilter} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | telephoneNumber      | F | Number attributes returned  |
| tream[ | e | mobile homePhone     | A | to the phone.               |
| ldap_n | x |                      | L |                             |
| umber_ | t |                      | S |                             |
| attr]{ |   |                      | E |                             |
| #ldap_ |   |                      |   |                             |
| number |   |                      |   |                             |
| _attr} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | (\|(te               | F | Search filter for number    |
| dstrea | e | lephoneNumber=%)(hom | A | lookups.                    |
| m[ldap | x | ePhone=%)(moblie=%)) | L |                             |
| _numbe | t |                      | S |                             |
| r_filt |   |                      | E |                             |
| er]{#l |   |                      |   |                             |
| dap_nu |   |                      |   |                             |
| mber_f |   |                      |   |                             |
| ilter} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | super-secret         | F | Ldap bind user password.    |
| tream[ | e |                      | A |                             |
| ldap_p | x |                      | L |                             |
| asswor | t |                      | S |                             |
| d]{#ld |   |                      | E |                             |
| ap_pas |   |                      |   |                             |
| sword} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | mydomain.com         | F | Ldap server host name       |
| andstr | e |                      | A |                             |
| eam[ld | x |                      | L |                             |
| ap_ser | t |                      | S |                             |
| ver]{# |   |                      | E |                             |
| ldap_s |   |                      |   |                             |
| erver} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | ou=user              | F | Ldap base for users.        |
| andstr | e | s,dc=mydomain,dc=com | A |                             |
| eam[ld | x |                      | L |                             |
| ap_use | t |                      | S |                             |
| r_base |   |                      | E |                             |
| ]{#lda |   |                      |   |                             |
| p_user |   |                      |   |                             |
| _base} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | cn=pbxadmi           | F | Ldap server bind username   |
| tream[ | e | n,dc=mydomain,dc=com | A |                             |
| ldap_u | x |                      | L |                             |
| sernam | t |                      | S |                             |
| e]{#ld |   |                      | E |                             |
| ap_use |   |                      |   |                             |
| rname} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 720                  | T | 0=disabled, 5-720 minutes   |
| dstrea | e |                      | R |                             |
| m[phon | x |                      | U |                             |
| ebook_ | t |                      | E |                             |
| downlo |   |                      |   |                             |
| ad_int |   |                      |   |                             |
| erval] |   |                      |   |                             |
| {#phon |   |                      |   |                             |
| ebook_ |   |                      |   |                             |
| downlo |   |                      |   |                             |
| ad_int |   |                      |   |                             |
| erval} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 5                    | F | Layer 2 QoS 802.1p Priority |
| tream[ | e |                      | A | Value for RTP media         |
| qos_rt | x |                      | L |                             |
| p]{#qo | t |                      | S |                             |
| s_rtp} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 3                    | F | Layer 2 QoS 802.1p Priority |
| tream[ | e |                      | A | Value for SIP signaling     |
| qos_si | x |                      | L |                             |
| p]{#qo | t |                      | S |                             |
| s_sip} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 1                    | T | GXV Android phones - fix    |
| tream[ | e |                      | R | auto-ring bug.              |
| sip_on | x |                      | U |                             |
| ly_kno | t |                      | E |                             |
| wn_ser |   |                      |   |                             |
| vers]{ |   |                      |   |                             |
| #sip_o |   |                      |   |                             |
| nly_kn |   |                      |   |                             |
| own_se |   |                      |   |                             |
| rvers} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | mydomain.com         | T | Bug in Grandstream where    |
| andstr | e |                      | R | null stun[server]{#server}  |
| eam[st | x |                      | U | defaults to sip server/port |
| un_ser | t |                      | E |                             |
| ver]{# |   |                      |   |                             |
| stun_s |   |                      |   |                             |
| erver} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 1                    | T | GXV Android phones - fix    |
| dstrea | e |                      | R | auto-ring bug.              |
| m[vali | x |                      | U |                             |
| date_i | t |                      | E |                             |
| ncomin |   |                      |   |                             |
| g_sip] |   |                      |   |                             |
| {#vali |   |                      |   |                             |
| date_i |   |                      |   |                             |
| ncomin |   |                      |   |                             |
| g_sip} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | <h                   | F | Wallpaper Image JPEG        |
| tream[ | e | ttps://mydomain.com/ | A | 480x272 16-bit depth        |
| wallpa | x | files/wallpaper.jpg> | L | dithered                    |
| per_ur | t |                      | S |                             |
| l]{#wa |   |                      | E |                             |
| llpape |   |                      |   |                             |
| r_url} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 1                    | F | Bluetooth Power - 0 - Off,  |
| dstrea | e |                      | A | 1 - On, 2 - Off & Hide Menu |
| m[blue | x |                      | L | From LCD                    |
| tooth_ | t |                      | S |                             |
| power] |   |                      | E |                             |
| {#blue |   |                      |   |                             |
| tooth_ |   |                      |   |                             |
| power} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 1                    | F | Bluetooth Handsfree - 0 -   |
| tream[ | e |                      | A | Off, 1 - On                 |
| blueto | x |                      | L |                             |
| oth_ha | t |                      | S |                             |
| ndsfre |   |                      | E |                             |
| e]{#bl |   |                      |   |                             |
| uetoot |   |                      |   |                             |
| h_hand |   |                      |   |                             |
| sfree} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 1                    | T | Attended Transfer Mode. 0 - |
| tream[ | e |                      | R | Static, 1 - Dynamic.        |
| auto_a | x |                      | U | Default is 0                |
| ttende | t |                      | E |                             |
| d_tran |   |                      |   |                             |
| sfer]{ |   |                      |   |                             |
| #auto_ |   |                      |   |                             |
| attend |   |                      |   |                             |
| ed_tra |   |                      |   |                             |
| nsfer} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t |                      | F | Syslog Server (name of the  |
| tream[ | e |                      | A | server, max length is 64    |
| syslog | x |                      | L | characters)                 |
| _serve | t |                      | S |                             |
| r]{#sy |   |                      | E |                             |
| slog_s |   |                      |   |                             |
| erver} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 0                    | F | Syslog Level. 0 - NONE, 1 - |
| dstrea | e |                      | A | DEBUG, 2 - INFO, 3 -        |
| m[sysl | x |                      | L | WARNING, 4 - ERROR. Default |
| og_lev | t |                      | S | is 0                        |
| el]{#s |   |                      | E |                             |
| yslog_ |   |                      |   |                             |
| level} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 0                    | F | Send SIP Log. 0 - Do not    |
| dstrea | e |                      | A | send SIP log in Syslog, 1 - |
| m[send | x |                      | L | Send SIP log in Syslog if   |
| _sip_l | t |                      | S | configured and set to DEBUG |
| og]{#s |   |                      | E | level. Default is 0         |
| end_si |   |                      |   |                             |
| p_log} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | 1                    | T | Screensaver. 0 - No, 1 -    |
| andstr | e |                      | R | Yes, 2 - On if no VPK is    |
| eam[sc | x |                      | U | active. Default is 1        |
| reensa | t |                      | E |                             |
| ver]{# |   |                      |   |                             |
| screen |   |                      |   |                             |
| saver} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 0                    | T | Screensaver Source. 0 -     |
| dstrea | e |                      | R | Default, 1 - USB, 2 -       |
| m[scre | x |                      | U | Download. Default is 0.     |
| ensave | t |                      | E | \--for GXP2140/2160/2170    |
| r_sour |   |                      |   | only                        |
| ce]{#s |   |                      |   |                             |
| creens |   |                      |   |                             |
| aver_s |   |                      |   |                             |
| ource} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | 1                    | T | Show Date and Time. 0 - No, |
| andstr | e |                      | R | 1 - Yes. Default is 1       |
| eam[sc | x |                      | U |                             |
| reensa | t |                      | E |                             |
| ver_sh |   |                      |   |                             |
| ow_dat |   |                      |   |                             |
| e_time |   |                      |   |                             |
| ]{#scr |   |                      |   |                             |
| eensav |   |                      |   |                             |
| er_sho |   |                      |   |                             |
| w_date |   |                      |   |                             |
| _time} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 5                    | T | Screensaver Timeout.        |
| tream[ | e |                      | R | Minutes 3-60                |
| screen | x |                      | U |                             |
| saver_ | t |                      | E |                             |
| timeou |   |                      |   |                             |
| t]{#sc |   |                      |   |                             |
| reensa |   |                      |   |                             |
| ver_ti |   |                      |   |                             |
| meout} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t |                      | F | Screensaver Server Path     |
| andstr | e |                      | A |                             |
| eam[sc | x |                      | L |                             |
| reensa | t |                      | S |                             |
| ver_se |   |                      | E |                             |
| rver_p |   |                      |   |                             |
| ath]{# |   |                      |   |                             |
| screen |   |                      |   |                             |
| saver_ |   |                      |   |                             |
| server |   |                      |   |                             |
| _path} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | 0                    | F | Screensaver XML Download    |
| dstrea | e |                      | A | Interval Number: 5 - 720.   |
| m[scre | x |                      | L | Default is 0 (disable auto  |
| ensave | t |                      | S | downloading)                |
| r_xml_ |   |                      | E |                             |
| downlo |   |                      |   |                             |
| ad_int |   |                      |   |                             |
| erval] |   |                      |   |                             |
| {#scre |   |                      |   |                             |
| ensave |   |                      |   |                             |
| r_xml_ |   |                      |   |                             |
| downlo |   |                      |   |                             |
| ad_int |   |                      |   |                             |
| erval} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 0                    | T | SRTP Mode. 0 - Disabled,    |
| tream[ | e |                      | R | 1 - Enabled but not forced, |
| srtp]{ | x |                      | U | 2 - Enabled and forced, 3 - |
| #srtp} | t |                      | E | Optional. Default is 0      |
+--------+---+----------------------+---+-----------------------------+
| hte    | t | 18                   | T | Time zone 18=EST 14=CST     |
| k[time | e |                      | R | 6=PST 9,10=MST              |
| _zone] | x |                      | U |                             |
| {#time | t |                      | E |                             |
| _zone} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| hte    | n | 1                    | T | DST off=0 on=1 auto=2       |
| k[dst] | u |                      | R |                             |
| {#dst} | m |                      | U |                             |
|        | e |                      | E |                             |
|        | r |                      |   |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| htek[  | n | 1                    | T | Year-Month-Day=0            |
| date_d | u |                      | R | Month-Day-Year=1            |
| isplay | m |                      | U | Day-Month-Year=2            |
| _forma | e |                      | E |                             |
| t]{#da | r |                      |   |                             |
| te_dis | i |                      |   |                             |
| play_f | c |                      |   |                             |
| ormat} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| h      | n | 1                    | T | 1=12hr 0=24hr               |
| tek[ti | u |                      | R |                             |
| me_for | m |                      | U |                             |
| mat]{# | e |                      | E |                             |
| time_f | r |                      |   |                             |
| ormat} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| poly   | t | \[*\]xxxx\|\[2-9\    | F |                             |
| com[di | e | ]11\|0T\|011xxx.T\|\ | A |                             |
| gitmap | x | [0-1\]\[2-9\]xxxxxxx | L |                             |
| ]{#dig | t | xx\|\[2-9\]xxxxxxxxx | S |                             |
| itmap} |   | \|\[1-9\]xxT\|*\*x.T | E |                             |
+--------+---+----------------------+---+-----------------------------+
| polyco | t | 1                    | T | Call Waiting 1=enabled      |
| m[call | e |                      | R | 0=disable                   |
| _waiti | x |                      | U |                             |
| ng]{#c | t |                      | E |                             |
| all_wa |   |                      |   |                             |
| iting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| cidr   | a | 209.210.17.193/32    | F |                             |
|        | r |                      | A |                             |
|        | r |                      | L |                             |
|        | a |                      | S |                             |
|        | y |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| http[  | t | admin                | T |                             |
| auth_u | e |                      | R |                             |
| sernam | x |                      | U |                             |
| e]{#au | t |                      | E |                             |
| th_use |   |                      |   |                             |
| rname} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| htt    | t | digest               | T |                             |
| p[auth | e |                      | R |                             |
| _type] | x |                      | U |                             |
| {#auth | t |                      | E |                             |
| _type} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| e      | t | TRUE                 | T |                             |
| nabled | e |                      | R |                             |
|        | x |                      | U |                             |
|        | t |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| cidr   | a | 209.210.16.196/32    | F |                             |
|        | r |                      | A |                             |
|        | r |                      | L |                             |
|        | a |                      | S |                             |
|        | y |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| a      | b | TRUE                 | F |                             |
| uto[in | o |                      | A |                             |
| sert_e | o |                      | L |                             |
| nabled | l |                      | S |                             |
| ]{#ins | e |                      | E |                             |
| ert_en | a |                      |   |                             |
| abled} | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| htt    | b | FALSE                | F |                             |
| p[auth | o |                      | A |                             |
| _disab | o |                      | L |                             |
| le]{#a | l |                      | S |                             |
| uth_di | e |                      | E |                             |
| sable} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| admin[ | t |                      | F |                             |
| name]{ | e |                      | A |                             |
| #name} | x |                      | L |                             |
|        | t |                      | S |                             |
|        |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| ad     | t |                      | F |                             |
| min[pa | e |                      | A |                             |
| ssword | x |                      | L |                             |
| ]{#pas | t |                      | S |                             |
| sword} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| path   | t |                      | F |                             |
|        | e |                      | A |                             |
|        | x |                      | L |                             |
|        | t |                      | S |                             |
|        |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| out    | t |                      | F |                             |
| bound[ | e |                      | A |                             |
| proxy_ | x |                      | L |                             |
| primar | t |                      | S |                             |
| y]{#pr |   |                      | E |                             |
| oxy_pr |   |                      |   |                             |
| imary} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| o      | t |                      | F |                             |
| utboun | e |                      | A |                             |
| d[prox | x |                      | L |                             |
| y_seco | t |                      | S |                             |
| ndary] |   |                      | E |                             |
| {#prox |   |                      |   |                             |
| y_seco |   |                      |   |                             |
| ndary} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| l      | n | 5060                 | T |                             |
| ine[si | u |                      | R |                             |
| p_port | m |                      | U |                             |
| ]{#sip | e |                      | E |                             |
| _port} | r |                      |   |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| line[  | t | tcp                  | T |                             |
| sip_tr | e |                      | R |                             |
| anspor | x |                      | U |                             |
| t]{#si | t |                      | E |                             |
| p_tran |   |                      |   |                             |
| sport} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| d      | b | TRUE                 | T |                             |
| ayligh | o |                      | R |                             |
| t[savi | o |                      | U |                             |
| ngs_en | l |                      | E |                             |
| abled] | e |                      |   |                             |
| {#savi | a |                      |   |                             |
| ngs_en | n |                      |   |                             |
| abled} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| day    | t | 3                    | T |                             |
| light[ | e |                      | R |                             |
| saving | x |                      | U |                             |
| s_star | t |                      | E |                             |
| t_mont |   |                      |   |                             |
| h]{#sa |   |                      |   |                             |
| vings_ |   |                      |   |                             |
| start_ |   |                      |   |                             |
| month} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| d      | t | 7                    | T |                             |
| ayligh | e |                      | R |                             |
| t[savi | x |                      | U |                             |
| ngs_st | t |                      | E |                             |
| art_we |   |                      |   |                             |
| ekday] |   |                      |   |                             |
| {#savi |   |                      |   |                             |
| ngs_st |   |                      |   |                             |
| art_we |   |                      |   |                             |
| ekday} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| d      | t | 2                    | T |                             |
| ayligh | e |                      | R |                             |
| t[savi | x |                      | U |                             |
| ngs_st | t |                      | E |                             |
| art_ti |   |                      |   |                             |
| me]{#s |   |                      |   |                             |
| avings |   |                      |   |                             |
| _start |   |                      |   |                             |
| _time} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| dayli  | t | 7                    | T |                             |
| ght[sa | e |                      | R |                             |
| vings_ | x |                      | U |                             |
| stop_w | t |                      | E |                             |
| eekday |   |                      |   |                             |
| ]{#sav |   |                      |   |                             |
| ings_s |   |                      |   |                             |
| top_we |   |                      |   |                             |
| ekday} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| dayli  | t | 2                    | T |                             |
| ght[sa | e |                      | R |                             |
| vings_ | x |                      | U |                             |
| stop_t | t |                      | E |                             |
| ime]{# |   |                      |   |                             |
| saving |   |                      |   |                             |
| s_stop |   |                      |   |                             |
| _time} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| http[  | b | TRUE                 | T |                             |
| domain | o |                      | R |                             |
| _filte | o |                      | U |                             |
| r]{#do | l |                      | E |                             |
| main_f | e |                      |   |                             |
| ilter} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| cont   | b | TRUE                 | F |                             |
| act[us | o |                      | A |                             |
| ers]{# | o |                      | L |                             |
| users} | l |                      | S |                             |
|        | e |                      | E |                             |
|        | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| contac | b | TRUE                 | F |                             |
| t[grou | o |                      | A |                             |
| ps]{#g | o |                      | L |                             |
| roups} | l |                      | S |                             |
|        | e |                      | E |                             |
|        | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| num    | t | TRUE                 | T |                             |
| ber[as | e |                      | R |                             |
| _prese | x |                      | U |                             |
| nce_id | t |                      | E |                             |
| ]{#as_ |   |                      |   |                             |
| presen |   |                      |   |                             |
| ce_id} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ntp[se | t | pool.ntp.org         | T |                             |
| rver_p | e |                      | R |                             |
| rimary | x |                      | U |                             |
| ]{#ser | t |                      | E |                             |
| ver_pr |   |                      |   |                             |
| imary} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ntp[   | t | 2.us.pool.ntp.org    | T |                             |
| server | e |                      | R |                             |
| _secon | x |                      | U |                             |
| dary]{ | t |                      | E |                             |
| #serve |   |                      |   |                             |
| r_seco |   |                      |   |                             |
| ndary} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| sp     | t | GMT-07:00            | T |                             |
| a[time | e |                      | R |                             |
| _zone] | x |                      | U |                             |
| {#time | t |                      | E |                             |
| _zone} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[ti | t | 12hr                 | T | 12hr,24hr                   |
| me_for | e |                      | R |                             |
| mat]{# | x |                      | U |                             |
| time_f | t |                      | E |                             |
| ormat} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[da | t | day/month            | T |                             |
| te_for | e |                      | R |                             |
| mat]{# | x |                      | U |                             |
| date_f | t |                      | E |                             |
| ormat} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | 30 s                 | T |                             |
| back_l | e |                      | R |                             |
| ight_t | x |                      | U |                             |
| imer]{ | t |                      | E |                             |
| #back_ |   |                      |   |                             |
| light_ |   |                      |   |                             |
| timer} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | Yes                  | T |                             |
| handle | e |                      | R |                             |
| _via_r | x |                      | U |                             |
| port]{ | t |                      | E |                             |
| #handl |   |                      |   |                             |
| e_via_ |   |                      |   |                             |
| rport} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | Yes                  | T |                             |
| insert | e |                      | R |                             |
| _via_r | x |                      | U |                             |
| port]{ | t |                      | E |                             |
| #inser |   |                      |   |                             |
| t_via_ |   |                      |   |                             |
| rport} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| sp     | t | Yes                  | T | Call Waiting Yes=enabled    |
| a[call | e |                      | R | No=disable                  |
| _waiti | x |                      | U |                             |
| ng]{#c | t |                      | E |                             |
| all_wa |   |                      |   |                             |
| iting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | No                   | T | Feature Key Sync            |
| featur | e |                      | R | Yes=enabled No=disable      |
| e_key_ | x |                      | U |                             |
| sync]{ | t |                      | E |                             |
| #featu |   |                      |   |                             |
| re_key |   |                      |   |                             |
| _sync} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[du | t | No                   | T | Dual Registration           |
| al_reg | e |                      | R | Yes=enabled No=disable      |
| istrat | x |                      | U |                             |
| ion]{# | t |                      | E |                             |
| dual_r |   |                      |   |                             |
| egistr |   |                      |   |                             |
| ation} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | No                   | T | Auto register when failover |
| regist | e |                      | R | Yes=enabled No=disable      |
| er_whe | x |                      | U |                             |
| n_fail | t |                      | E |                             |
| over]{ |   |                      |   |                             |
| #regis |   |                      |   |                             |
| ter_wh |   |                      |   |                             |
| en_fai |   |                      |   |                             |
| lover} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| sno    | t | on                   | T | Call Waiting on=enabled     |
| m[call | e |                      | R | off=disable visual only and |
| _waiti | x |                      | U | ringer                      |
| ng]{#c | t |                      | E |                             |
| all_wa |   |                      |   |                             |
| iting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| nway[  | t | TRUE                 | F | N-Way conferencing for      |
| confer | e |                      | A | devices supporting network  |
| ence]{ | x |                      | L | conference uri              |
| #confe | t |                      | S |                             |
| rence} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| vtec   | t | 0                    | F | Enable vlan=1               |
| h[vlan | e |                      | A |                             |
| _wan_e | x |                      | L |                             |
| nable] | t |                      | S |                             |
| {#vlan |   |                      | E |                             |
| _wan_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| vt     | t | 1                    | F | VLAN ID                     |
| ech[vl | e |                      | A |                             |
| an_wan | x |                      | L |                             |
| _id]{# | t |                      | S |                             |
| vlan_w |   |                      | E |                             |
| an_id} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| vt     | t | 0                    | F | VLAN Priority               |
| ech[vl | e |                      | A |                             |
| an_wan | x |                      | L |                             |
| _prior | t |                      | S |                             |
| ity]{# |   |                      | E |                             |
| vlan_w |   |                      |   |                             |
| an_pri |   |                      |   |                             |
| ority} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| stu    | t |                      | F | STUN server address         |
| n[serv | e |                      | A |                             |
| er]{#s | x |                      | L |                             |
| erver} | t |                      | S |                             |
|        |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| stun[  | n | 3478                 | F | STUN server port            |
| port]{ | u |                      | A |                             |
| #port} | m |                      | L |                             |
|        | e |                      | S |                             |
|        | r |                      | E |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| a      | n | 0                    | T | Aastra timezone offset in   |
| astra[ | u |                      | R | minutes (e.g. 300 = GMT-5 = |
| gmt_of | m |                      | U | Eastern Standard Time)      |
| fset]{ | e |                      | E |                             |
| #gmt_o | r |                      |   |                             |
| ffset} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| aas    | n | 0                    | T | Aastra clock format         |
| tra[ti | u |                      | R |                             |
| me_for | m |                      | U |                             |
| mat]{# | e |                      | E |                             |
| time_f | r |                      |   |                             |
| ormat} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| aas    | n | 0                    | T | Aastra date format          |
| tra[da | u |                      | R |                             |
| te_for | m |                      | U |                             |
| mat]{# | e |                      | E |                             |
| date_f | r |                      |   |                             |
| ormat} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | `-5`                 | F | Time zone ranges from -11   |
| k[time | e |                      | A | to +12                      |
| _zone] | x | :                    | L |                             |
| {#time | t |                      | S |                             |
| _zone} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | United               | F | Time zone name example      |
| ink[ti | e | States-Eastern Time  | A | United States-Mountain Time |
| me_zon | x |                      | L |                             |
| e_name | t |                      | S |                             |
| ]{#tim |   |                      | E |                             |
| e_zone |   |                      |   |                             |
| _name} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | 1                    | F | 0-12 Hour, 1-24 Hour        |
| ink[ti | e |                      | A |                             |
| me_for | x |                      | L |                             |
| mat]{# | t |                      | S |                             |
| time_f |   |                      | E |                             |
| ormat} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | b | 1                    | T | Send the response back to   |
| ink[rp | o |                      | R | the source it came from.    |
| ort]{# | o |                      | U |                             |
| rport} | l |                      | E |                             |
|        | e |                      |   |                             |
|        | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | b | 0                    | T | SIP Session Timers          |
| alink[ | o |                      | R |                             |
| sessio | o |                      | U |                             |
| n_time | l |                      | E |                             |
| r]{#se | e |                      |   |                             |
| ssion_ | a |                      |   |                             |
| timer} | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | b | 0                    | T | Retransmission              |
| ink[re | o |                      | R |                             |
| transm | o |                      | U |                             |
| ission | l |                      | E |                             |
| ]{#ret | e |                      |   |                             |
| ransmi | a |                      |   |                             |
| ssion} | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | b | 1                    | T | subscribe to the voicemail  |
| alink[ | o |                      | R | MWI 0-Disabled (default),   |
| subscr | o |                      | U | 1-Enabled                   |
| ibe_mw | l |                      | E |                             |
| i_to_v | e |                      |   |                             |
| m]{#su | a |                      |   |                             |
| bscrib | n |                      |   |                             |
| e_mwi_ |   |                      |   |                             |
| to_vm} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | 0                    | T |                             |
| k[srtp | e |                      | R |                             |
| _encry | x |                      | U |                             |
| ption] | t |                      | E |                             |
| {#srtp |   |                      |   |                             |
| _encry |   |                      |   |                             |
| ption} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 0                    | F | Default 0                   |
| k[rfc2 | u |                      | A |                             |
| 543_ho | m |                      | L |                             |
| ld]{#r | e |                      | S |                             |
| fc2543 | r |                      | E |                             |
| _hold} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 0                    | F | The value is 0(default) or  |
| k[blf_ | u |                      | A | 1.                          |
| led_mo | m |                      | L |                             |
| de]{#b | e |                      | S |                             |
| lf_led | r |                      | E |                             |
| _mode} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | n | 1                    | T | (0-Disabled;1-Enabled)      |
| alink[ | u |                      | R |                             |
| trust_ | m |                      | U |                             |
| ctrl]{ | e |                      | E |                             |
| #trust | r |                      |   |                             |
| _ctrl} | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 0                    | F | (0-Disabled;1-Enabled)      |
| k[dire | u |                      | A |                             |
| ct_ip_ | m |                      | L |                             |
| call_e | e |                      | S |                             |
| nable] | r |                      | E |                             |
| {#dire | i |                      |   |                             |
| ct_ip_ | c |                      |   |                             |
| call_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | n | 0                    | F | (0-Disabled;1-Enabled)      |
| ink[hi | u |                      | A |                             |
| de_fea | m |                      | L |                             |
| ture_a | e |                      | S |                             |
| ccess_ | r |                      | E |                             |
| codes_ | i |                      |   |                             |
| enable | c |                      |   |                             |
| ]{#hid |   |                      |   |                             |
| e_feat |   |                      |   |                             |
| ure_ac |   |                      |   |                             |
| cess_c |   |                      |   |                             |
| odes_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | n | 0                    | F | Display Voice Mail Popup    |
| ink[vo | u |                      | A |                             |
| ice_ma | m |                      | L |                             |
| il_pop | e |                      | S |                             |
| up_ena | r |                      | E |                             |
| ble]{# | i |                      |   |                             |
| voice_ | c |                      |   |                             |
| mail_p |   |                      |   |                             |
| opup_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 0                    | F | Display Missed Call Popup   |
| k[miss | u |                      | A |                             |
| ed_cal | m |                      | L |                             |
| l_popu | e |                      | S |                             |
| p_enab | r |                      | E |                             |
| le]{#m | i |                      |   |                             |
| issed_ | c |                      |   |                             |
| call_p |   |                      |   |                             |
| opup_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | n | 0                    | T | The type of SIP header(s)   |
| alink[ | u |                      | R | to carry the caller ID;     |
| cid_so | m |                      | U | 0-FROM (default), 1-PAI     |
| urce]{ | e |                      | E | 2-PAI-FROM,                 |
| #cid_s | r |                      |   | 3-PRID-PAI-FROM,            |
| ource} | i |                      |   | 4-PAI-RPID-FROM,            |
|        | c |                      |   | 5-RPID-FROM                 |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 1                    | T | 0-Disabled 1-Enabled        |
| k[dtmf | u |                      | R |                             |
| _hide] | m |                      | U |                             |
| {#dtmf | e |                      | E |                             |
| _hide} | r |                      |   |                             |
|        | i |                      |   |                             |
|        | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 5060                 | F | 5060 default                |
| k[sip_ | u |                      | A |                             |
| listen | m |                      | L |                             |
| _port] | e |                      | S |                             |
| {#sip_ | r |                      | E |                             |
| listen | i |                      |   |                             |
| _port} | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | <h                   | T | Base URL for Yealink        |
| k[firm | e | ttps://server.yourdo | R | Firmware. Download from     |
| ware_u | x | main.com/app/yealink | U | <                           |
| rl]{#f | t | /resources/firmware> | E | http://support.yealink.com> |
| irmwar |   |                      |   |                             |
| e_url} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | cp860-37.81.0.10.rom | T | Filename of the CP860       |
| ink[fi | e |                      | R | firmware ROM                |
| rmware | x |                      | U |                             |
| _cp860 | t |                      | E |                             |
| ]{#fir |   |                      |   |                             |
| mware_ |   |                      |   |                             |
| cp860} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | cp960-73.80.0.25.rom | T | Filename of the CP960       |
| ink[fi | e |                      | R | firmware ROM                |
| rmware | x |                      | U |                             |
| _cp960 | t |                      | E |                             |
| ]{#fir |   |                      |   |                             |
| mware_ |   |                      |   |                             |
| cp960} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t29g-46.81.0.110.rom | T | Filename of the T29G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t29 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t29g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t38g-38.70.0.185.rom | T | Filename of the T38G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t38 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t38g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t40g-76.81.0.110.rom | T | Filename of the T40G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t40 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t40g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t40p-54.81.0.110.rom | T | Filename of the T40P        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t40 | t |                      | E |                             |
| p]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t40p} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t41s-66.81.0.110.rom | T | Filename of the T41S        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t41 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t41s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t42g-29.81.0.110.rom | T | Filename of the T42G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t42 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t42g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t42s-66.81.0.110.rom | T | Filename of the T42S        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t42 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t42s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t46g-28.81.0.110.rom | T | Filename of the T46G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t46 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t46g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t46s-66.81.0.110.rom | T | Filename of the T46S        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t46 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t46s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t48g-35.81.0.110.rom | T | Filename of the T48G        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t48 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t48g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t48s-66.81.0.110.rom | T | Filename of the T48S        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t48 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t48s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t49g-51.80.0.100.rom | T | Filename of the             |
| alink[ | e |                      | R | T49Gfirmware ROM            |
| firmwa | x |                      | U |                             |
| re_t49 | t |                      | E |                             |
| g]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t49g} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | T54S(                | T | Firmware tested 2017-11-26  |
| alink[ | e | T52S)-70.82.0.20.rom | R |                             |
| firmwa | x |                      | U |                             |
| re_t54 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t54s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t56a-58.80.0.25.rom  | T | Filename of the T56A        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t56 | t |                      | E |                             |
| a]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t56a} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t58a-58.80.0.25.rom  | T | Filename of the T58A        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t58 | t |                      | E |                             |
| a]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t58a} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t58v-58.80.0.25.rom  | T | Filename of the T58V        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t58 | t |                      | E |                             |
| v]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t58v} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | vp530-23.70.0.40.rom | T | Filename of the VP530       |
| ink[fi | e |                      | R | firmware ROM                |
| rmware | x |                      | U |                             |
| _vp530 | t |                      | E |                             |
| ]{#fir |   |                      |   |                             |
| mware_ |   |                      |   |                             |
| vp530} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | b | 1                    | F | (0-Disabled;1-Enabled)      |
| k[netw | o |                      | A |                             |
| ork_vp | o |                      | L |                             |
| n_enab | l |                      | S |                             |
| le]{#n | e |                      | E |                             |
| etwork | a |                      |   |                             |
| _vpn_e | n |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | n | 0                    | F | IP Address mode 0-ipv4,     |
| k[ip_a | u |                      | A | 1-ipv6, 2-ipv4&ipv6         |
| ddress | m |                      | L |                             |
| _mode] | e |                      | S |                             |
| {#ip_a | r |                      | E |                             |
| ddress | i |                      |   |                             |
| _mode} | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | b | 0                    | F | LLDP 0-Disabled, 1-Enabled  |
| ink[ll | o |                      | A |                             |
| dp_ena | o |                      | L |                             |
| ble]{# | l |                      | S |                             |
| lldp_e | e |                      | E |                             |
| nable} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | b | 0                    | F | CDP 0-Disabled, 1-Enabled   |
| alink[ | o |                      | A |                             |
| cdp_en | o |                      | L |                             |
| able]{ | l |                      | S |                             |
| #cdp_e | e |                      | E |                             |
| nable} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | b | 0                    | T | Overwrite Mode 0-Disabled,  |
| ink[ov | o |                      | R | 1-Enabled                   |
| erwrit | o |                      | U |                             |
| e_mode | l |                      | E |                             |
| ]{#ove | e |                      |   |                             |
| rwrite | a |                      |   |                             |
| _mode} | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | n | 0                    | T | DSS Key Label Length        |
| alink[ | u |                      | R | Default-0 Extended-1 Mid    |
| dsskey | m |                      | U | Range-2                     |
| _lengt | e |                      | E |                             |
| h]{#ds | r |                      |   |                             |
| skey_l | i |                      |   |                             |
| ength} | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | n | 0                    | T | Enable or disable the       |
| alink[ | u |                      | R | feature key                 |
| featur | m |                      | U | synchronization; 0-Disabled |
| e_key_ | e |                      | E | (default) 1-Enabled         |
| sync]{ | r |                      |   |                             |
| #featu | i |                      |   |                             |
| re_key | c |                      |   |                             |
| _sync} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | b | 0                    | T | Auto dial after digit       |
| alink[ | o |                      | R | timeout 0-Disabled          |
| predia | o |                      | U | (default), 1-Enabled;       |
| l_auto | l |                      | E |                             |
| dial]{ | e |                      |   |                             |
| #predi | a |                      |   |                             |
| al_aut | n |                      |   |                             |
| odial} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | custom.wav           | F | custom ring tone            |
| k[ring | e |                      | A | (Busy.wav);                 |
| _type] | x |                      | L |                             |
| {#ring | t |                      | S |                             |
| _type} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | <http://l            | F | <h                          |
| k[ring | e | ocalhost/all,delete> | A | ttp://localhost/all,delete> |
| tone_d | x |                      | L | all the customized ring     |
| elete] | t |                      | S | tones                       |
| {#ring |   |                      | E |                             |
| tone_d |   |                      |   |                             |
| elete} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| dayli  | t | 11                   | T |                             |
| ght[sa | e |                      | R |                             |
| vings_ | x |                      | U |                             |
| start_ | t |                      | E |                             |
| day]{# |   |                      |   |                             |
| saving |   |                      |   |                             |
| s_star |   |                      |   |                             |
| t_day} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| d      | t | 11                   | T |                             |
| ayligh | e |                      | R |                             |
| t[savi | x |                      | U |                             |
| ngs_st | t |                      | E |                             |
| op_mon |   |                      |   |                             |
| th]{#s |   |                      |   |                             |
| avings |   |                      |   |                             |
| _stop_ |   |                      |   |                             |
| month} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| day    | t | 4                    | T |                             |
| light[ | e |                      | R |                             |
| saving | x |                      | U |                             |
| s_stop | t |                      | E |                             |
| _day]{ |   |                      |   |                             |
| #savin |   |                      |   |                             |
| gs_sto |   |                      |   |                             |
| p_day} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| http[  | a | 555                  | T |                             |
| auth_p | r |                      | R |                             |
| asswor | r |                      | U |                             |
| d]{#au | a |                      | E |                             |
| th_pas | y |                      |   |                             |
| sword} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| fan    | t | example.domain.tld   | F | enter a server name or ip   |
| vil[st | e |                      | A |                             |
| un_ser | x |                      | L |                             |
| ver]{# | t |                      | S |                             |
| stun_s |   |                      | E |                             |
| erver} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gr     | t | 1                    | F | DNS Mode 0=A; 1=SRV;        |
| andstr | e |                      | A | 2=NAPTR/SRV;                |
| eam[dn | x |                      | L |                             |
| s_mode | t |                      | S |                             |
| ]{#dns |   |                      | E |                             |
| _mode} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | con                  | F | List of contact groups that |
| dstrea | e | tacts[elementary]{#e | A | every phone will have       |
| m[glob | x | lementary},contacts[ | L | access to. Namely building  |
| al_con | t | facilities]{#facilit | S | sites.                      |
| tact_g |   | ies},contacts[other] | E |                             |
| roups] |   | {#other},contacts[se |   |                             |
| {#glob |   | condary]{#secondary} |   |                             |
| al_con |   |                      |   |                             |
| tact_g |   |                      |   |                             |
| roups} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | 0                    | T | NAT Traversal. 0 - No, 1 -  |
| tream[ | e |                      | R | STUN, 2 - keep alive, 3 -   |
| nat_tr | x |                      | U | UPnP, 4 - Auto, 5 - VPN     |
| aversa | t |                      | E |                             |
| l]{#na |   |                      |   |                             |
| t_trav |   |                      |   |                             |
| ersal} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| grands | t | mydomain.c           | T | Grandstream Phonebook       |
| tream[ | e | om/app/provision/pb/ | R | Server Path - NOTE template |
| phoneb | x |                      | U | adds MAC on the end of this |
| ook_xm | t |                      | E | if                          |
| l_serv |   |                      |   | contact                     |
| er_pat |   |                      |   | [grandstream]{#grandstream} |
| h]{#ph |   |                      |   | is enabled. This also       |
| oneboo |   |                      |   | requires nginx rewrite      |
| k_xml_ |   |                      |   | rules for phonebook.xml     |
| server |   |                      |   |                             |
| _path} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| po     | t |                      | F | 3600 \* GMT offset          |
| lycom[ | e |                      | A |                             |
| gmt_of | x |                      | L |                             |
| fset]{ | t |                      | S |                             |
| #gmt_o |   |                      | E |                             |
| ffset} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| po     | n | 0                    | T | Feature Key Sync 1=enabled  |
| lycom[ | u |                      | R | 0=disable                   |
| featur | m |                      | U |                             |
| e_key_ | e |                      | E |                             |
| sync]{ | r |                      |   |                             |
| #featu | i |                      |   |                             |
| re_key | c |                      |   |                             |
| _sync} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| vo     | t | \*97                 | T |                             |
| icemai | e |                      | R |                             |
| l[numb | x |                      | U |                             |
| er]{#n | t |                      | E |                             |
| umber} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| line[  | n | 120                  | T |                             |
| regist | u |                      | R |                             |
| er_exp | m |                      | U |                             |
| ires]{ | e |                      | E |                             |
| #regis | r |                      |   |                             |
| ter_ex | i |                      |   |                             |
| pires} | c |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| co     | b | TRUE                 | F | allow extensions to be      |
| ntact[ | o |                      | A | provisioned as contacts as  |
| extens | o |                      | L | in provision templates      |
| ions]{ | l |                      | S |                             |
| #exten | e |                      | E |                             |
| sions} | a |                      |   |                             |
|        | n |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| sp     | t | (*xxxxxxx\|*xx       | T |                             |
| a[dial | e | xxxx[\|\*xxxxx\|\*xx | R |                             |
| _plan] | x | xx\|](##SUBST##|*xxx | U |                             |
| {#dial | t | xx|*xxxx|)*xxx\|*xx\ | E |                             |
| _plan} |   | *[\|\*x\|\*\*xxxxx\| |   |                             |
|        |   | \*\*xxxx\|\*\*xxx\|\ |   |                             |
|        |   | *\*xx\|](##SUBST##|* |   |                             |
|        |   | x|**xxxxx|**xxxx|**x |   |                             |
|        |   | xx|**xx|)\[3469\]11[ |   |                             |
|        |   | \|0\|](##SUBST##|0|) |   |                             |
|        |   | 00[\|\[2-9\]xxxxxx\| |   |                             |
|        |   | ](##SUBST##|[2-9]xxx |   |                             |
|        |   | xxx|)1xxx\[2-9\]xxxx |   |                             |
|        |   | xxS0\|xxxxxxxxxxxx.) |   |                             |
+--------+---+----------------------+---+-----------------------------+
| spa[   | t | No                   | T | spa secure call No or Yes   |
| secure | e |                      | R |                             |
| _call_ | x |                      | U |                             |
| settin | t |                      | E |                             |
| g]{#se |   |                      |   |                             |
| cure_c |   |                      |   |                             |
| all_se |   |                      |   |                             |
| tting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| sno    | t | USA-7                | F | <http://wiki.               |
| m[time | e |                      | A | snom.com/Settings/timezone> |
| _zone] | x |                      | L |                             |
| {#time | t |                      | S |                             |
| _zone} |   |                      | E |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | 3                    | F | 0-WWW MMM DD (default),     |
| ink[da | e |                      | A | 1-DD-MMM-YY, 2-YYYY-MM-DD,  |
| te_for | x |                      | L | 3-DD/MM/YYYY, 4-MM/DD/YY,   |
| mat]{# | t |                      | S | 5-DD MMM YYYY, 6-WWW DD MMM |
| date_f |   |                      | E |                             |
| ormat} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | n | 3600                 | F | Integer from 0 to 65535     |
| ink[ou | u |                      | A |                             |
| tbound | m |                      | L |                             |
| _proxy | e |                      | S |                             |
| _fallb | r |                      | E |                             |
| ack_in | i |                      |   |                             |
| terval | c |                      |   |                             |
| ]{#out |   |                      |   |                             |
| bound_ |   |                      |   |                             |
| proxy_ |   |                      |   |                             |
| fallba |   |                      |   |                             |
| ck_int |   |                      |   |                             |
| erval} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | n | 0                    | F | (0-Disabled:power indicator |
| alink[ | u |                      | A | LED is off;1-Enabled:power  |
| missed | m |                      | L | indicator LED is solid red) |
| _call_ | e |                      | S |                             |
| power_ | r |                      | E |                             |
| led_fl | i |                      |   |                             |
| ash_en | c |                      |   |                             |
| able]{ |   |                      |   |                             |
| #misse |   |                      |   |                             |
| d_call |   |                      |   |                             |
| _power |   |                      |   |                             |
| _led_f |   |                      |   |                             |
| lash_e |   |                      |   |                             |
| nable} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t41p-36.81.0.110.rom | T | Filename of the T41P        |
| alink[ | e |                      | R | firmware ROM                |
| firmwa | x |                      | U |                             |
| re_t41 | t |                      | E |                             |
| p]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t41p} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| ye     | t | t52s-70.81.0.10.rom  | T | Filename of the             |
| alink[ | e |                      | R | T52Sfirmware ROM            |
| firmwa | x |                      | U |                             |
| re_t52 | t |                      | E |                             |
| s]{#fi |   |                      |   |                             |
| rmware |   |                      |   |                             |
| _t52s} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yeal   | t | <hxxps://replace-t   | F | (URL within 511 characters) |
| ink[op | e | his.url/openvpn.tar> | A |                             |
| envpn_ | x |                      | L |                             |
| url]{# | t |                      | S |                             |
| openvp |   |                      | E |                             |
| n_url} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | custom.wav           | F | Before using this           |
| k[ring | e |                      | A | parameter, you should store |
| tone_u | x |                      | L | the desired ring tone       |
| rl]{#r | t |                      | S | (custom.wav) to the         |
| ington |   |                      | E | provisioning server         |
| e_url} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| yealin | t | 0                    | T | Call Waiting 1=enabled      |
| k[call | e |                      | R | 0=disable                   |
| _waiti | x |                      | U |                             |
| ng]{#c | t |                      | E |                             |
| all_wa |   |                      |   |                             |
| iting} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
| gran   | t | {x+[\|\*x+\|\*++\|]( | T | Define the digits that are  |
| dstrea | e | ##SUBST##|*x+|*++|)p | R | allowed to be called.       |
| m[dial | x | ark+\*x+\|flow+\*x+} | U |                             |
| _plan] | t |                      | E |                             |
| {#dial |   |                      |   |                             |
| _plan} |   |                      |   |                             |
+--------+---+----------------------+---+-----------------------------+
