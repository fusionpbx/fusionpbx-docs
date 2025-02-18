# Dialplan Application

Dialplan Application uses FreeSWITCH **show application** to build the
dropdown lists found in FusionPBX dialplans. This is a list
from a default install and the list can change depending on how many
FreeSWITCH modules are installed.

+-------+-------------+----------------------------------------+----+---+
| name  | description | syntax                                 | ik |   |
|       |             |                                        | ey |   |
+=======+=============+========================================+====+===+
| a     | Answer the  |                                        | m  |   |
| nswer | call        |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| att   | Attended    | \<channel_url\>                        | m  |   |
| _xfer | Transfer    |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| bgs   | Execute a   | \<command\>                            | m  |   |
| ystem | system      |                                        | od |   |
|       | command in  |                                        | _d |   |
|       | the         |                                        | pt |   |
|       | background  |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| bi    | bind a key  | \<realm\>,\<digits\|\~reg              | m  |   |
| nd_di | sequence or | ex\>,\<string\>\[,\<value\>\]\[,\<dtmf | od |   |
| git_a | regex to an | target leg\>\]\[,\<event target        | _d |   |
| ction | action      | leg\>\]                                | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| bin   | Bind a key  | \<key\> \[aab\] \[aoi\|1\] \<app\>     | m  |   |
| d_met | to an       |                                        | od |   |
| a_app | application |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| block | Block DTMF  |                                        | m  |   |
| _dtmf |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| break | Break       |                                        | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| b     | Bridge      | \<channel_url\>                        | m  |   |
| ridge | Audio       |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| bri   | Export a    | \<varname\>=\<value\>                  | m  |   |
| dge_e | channel     |                                        | od |   |
| xport | variable    |                                        | _d |   |
|       | across a    |                                        | pt |   |
|       | bridge      |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| callc | CallCenter  | queue_name                             | mo |   |
| enter |             |                                        | d_ |   |
|       |             |                                        | ca |   |
|       |             |                                        | ll |   |
|       |             |                                        | ce |   |
|       |             |                                        | nt |   |
|       |             |                                        | er |   |
+-------+-------------+----------------------------------------+----+---+
| ca    | capture     | \<varname\>\<regex\>                   | m  |   |
| pture | data into a |                                        | od |   |
|       | var         |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| chec  | Check an ip | \<ip\> \<acl \| cidr\>                 | m  |   |
| k_acl | against an  | \[\<hangup_cause\>\]                   | od |   |
|       | ACL list    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| cle   | clear all   | \<realm\>\|all\[,target\]              | m  |   |
| ar_di | digit       |                                        | od |   |
| git_a | bindings    |                                        | _d |   |
| ction |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| cle   | Clear       |                                        | m  |   |
| ar_sp | Speech      |                                        | od |   |
| eech_ | Handle      |                                        | _d |   |
| cache | Cache       |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| cn    | Do PLC on   |                                        | m  |   |
| g_plc | CNG frames  |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| confe | conference  |                                        | mo |   |
| rence |             |                                        | d_ |   |
|       |             |                                        | co |   |
|       |             |                                        | nf |   |
|       |             |                                        | er |   |
|       |             |                                        | en |   |
|       |             |                                        | ce |   |
+-------+-------------+----------------------------------------+----+---+
| co    | confe       |                                        | mo |   |
| nfere | rence_set_a |                                        | d_ |   |
| nce_s | uto_outcall |                                        | co |   |
| et_au |             |                                        | nf |   |
| to_ou |             |                                        | er |   |
| tcall |             |                                        | en |   |
|       |             |                                        | ce |   |
+-------+-------------+----------------------------------------+----+---+
| db    | Insert to   | \[inse                                 | mo |   |
|       | the db      | rt\|delete\]/\<realm\>/\<key\>/\<val\> | d_ |   |
|       |             |                                        | db |   |
+-------+-------------+----------------------------------------+----+---+
| de    | decode      | \[max_pictures\]                       | m  |   |
| code_ | picture     |                                        | od |   |
| video |             |                                        | _f |   |
|       |             |                                        | sv |   |
+-------+-------------+----------------------------------------+----+---+
| d     | Prevent     | \[only_rtp\]                           | m  |   |
| edupl | duplicate   |                                        | od |   |
| icate | inband +    |                                        | _d |   |
| _dtmf | 2833 dtmf   |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| de    | Send call   | \<deflect_data\>                       | m  |   |
| flect | deflect     |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| delay | echo audio  | \<delay ms\>                           | m  |   |
| _echo | at a        |                                        | od |   |
|       | specified   |                                        | _d |   |
|       | delay       |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| de    | d           | > \<threshold\> \<audio_hits\>         | m  |   |
| tect_ | etect_audio | > \<timeout_ms\> \[\<file\>\]          | od |   |
| audio |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| dete  | det         | > \<threshold\> \<silence_hits\>       | m  |   |
| ct_si | ect_silence | > \<timeout_ms\> \[\<file\>\]          | od |   |
| lence |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| det   | Detect      | \<mod_name\> \<gram_name\>             | m  |   |
| ect_s | speech      | \<gram_path\> \[\<addr\>\] OR grammar  | od |   |
| peech |             | \<gram_name\> \[\<path\>\] OR          | _d |   |
|       |             | nogrammar \<gram_name\> OR             | pt |   |
|       |             | grammaron/grammaroff \<gram_name\> OR  | oo |   |
|       |             | grammarsalloff                         | ls |   |
+-------+-------------+----------------------------------------+----+---+
|       |             | OR pause OR resume OR                  |    |   |
|       |             | start_input_timers OR stop OR param    |    |   |
|       |             | \<name\> \<value\>                     |    |   |
+-------+-------------+----------------------------------------+----+---+
| di    | change      | \<realm\>\[,\<target\>\]               | m  |   |
| git_a | binding     |                                        | od |   |
| ction | realm       |                                        | _d |   |
| _set_ |             |                                        | pt |   |
| realm |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| d     | Displace    | > \<path\> \[\<flags\>\]               | m  |   |
| ispla | File        | > \[+time_limit_ms\]                   | od |   |
| ce_se |             |                                        | _d |   |
| ssion |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| ea    | Enable      |                                        | m  |   |
| rly_h | early       |                                        | od |   |
| angup | hangup      |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| eave  | eavesdrop   | \[all \| \<uuid\>\]                    | m  |   |
| sdrop | on a uuid   |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| echo  | Echo        |                                        | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| e     | Enable      | \[0\|\<seconds\>\]                     | m  |   |
| nable | Media       |                                        | od |   |
| _hear | Heartbeat   |                                        | _d |   |
| tbeat |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| e     | Enable      | \[0\|\<seconds\>\]                     | m  |   |
| nable | Keepalive   |                                        | od |   |
| _keep |             |                                        | _d |   |
| alive |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| e     | Playback    | \<path\>                               | m  |   |
| ndles | File        |                                        | od |   |
| s_pla | Endlessly   |                                        | _d |   |
| yback |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| enum  | Perform an  | \[reload \| \<number\> \[\<root\>\]\]  | mo |   |
|       | ENUM lookup |                                        | d_ |   |
|       |             |                                        | en |   |
|       |             |                                        | um |   |
+-------+-------------+----------------------------------------+----+---+
| eval  | Do Nothing  |                                        | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| event | Fire an     |                                        | m  |   |
|       | event       |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| ex    | Execute an  | \<extension\> \<dialplan\> \<context\> | m  |   |
| ecute | extension   |                                        | od |   |
| _exte |             |                                        | _d |   |
| nsion |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| e     | Export a    | \<varname\>=\<value\>                  | m  |   |
| xport | channel     |                                        | od |   |
|       | variable    |                                        | _d |   |
|       | across a    |                                        | pt |   |
|       | bridge      |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| fax_d | Detect      |                                        | m  |   |
| etect | faxes       |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| fifo  | Park with   | \<fifo                                 | mo |   |
|       | FIFO        | name\>\[!\<importance_number\>\] \[in  | d_ |   |
|       |             | \[\<announce file\>undef\] \| out      | fi |   |
|       |             | \[waitundef\] \[\<music                | fo |   |
|       |             | file\>\|undef\]\]                      |    |   |
+-------+-------------+----------------------------------------+----+---+
| fifo_ | Count a     | > \<fifo_outbound_uuid\>               | mo |   |
| track | call as a   |                                        | d_ |   |
| _call | fifo call   |                                        | fi |   |
|       | in the      |                                        | fo |   |
|       | m           |                                        |    |   |
|       | anual_calls |                                        |    |   |
|       | queue       |                                        |    |   |
+-------+-------------+----------------------------------------+----+---+
| fire  | fire the    |                                        | m  |   |
|       | message     |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| flush | flush any   |                                        | m  |   |
| _dtmf | queued dtmf |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| gen   | Generate    | \<tgml_script\>\[\|\<loops\>\]         | m  |   |
| tones | Tones       |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| group | Manage a    | \[insert\|delete\]:\<group             | mo |   |
|       | group       | name\>:\<val\>                         | d_ |   |
|       |             |                                        | db |   |
+-------+-------------+----------------------------------------+----+---+
| h     | Hangup the  | \[\<cause\>\]                          | m  |   |
| angup | call        |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| hash  | Insert into | \[insertdelete\|dele                   | mo |   |
|       | the         | te_ifmatch\]/\<realm\>/\<key\>/\<val\> | d_ |   |
|       | hashtable   |                                        | ha |   |
|       |             |                                        | sh |   |
+-------+-------------+----------------------------------------+----+---+
| hold  | Send a hold | \[\<display message\>\]                | m  |   |
|       | message     |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| info  | Display     |                                        | m  |   |
|       | Call Info   |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| info  | Display     |                                        | m  |   |
|       | Call Info   |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| inte  | intercept   | \[-bleg\] \<uuid\>                     | m  |   |
| rcept |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| ivr   | Run an ivr  |                                        | m  |   |
|       | menu        |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| ji    | Send        | > \<jitterbuffer_data\>                | m  |   |
| tterb | session     |                                        | od |   |
| uffer | j           |                                        | _d |   |
|       | itterbuffer |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| limit | Limit       | > \<backend\> \<realm\> \<id\>         | m  |   |
|       |             | > \[\<max\>\[/interval\]\] \[number    | od |   |
|       |             | > \[dialplan \[context\]\]\]           | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| lim   | Limit       | > \<backend\> \<realm\> \<id\>         | m  |   |
| it_ex |             | > \<max\>\[/interval\] \<application\> | od |   |
| ecute |             | > \[application arguments\]            | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| limit | Limit       | > \<realm\> \<id\>                     | m  |   |
| _hash |             | > \[\<max\>\[/interval\]\] \[number    | od |   |
|       |             | > \[dialplan \[context\]\]\]           | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| lim   | Limit       | > \<realm\> \<id\>                     | m  |   |
| it_ha |             | > \<max\>\[/interval\] \<application\> | od |   |
| sh_ex |             | > \[application arguments\]            | _d |   |
| ecute |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| log   | Logs to the | \<log_level\> \<log_string\>           | m  |   |
|       | logger      |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| loo   | Playback    | \[+loops\] \<path\>                    | m  |   |
| p_pla | File looply |                                        | od |   |
| yback |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| m     | Reset all   |                                        | m  |   |
| edia_ | b           |                                        | od |   |
| reset | ypass/proxy |                                        | _d |   |
|       | media flags |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| mkdir | Create a    | > \<path\>                             | m  |   |
|       | directory   |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| mul   | Set many    | \[\^\^\<delim\>\]\<varname\>=\<value\> | m  |   |
| tiset | channel     | \<var2\>=\<val2\>                      | od |   |
|       | variables   |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| multi | Unset many  | \[\^\^\<delim\>\]\<varname\> \<var2\>  | m  |   |
| unset | channel     | \<var3\>                               | od |   |
|       | variables   |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| mutex | block on a  | \<keyname\>\[ on\|off\]                | m  |   |
|       | call flow   |                                        | od |   |
|       | only        |                                        | _d |   |
|       | allowing    |                                        | pt |   |
|       | one at a    |                                        | oo |   |
|       | time        |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| no    | Refuse      |                                        | m  |   |
| video | Inbound     |                                        | od |   |
|       | Video       |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| park  | Park        |                                        | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| park_ | Park State  |                                        | m  |   |
| state |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| p     | Say a       | \<macro_name\>,\<data\>                | m  |   |
| hrase | Phrase      |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| p     | Pickup      | \[\<key\>\]                            | m  |   |
| ickup |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| pl    | Play and do | \<file\> detect:\<engine\>             | m  |   |
| ay_an | speech      | {param1=val1,param2=val2}\<grammar\>   | od |   |
| d_det | recognition |                                        | _d |   |
| ect_s |             |                                        | pt |   |
| peech |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| play  | Play and    | > \<min\> \<max\> \<tries\>            | >  |   |
| _and_ | get Digits  | > \<timeout\> \<terminators\> \<file\> |  m |   |
| get_d |             | > \<invalid_file\> \<var_name\>        | od |   |
| igits |             | > \<regexp\> \[\<digit_timeout\>\]     | _d |   |
|       |             | > \[\'\<failure_ext\> \[failure_dp     | pt |   |
|       |             | > \[failure_context\]\]\'\]            | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| pla   | play a fsv  | \<file\>                               | m  |   |
| y_fsv | file        |                                        | od |   |
|       |             |                                        | _f |   |
|       |             |                                        | sv |   |
+-------+-------------+----------------------------------------+----+---+
| pla   | play a yvv  | > \<file\> \[width\] \[height\]        | m  |   |
| y_yuv | file        |                                        | od |   |
|       |             |                                        | _f |   |
|       |             |                                        | sv |   |
+-------+-------------+----------------------------------------+----+---+
| pla   | Playback    | > \<path\>                             | m  |   |
| yback | File        |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| pre_a | Pre-Answer  |                                        | m  |   |
| nswer | the call    |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| prepr | pre-process |                                        | m  |   |
| ocess |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| pre   | Send        | > \<rpid\> \<status\> \[\<id\>\]       | m  |   |
| sence | Presence    |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| pr    | Set privacy | offnamenumber                          | m  |   |
| ivacy | on calls    |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| push  | Set a       | \<varname\>=\<value\>                  | m  |   |
|       | channel     |                                        | od |   |
|       | variable    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| queue | Queue dtmf  | \<dtmf_data\>                          | m  |   |
| _dtmf | to be sent  |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| read  | Read Digits | \<min\> \<max\> \<file\> \<var_name\>  | m  |   |
|       |             | \<timeout\> \<terminators\>            | od |   |
|       |             | \<digit_timeout\>                      | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Record File | > \<path\> \[\<time_limit_secs\>\]     | m  |   |
| ecord |             | > \[\<silence_thresh\>\]               | od |   |
|       |             | > \[\<silence_hits\>\]                 | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| recor | record an   | > \<file\>                             | m  |   |
| d_fsv | fsv file    |                                        | od |   |
|       |             |                                        | _f |   |
|       |             |                                        | sv |   |
+-------+-------------+----------------------------------------+----+---+
| reco  | Record      | > \<path\> \[+\<timeout\>\]            | m  |   |
| rd_se | Session     |                                        | od |   |
| ssion |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| reco  | Mask audio  | \<path\>                               | m  |   |
| rd_se | in          |                                        | od |   |
| ssion | recording   |                                        | _d |   |
| _mask |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Resume      | > \<path\>                             | m  |   |
| ecord | recording   |                                        | od |   |
| _sess |             |                                        | _d |   |
| ion_u |             |                                        | pt |   |
| nmask |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Send call   |                                        | m  |   |
| ecove | recov       |                                        | od |   |
| ry_re | ery_refresh |                                        | _d |   |
| fresh |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| red   | Send        | > \<redirect_data\>                    | m  |   |
| irect | session     |                                        | od |   |
|       | redirect    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Remove      | \[\<function\>\]                       | m  |   |
| emove | media bugs  |                                        | od |   |
| _bugs |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Rename file | \<from_path\> \<to_path\>              | m  |   |
| ename |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| reply | reply to a  |                                        | m  |   |
|       | message     |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| re    | Send        | \<respond_data\>                       | m  |   |
| spond | session     |                                        | od |   |
|       | respond     |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| ring_ | Indicate    |                                        | m  |   |
| ready | Ring_Ready  |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| rxfax | FAX Receive | \<filename\>                           | m  |   |
|       | Application |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| say   | say         | \<module_name\>\[:\<lang\>\]           | m  |   |
|       |             | \<say_type\> \<say_method\>            | od |   |
|       |             | \[\<say_gender\>\] \<text\>            | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sched | Schedule a  | \[+\]\<time\> \<path\> \[alegboth\]    | m  |   |
| _broa | broadcast   |                                        | od |   |
| dcast | in the      |                                        | _d |   |
|       | future      |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sc    | cancel      | \[group\]                              | m  |   |
| hed_c | scheduled   |                                        | od |   |
| ancel | tasks       |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sc    | Schedule a  | \[+\]\<time\> \[\<cause\>\]            | m  |   |
| hed_h | hangup in   |                                        | od |   |
| angup | the future  |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sched | Enable      | \[0\|\<seconds\>\]                     | m  |   |
| _hear | Scheduled   |                                        | od |   |
| tbeat | Heartbeat   |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sche  | Schedule a  | \[+\]\<time\> \<extension\>            | m  |   |
| d_tra | transfer in | \<dialplan\> \<context\>               | od |   |
| nsfer | the future  |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| send  | send the    |                                        | m  |   |
|       | message     |                                        | od |   |
|       | as-is       |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| se    | Send        | > \<text\>                             | m  |   |
| nd_di | session a   |                                        | od |   |
| splay | new display |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| send  | Send dtmf   | > \<dtmf_data\>                        | m  |   |
| _dtmf | to be sent  |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| send  | Send info   | > \<info\>                             | m  |   |
| _info |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| s     | sessi       | > \<level\>                            | m  |   |
| essio | on_loglevel |                                        | od |   |
| n_log |             |                                        | _d |   |
| level |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set   | set a       |                                        | m  |   |
|       | variable    |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| set   | Set a       | \<varname\>=\<value\>                  | m  |   |
|       | channel     |                                        | od |   |
|       | variable    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set_a | set volume  |                                        | m  |   |
| udio_ |             |                                        | od |   |
| level |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set_g | Set a       | \<varname\>=\<value\>                  | m  |   |
| lobal | global      |                                        | od |   |
|       | variable    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set_m | Set Media   |                                        | m  |   |
| edia_ | Stats       |                                        | od |   |
| stats |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set   | set mute    |                                        | m  |   |
| _mute |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set   | Name the    | \<name\>                               | m  |   |
| _name | channel     |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set_p | Set a       | \<varname\>=\<value\>                  | m  |   |
| rofil | caller      |                                        | od |   |
| e_var | profile     |                                        | _d |   |
|       | variable    |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set   | Set a User  | \<user\>@\<domain\> \[prefix\]         | m  |   |
| _user |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| set_z | Enable      |                                        | m  |   |
| ombie | Zombie      |                                        | od |   |
| _exec | Execution   |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sleep | Pause a     | \<pausemilliseconds\>                  | m  |   |
|       | channel     |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Connect to  | \<ip\>\[:\<port\>\]                    | mo |   |
| ocket | a socket    |                                        | d_ |   |
|       |             |                                        | ev |   |
|       |             |                                        | en |   |
|       |             |                                        | t_ |   |
|       |             |                                        | so |   |
|       |             |                                        | ck |   |
|       |             |                                        | et |   |
+-------+-------------+----------------------------------------+----+---+
| sofi  | private     | > \<uuid\>                             | m  |   |
| a_sla | sofia sla   |                                        | od |   |
|       | function    |                                        | _s |   |
|       |             |                                        | of |   |
|       |             |                                        | ia |   |
+-------+-------------+----------------------------------------+----+---+
| soft  | Put a       | > \<unhold key\> \[\<moh_a\>\]         | m  |   |
| _hold | bridged     | > \[\<moh_b\>\]                        | od |   |
|       | channel on  |                                        | _d |   |
|       | hold        |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sound | Analyze     |                                        | m  |   |
| _test | Audio       |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | Detect TDD  |                                        | m  |   |
| ndsp_ | data        |                                        | od |   |
| detec |             |                                        | _s |   |
| t_tdd |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | Send TDD    |                                        | m  |   |
| ndsp_ | data        |                                        | od |   |
| injec |             |                                        | _s |   |
| t_tdd |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Send TDD    |                                        | m  |   |
| pands | data        |                                        | od |   |
| p_sen |             |                                        | _s |   |
| d_tdd |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | Detect dtmf |                                        | m  |   |
| ndsp_ |             |                                        | od |   |
| start |             |                                        | _s |   |
| _dtmf |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| span  | start fax   | \<app\>\[ \<arg\>\]\[ \<timeout\>\]\[  | m  |   |
| dsp_s | detect      | \<tone_type\>\]                        | od |   |
| tart_ |             |                                        | _s |   |
| fax_d |             |                                        | pa |   |
| etect |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spand | Start       | \<name\>                               | m  |   |
| sp_st | background  |                                        | od |   |
| art_t | tone        |                                        | _s |   |
| one_d | detection   |                                        | pa |   |
| etect | with        |                                        | nd |   |
|       | cadence     |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | stop        |                                        | m  |   |
| ndsp_ | sending tdd |                                        | od |   |
| stop_ |             |                                        | _s |   |
| detec |             |                                        | pa |   |
| t_tdd |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | stop inband |                                        | m  |   |
| andsp | dtmf        |                                        | od |   |
| _stop |             |                                        | _s |   |
| _dtmf |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | stop fax    |                                        | m  |   |
| ndsp_ | detect      |                                        | od |   |
| stop_ |             |                                        | _s |   |
| fax_d |             |                                        | pa |   |
| etect |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | stop        |                                        | m  |   |
| ndsp_ | sending tdd |                                        | od |   |
| stop_ |             |                                        | _s |   |
| injec |             |                                        | pa |   |
| t_tdd |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| span  | Stop        |                                        | m  |   |
| dsp_s | background  |                                        | od |   |
| top_t | tone        |                                        | _s |   |
| one_d | detection   |                                        | pa |   |
| etect | with        |                                        | nd |   |
|       | cadence     |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| speak | Speak text  | \<engine\>\<text\>                     | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| start | Detect dtmf |                                        | m  |   |
| _dtmf |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| star  | Generate    |                                        | m  |   |
| t_dtm | dtmf        |                                        | od |   |
| f_gen |             |                                        | _d |   |
| erate |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | stop        |                                        | m  |   |
|       | execution   |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | Do Nothing  |                                        | m  |   |
|       |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Stop        | \<path\>                               | m  |   |
| top_d | Displace    |                                        | od |   |
| ispla | File        |                                        | _d |   |
| ce_se |             |                                        | pt |   |
| ssion |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | stop inband |                                        | m  |   |
| _dtmf | dtmf        |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| sto   | stop inband | \[write\]                              | m  |   |
| p_dtm | dtmf        |                                        | od |   |
| f_gen | generation  |                                        | _d |   |
| erate |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | Stop Record | \<path\>                               | m  |   |
| _reco | Session     |                                        | od |   |
| rd_se |             |                                        | _d |   |
| ssion |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| s     | stop        |                                        | m  |   |
| top_t | detecting   |                                        | od |   |
| one_d | tones       |                                        | _d |   |
| etect |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | Stop video  | > \<path\>                             | m  |   |
| _vide | write       |                                        | od |   |
| o_wri | overlay     |                                        | _d |   |
| te_ov |             |                                        | pt |   |
| erlay |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| st    | Stop FAX    |                                        | m  |   |
| opfax | Application |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| str   | strftime    | \[\<epoch\>\|\]\<format string\>       | m  |   |
| ftime |             |                                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| s     | execute a   |                                        | m  |   |
| ystem | system      |                                        | od |   |
|       | command     |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Execute a   | > \<command\>                          | m  |   |
| ystem | system      |                                        | od |   |
|       | command     |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| t     | Convert to  |                                        | m  |   |
| 38_ga | T38 Gateway |                                        | od |   |
| teway | if tones    |                                        | _s |   |
|       | are heard   |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| thre  | three way   | \<uuid\>                               | m  |   |
| e_way | call with a |                                        | od |   |
|       | uuid        |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| t     | Detect      |                                        | m  |   |
| one_d | tones       |                                        | od |   |
| etect |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| tra   | Transfer a  | > \<exten\> \[\<dialplan\>             | m  |   |
| nsfer | channel     | > \<context\>\]                        | od |   |
|       |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| tra   | Transfer    | \<\~variable_prefix\|variable\>        | m  |   |
| nsfer | variables   |                                        | od |   |
| _vars |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| txfax | FAX         | \<filename\>                           | m  |   |
|       | Transmit    |                                        | od |   |
|       | Application |                                        | _s |   |
|       |             |                                        | pa |   |
|       |             |                                        | nd |   |
|       |             |                                        | sp |   |
+-------+-------------+----------------------------------------+----+---+
| unbin | Unbind a    | \[\<key\>\]                            | m  |   |
| d_met | key from an |                                        | od |   |
| a_app | application |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| un    | Stop        |                                        | m  |   |
| block | blocking    |                                        | od |   |
| _dtmf | DTMF        |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| u     | Send a      |                                        | m  |   |
| nhold | un-hold     |                                        | od |   |
|       | message     |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| u     | Tell        |                                        | mo |   |
| nloop | loopback to |                                        | d_ |   |
|       | unfold      |                                        | lo |   |
|       |             |                                        | op |   |
|       |             |                                        | ba |   |
|       |             |                                        | ck |   |
+-------+-------------+----------------------------------------+----+---+
| unset | unset a     |                                        | m  |   |
|       | variable    |                                        | od |   |
|       |             |                                        | _s |   |
|       |             |                                        | ms |   |
+-------+-------------+----------------------------------------+----+---+
| unset | Unset a     | > \<varname\>                          | m  |   |
|       | channel     |                                        | od |   |
|       | variable    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| un    | Set a       | \<varname\>=\<value\>                  | m  |   |
| shift | channel     |                                        | od |   |
|       | variable    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| valet | valet_park  | > \<lotname\> \<extension\>auto        | m  |   |
| _park |             | > \[in\|out\] \[min\] \[max\]\]        | od |   |
|       |             |                                        | _v |   |
|       |             |                                        | al |   |
|       |             |                                        | et |   |
|       |             |                                        | _p |   |
|       |             |                                        | ar |   |
|       |             |                                        | ki |   |
|       |             |                                        | ng |   |
+-------+-------------+----------------------------------------+----+---+
| verb  | Make ALL    |                                        | m  |   |
| ose_e | Events      |                                        | od |   |
| vents | verbose.    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| vi    | Set video   | \[\[onoff\]                            | m  |   |
| deo_d | decode.     |                                        | od |   |
| ecode |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| vid   | Send video  | \[manual\|auto\]                       | m  |   |
| eo_re | refresh.    |                                        | od |   |
| fresh |             |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| vide  | Video write | \<path\> \[\<pos\>\] \[\<alpha\>\]     | m  |   |
| o_wri | overlay     |                                        | od |   |
| te_ov |             |                                        | _d |   |
| erlay |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| wait_ | Wait for    |                                        | m  |   |
| for_a | call to be  |                                        | od |   |
| nswer | answered    |                                        | _d |   |
|       |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
| w     | wait_       | > \<silence_thresh\> \<silence_hits\>  | m  |   |
| ait_f | for_silence | > \<listen_hits\> \<timeout_ms\>       | od |   |
| or_si |             | > \[\<file\>\]                         | _d |   |
| lence |             |                                        | pt |   |
|       |             |                                        | oo |   |
|       |             |                                        | ls |   |
+-------+-------------+----------------------------------------+----+---+
