# Dialplan Application

Dialplan Application uses FreeSWITCH **show application** to build the
dropdown lists that are found in FusionPBX dialplans. This is a list
from a default install and the list can change depending on how many
FreeSWITCH modules are installed.

+-------+-------------+----------------------------------------+----+---+
| name  | description | syntax                                 | ik |   |
|       |             |                                        | ey |   |
+=======+=============+========================================+====+===+
| a     | Answer the  |                                        | mo |   |
| nswer | call        |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| a     | Attended    | \<channel[url]{#url}\>                 | mo |   |
| tt[xf | Transfer    |                                        | d[ |   |
| er]{# |             |                                        | dp |   |
| xfer} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| bgs   | Execute a   | \<command\>                            | mo |   |
| ystem | system      |                                        | d[ |   |
|       | command in  |                                        | dp |   |
|       | the         |                                        | to |   |
|       | background  |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| bin   | bind a key  | \<realm\>,\<digits\|\~reg              | mo |   |
| d[dig | sequence or | ex\>,\<string\>\[,\<value\>\]\[,\<dtmf | d[ |   |
| it_ac | regex to an | target leg\>\]\[,\<event target        | dp |   |
| tion] | action      | leg\>\]                                | to |   |
| {#dig |             |                                        | ol |   |
| it_ac |             |                                        | s] |   |
| tion} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| bind[ | Bind a key  | \<key\> \[a[\|b\|](##SUBST##|b|)ab\]   | mo |   |
| meta_ | to an       | \[a[\|b\|](##S                         | d[ |   |
| app]{ | application | UBST##|b|)o[\|s\|](##SUBST##|s|)i\|1\] | dp |   |
| #meta |             | \<app\>                                | to |   |
| _app} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| blo   | Block DTMF  |                                        | mo |   |
| ck[dt |             |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| break | Break       |                                        | mo |   |
|       |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| b     | Bridge      | \<channel[url]{#url}\>                 | mo |   |
| ridge | Audio       |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| bri   | Export a    | \<varname\>=\<value\>                  | mo |   |
| dge[e | channel     |                                        | d[ |   |
| xport | variable    |                                        | dp |   |
| ]{#ex | across a    |                                        | to |   |
| port} | bridge      |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| callc | CallCenter  | queue[name]{#name}                     | mo |   |
| enter |             |                                        | d[ |   |
|       |             |                                        | ca |   |
|       |             |                                        | ll |   |
|       |             |                                        | ce |   |
|       |             |                                        | nt |   |
|       |             |                                        | er |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #c |   |
|       |             |                                        | al |   |
|       |             |                                        | lc |   |
|       |             |                                        | en |   |
|       |             |                                        | te |   |
|       |             |                                        | r} |   |
+-------+-------------+----------------------------------------+----+---+
| ca    | capture     | \<varname\>[\|\                        | mo |   |
| pture | data into a | <data\>\|](##SUBST##|<data>|)\<regex\> | d[ |   |
|       | var         |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| c     | Check an ip | \<ip\> \<acl \| cidr\>                 | mo |   |
| heck[ | against an  | \[\<hangup[cause]{#cause}\>\]          | d[ |   |
| acl]{ | ACL list    |                                        | dp |   |
| #acl} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| clea  | clear all   | \<realm\>\|all\[,target\]              | mo |   |
| r[dig | digit       |                                        | d[ |   |
| it_ac | bindings    |                                        | dp |   |
| tion] |             |                                        | to |   |
| {#dig |             |                                        | ol |   |
| it_ac |             |                                        | s] |   |
| tion} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| clea  | Clear       |                                        | mo |   |
| r[spe | Speech      |                                        | d[ |   |
| ech_c | Handle      |                                        | dp |   |
| ache] | Cache       |                                        | to |   |
| {#spe |             |                                        | ol |   |
| ech_c |             |                                        | s] |   |
| ache} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| cng[  | Do PLC on   |                                        | mo |   |
| plc]{ | CNG frames  |                                        | d[ |   |
| #plc} |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| confe | conference  |                                        | mo |   |
| rence |             |                                        | d[ |   |
|       |             |                                        | co |   |
|       |             |                                        | nf |   |
|       |             |                                        | er |   |
|       |             |                                        | en |   |
|       |             |                                        | ce |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #c |   |
|       |             |                                        | on |   |
|       |             |                                        | fe |   |
|       |             |                                        | re |   |
|       |             |                                        | nc |   |
|       |             |                                        | e} |   |
+-------+-------------+----------------------------------------+----+---+
| co    | con         |                                        | mo |   |
| nfere | ference[set |                                        | d[ |   |
| nce[s | _auto_outca |                                        | co |   |
| et_au | ll]{#set_au |                                        | nf |   |
| to_ou | to_outcall} |                                        | er |   |
| tcall |             |                                        | en |   |
| ]{#se |             |                                        | ce |   |
| t_aut |             |                                        | ]{ |   |
| o_out |             |                                        | #c |   |
| call} |             |                                        | on |   |
|       |             |                                        | fe |   |
|       |             |                                        | re |   |
|       |             |                                        | nc |   |
|       |             |                                        | e} |   |
+-------+-------------+----------------------------------------+----+---+
| db    | Insert to   | \[inse                                 | mo |   |
|       | the db      | rt\|delete\]/\<realm\>/\<key\>/\<val\> | d[ |   |
|       |             |                                        | db |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #d |   |
|       |             |                                        | b} |   |
+-------+-------------+----------------------------------------+----+---+
| d     | decode      | \[max[pictures]{#pictures}\]           | mo |   |
| ecode | picture     |                                        | d[ |   |
| [vide |             |                                        | fs |   |
| o]{#v |             |                                        | v] |   |
| ideo} |             |                                        | {# |   |
|       |             |                                        | fs |   |
|       |             |                                        | v} |   |
+-------+-------------+----------------------------------------+----+---+
| dedu  | Prevent     | \[only[rtp]{#rtp}\]                    | mo |   |
| plica | duplicate   |                                        | d[ |   |
| te[dt | inband +    |                                        | dp |   |
| mf]{# | 2833 dtmf   |                                        | to |   |
| dtmf} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| de    | Send call   | \<deflect[data]{#data}\>               | mo |   |
| flect | deflect     |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| del   | echo audio  | \<delay ms\>                           | mo |   |
| ay[ec | at a        |                                        | d[ |   |
| ho]{# | specified   |                                        | dp |   |
| echo} | delay       |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| d     | detect[aud  | > \<threshold\> \<audio[hits]{#hits}\> | mo |   |
| etect | io]{#audio} | > \<timeout[ms]{#ms}\> \[\<file\>\]    | d[ |   |
| [audi |             |                                        | dp |   |
| o]{#a |             |                                        | to |   |
| udio} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| detec | det         | > \<threshold\>                        | mo |   |
| t[sil | ect[silence | > \<silence[hits]{#hits}\>             | d[ |   |
| ence] | ]{#silence} | > \<timeout[ms]{#ms}\> \[\<file\>\]    | dp |   |
| {#sil |             |                                        | to |   |
| ence} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| det   | Detect      | \<mod[name]{#name}\>                   | mo |   |
| ect[s | speech      | \<gram[name]{#name}\>                  | d[ |   |
| peech |             | \<gram[path]{#path}\> \[\<addr\>\] OR  | dp |   |
| ]{#sp |             | grammar \<gram[name]{#name}\>          | to |   |
| eech} |             | \[\<path\>\] OR nogrammar              | ol |   |
|       |             | \<gram[name]{#name}\> OR               | s] |   |
|       |             | grammaron/grammaroff                   | {# |   |
|       |             | \<gram[name]{#name}\> OR               | dp |   |
|       |             | grammarsalloff                         | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
|       |             | OR pause OR resume OR                  |    |   |
|       |             | start[input_timers]{#input_timers} OR  |    |   |
|       |             | stop OR param \<name\> \<value\>       |    |   |
+-------+-------------+----------------------------------------+----+---+
| di    | change      | \<realm\>\[,\<target\>\]               | mo |   |
| git[a | binding     |                                        | d[ |   |
| ction | realm       |                                        | dp |   |
| _set_ |             |                                        | to |   |
| realm |             |                                        | ol |   |
| ]{#ac |             |                                        | s] |   |
| tion_ |             |                                        | {# |   |
| set_r |             |                                        | dp |   |
| ealm} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| di    | Displace    | > \<path\> \[\<flags\>\]               | mo |   |
| splac | File        | > \[+time[limit_ms]{#limit_ms}\]       | d[ |   |
| e[ses |             |                                        | dp |   |
| sion] |             |                                        | to |   |
| {#ses |             |                                        | ol |   |
| sion} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| ea    | Enable      |                                        | mo |   |
| rly[h | early       |                                        | d[ |   |
| angup | hangup      |                                        | dp |   |
| ]{#ha |             |                                        | to |   |
| ngup} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| eave  | eavesdrop   | \[all \| \<uuid\>\]                    | mo |   |
| sdrop | on a uuid   |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| echo  | Echo        |                                        | mo |   |
|       |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| enab  | Enable      | \[0\|\<seconds\>\]                     | mo |   |
| le[he | Media       |                                        | d[ |   |
| artbe | Heartbeat   |                                        | dp |   |
| at]{# |             |                                        | to |   |
| heart |             |                                        | ol |   |
| beat} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| enab  | Enable      | \[0\|\<seconds\>\]                     | mo |   |
| le[ke | Keepalive   |                                        | d[ |   |
| epali |             |                                        | dp |   |
| ve]{# |             |                                        | to |   |
| keepa |             |                                        | ol |   |
| live} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| end   | Playback    | \<path\>                               | mo |   |
| less[ | File        |                                        | d[ |   |
| playb | Endlessly   |                                        | dp |   |
| ack]{ |             |                                        | to |   |
| #play |             |                                        | ol |   |
| back} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| enum  | Perform an  | \[reload \| \<number\> \[\<root\>\]\]  | mo |   |
|       | ENUM lookup |                                        | d[ |   |
|       |             |                                        | en |   |
|       |             |                                        | um |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #e |   |
|       |             |                                        | nu |   |
|       |             |                                        | m} |   |
+-------+-------------+----------------------------------------+----+---+
| eval  | Do Nothing  |                                        | mo |   |
|       |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| event | Fire an     |                                        | mo |   |
|       | event       |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| execu | Execute an  | \<extension\> \<dialplan\> \<context\> | mo |   |
| te[ex | extension   |                                        | d[ |   |
| tensi |             |                                        | dp |   |
| on]{# |             |                                        | to |   |
| exten |             |                                        | ol |   |
| sion} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| e     | Export a    | \<varname\>=\<value\>                  | mo |   |
| xport | channel     |                                        | d[ |   |
|       | variable    |                                        | dp |   |
|       | across a    |                                        | to |   |
|       | bridge      |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| fax[d | Detect      |                                        | mo |   |
| etect | faxes       |                                        | d[ |   |
| ]{#de |             |                                        | dp |   |
| tect} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| fifo  | Park with   | \<fifo                                 | mo |   |
|       | FIFO        | name                                   | d[ |   |
|       |             | \>\[!\<importance[number]{#number}\>\] | fi |   |
|       |             | \[in \[\<announce file\>[\|undef\]     | fo |   |
|       |             | \[\<music                              | ]{ |   |
|       |             | file\>\|](#                            | #f |   |
|       |             | #SUBST##|undef] [<music file>|)undef\] | if |   |
|       |             | \| out \[wait[\|nowait\] \[\<announce  | o} |   |
|       |             | file\>\|](##SUB                        |    |   |
|       |             | ST##|nowait] [<announce file>|)undef\] |    |   |
|       |             | \[\<music file\>\|undef\]\]            |    |   |
+-------+-------------+----------------------------------------+----+---+
| fifo  | Count a     | > \                                    | mo |   |
| [trac | call as a   | <fifo[outbound_uuid]{#outbound_uuid}\> | d[ |   |
| k_cal | fifo call   |                                        | fi |   |
| l]{#t | in the      |                                        | fo |   |
| rack_ | manual[cal  |                                        | ]{ |   |
| call} | ls]{#calls} |                                        | #f |   |
|       | queue       |                                        | if |   |
|       |             |                                        | o} |   |
+-------+-------------+----------------------------------------+----+---+
| fire  | fire the    |                                        | mo |   |
|       | message     |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| flu   | flush any   |                                        | mo |   |
| sh[dt | queued dtmf |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| gen   | Generate    | \<                                     | mo |   |
| tones | Tones       | tgml[script]{#script}\>\[\|\<loops\>\] | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| group | Manage a    | \[insert\|delete\]:\<group             | mo |   |
|       | group       | name\>:\<val\>                         | d[ |   |
|       |             |                                        | db |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #d |   |
|       |             |                                        | b} |   |
+-------+-------------+----------------------------------------+----+---+
| h     | Hangup the  | \[\<cause\>\]                          | mo |   |
| angup | call        |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| hash  | Insert into | \[                                     | mo |   |
|       | the         | insert[\|insert_ifempty\|](##SUBST##|i | d[ |   |
|       | hashtable   | nsert_ifempty|)delete\|delete[ifmatch] | ha |   |
|       |             | {#ifmatch}\]/\<realm\>/\<key\>/\<val\> | sh |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #h |   |
|       |             |                                        | as |   |
|       |             |                                        | h} |   |
+-------+-------------+----------------------------------------+----+---+
| hold  | Send a hold | \[\<display message\>\]                | mo |   |
|       | message     |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| info  | Display     |                                        | mo |   |
|       | Call Info   |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| info  | Display     |                                        | mo |   |
|       | Call Info   |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| inte  | intercept   | \[-bleg\] \<uuid\>                     | mo |   |
| rcept |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| ivr   | Run an ivr  |                                        | mo |   |
|       | menu        |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| ji    | Send        | > \<jitterbuffer[data]{#data}\>        | mo |   |
| tterb | session     |                                        | d[ |   |
| uffer | j           |                                        | dp |   |
|       | itterbuffer |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| limit | Limit       | > \<backend\> \<realm\> \<id\>         | mo |   |
|       |             | > \[\<max\>\[/interval\]\] \[number    | d[ |   |
|       |             | > \[dialplan \[context\]\]\]           | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| limi  | Limit       | > \<backend\> \<realm\> \<id\>         | mo |   |
| t[exe |             | > \<max\>\[/interval\] \<application\> | d[ |   |
| cute] |             | > \[application arguments\]            | dp |   |
| {#exe |             |                                        | to |   |
| cute} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| lim   | Limit       | > \<realm\> \<id\>                     | mo |   |
| it[ha |             | > \[\<max\>\[/interval\]\] \[number    | d[ |   |
| sh]{# |             | > \[dialplan \[context\]\]\]           | dp |   |
| hash} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| limi  | Limit       | > \<realm\> \<id\>                     | mo |   |
| t[has |             | > \<max\>\[/interval\] \<application\> | d[ |   |
| h_exe |             | > \[application arguments\]            | dp |   |
| cute] |             |                                        | to |   |
| {#has |             |                                        | ol |   |
| h_exe |             |                                        | s] |   |
| cute} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| log   | Logs to the | \<log[level]{#level}\>                 | mo |   |
|       | logger      | \<log[string]{#string}\>               | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| loop[ | Playback    | \[+loops\] \<path\>                    | mo |   |
| playb | File looply |                                        | d[ |   |
| ack]{ |             |                                        | dp |   |
| #play |             |                                        | to |   |
| back} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| media | Reset all   |                                        | mo |   |
| [rese | b           |                                        | d[ |   |
| t]{#r | ypass/proxy |                                        | dp |   |
| eset} | media flags |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| mkdir | Create a    | > \<path\>                             | mo |   |
|       | directory   |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| mul   | Set many    | \[\^\^\<delim\>\]\<varname\>=\<value\> | mo |   |
| tiset | channel     | \<var2\>=\<val2\>                      | d[ |   |
|       | variables   |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| multi | Unset many  | \[\^\^\<delim\>\]\<varname\> \<var2\>  | mo |   |
| unset | channel     | \<var3\>                               | d[ |   |
|       | variables   |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| mutex | block on a  | \<keyname\>\[ on\|off\]                | mo |   |
|       | call flow   |                                        | d[ |   |
|       | only        |                                        | dp |   |
|       | allowing    |                                        | to |   |
|       | one at a    |                                        | ol |   |
|       | time        |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| no    | Refuse      |                                        | mo |   |
| video | Inbound     |                                        | d[ |   |
|       | Video       |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| park  | Park        |                                        | mo |   |
|       |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| park  | Park State  |                                        | mo |   |
| [stat |             |                                        | d[ |   |
| e]{#s |             |                                        | dp |   |
| tate} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| p     | Say a       | \<macro[name]{#name}\>,\<data\>        | mo |   |
| hrase | Phrase      |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| p     | Pickup      | \[\<key\>\]                            | mo |   |
| ickup |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| pla   | Play and do | \<file\> detect:\<engine\>             | mo |   |
| y[and | speech      | {param1=val1,param2=val2}\<grammar\>   | d[ |   |
| _dete | recognition |                                        | dp |   |
| ct_sp |             |                                        | to |   |
| eech] |             |                                        | ol |   |
| {#and |             |                                        | s] |   |
| _dete |             |                                        | {# |   |
| ct_sp |             |                                        | dp |   |
| eech} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| pl    | Play and    | > \<min\> \<max\> \<tries\>            | >  |   |
| ay[an | get Digits  | > \<timeout\> \<terminators\> \<file\> | mo |   |
| d_get |             | > \<invalid[file]{#file}\>             | d[ |   |
| _digi |             | > \<var[name]{#name}\> \<regexp\>      | dp |   |
| ts]{# |             | > \[\<digit[timeout]{#timeout}\>\]     | to |   |
| and_g |             | > \[\'\<failure[ext]{#ext}\>           | ol |   |
| et_di |             | > \[failure[dp]{#dp}                   | s] |   |
| gits} |             | > \[failure[context]{#context}\]\]\'\] | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| play[ | play a fsv  | \<file\>                               | mo |   |
| fsv]{ | file        |                                        | d[ |   |
| #fsv} |             |                                        | fs |   |
|       |             |                                        | v] |   |
|       |             |                                        | {# |   |
|       |             |                                        | fs |   |
|       |             |                                        | v} |   |
+-------+-------------+----------------------------------------+----+---+
| play[ | play a yvv  | > \<file\> \[width\] \[height\]        | mo |   |
| yuv]{ | file        |                                        | d[ |   |
| #yuv} |             |                                        | fs |   |
|       |             |                                        | v] |   |
|       |             |                                        | {# |   |
|       |             |                                        | fs |   |
|       |             |                                        | v} |   |
+-------+-------------+----------------------------------------+----+---+
| pla   | Playback    | > \<path\>                             | mo |   |
| yback | File        |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| pre[a | Pre-Answer  |                                        | mo |   |
| nswer | the call    |                                        | d[ |   |
| ]{#an |             |                                        | dp |   |
| swer} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| prepr | pre-process |                                        | mo |   |
| ocess |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| pre   | Send        | > \<rpid\> \<status\> \[\<id\>\]       | mo |   |
| sence | Presence    |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| pr    | Set privacy | off[\|on\|](##SUBST##|on|              | mo |   |
| ivacy | on calls    | )name[\|full\|](##SUBST##|full|)number | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| push  | Set a       | \<varname\>=\<value\>                  | mo |   |
|       | channel     |                                        | d[ |   |
|       | variable    |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| que   | Queue dtmf  | \<dtmf[data]{#data}\>                  | mo |   |
| ue[dt | to be sent  |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| read  | Read Digits | \<min\> \<max\> \<file\>               | mo |   |
|       |             | \<var[name]{#name}\> \<timeout\>       | d[ |   |
|       |             | \<terminators\>                        | dp |   |
|       |             | \<digit[timeout]{#timeout}\>           | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Record File | > \<path\>                             | mo |   |
| ecord |             | >                                      | d[ |   |
|       |             |  \[\<time[limit_secs]{#limit_secs}\>\] | dp |   |
|       |             | > \[\<silence[thresh]{#thresh}\>\]     | to |   |
|       |             | > \[\<silence[hits]{#hits}\>\]         | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| re    | record an   | > \<file\>                             | mo |   |
| cord[ | fsv file    |                                        | d[ |   |
| fsv]{ |             |                                        | fs |   |
| #fsv} |             |                                        | v] |   |
|       |             |                                        | {# |   |
|       |             |                                        | fs |   |
|       |             |                                        | v} |   |
+-------+-------------+----------------------------------------+----+---+
| recor | Record      | > \<path\> \[+\<timeout\>\]            | mo |   |
| d[ses | Session     |                                        | d[ |   |
| sion] |             |                                        | dp |   |
| {#ses |             |                                        | to |   |
| sion} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| recor | Mask audio  | \<path\>                               | mo |   |
| d[ses | in          |                                        | d[ |   |
| sion_ | recording   |                                        | dp |   |
| mask] |             |                                        | to |   |
| {#ses |             |                                        | ol |   |
| sion_ |             |                                        | s] |   |
| mask} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| reco  | Resume      | > \<path\>                             | mo |   |
| rd[se | recording   |                                        | d[ |   |
| ssion |             |                                        | dp |   |
| _unma |             |                                        | to |   |
| sk]{# |             |                                        | ol |   |
| sessi |             |                                        | s] |   |
| on_un |             |                                        | {# |   |
| mask} |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| re    | Send call   |                                        | mo |   |
| cover | recov       |                                        | d[ |   |
| y[ref | ery[refresh |                                        | dp |   |
| resh] | ]{#refresh} |                                        | to |   |
| {#ref |             |                                        | ol |   |
| resh} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| red   | Send        | > \<redirect[data]{#data}\>            | mo |   |
| irect | session     |                                        | d[ |   |
|       | redirect    |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| remo  | Remove      | \[\<function\>\]                       | mo |   |
| ve[bu | media bugs  |                                        | d[ |   |
| gs]{# |             |                                        | dp |   |
| bugs} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| r     | Rename file | \<from[path]{#path}\>                  | mo |   |
| ename |             | \<to[path]{#path}\>                    | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| reply | reply to a  |                                        | mo |   |
|       | message     |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| re    | Send        | \<respond[data]{#data}\>               | mo |   |
| spond | session     |                                        | d[ |   |
|       | respond     |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| ring  | Indicate    |                                        | mo |   |
| [read | Ring[Rea    |                                        | d[ |   |
| y]{#r | dy]{#ready} |                                        | dp |   |
| eady} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| rxfax | FAX Receive | \<filename\>                           | mo |   |
|       | Application |                                        | d[ |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| say   | say         | \<module[name]{#name}\>\[:\<lang\>\]   | mo |   |
|       |             | \<say[type]{#type}\>                   | d[ |   |
|       |             | \<say[method]{#method}\>               | dp |   |
|       |             | \[\<say[gender]{#gender}\>\] \<text\>  | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sch   | Schedule a  | \[+\]\<time\> \<path\>                 | mo |   |
| ed[br | broadcast   | \                                      | d[ |   |
| oadca | in the      | [aleg[\|bleg\|](##SUBST##|bleg|)both\] | dp |   |
| st]{# | future      |                                        | to |   |
| broad |             |                                        | ol |   |
| cast} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sc    | cancel      | \[group\]                              | mo |   |
| hed[c | scheduled   |                                        | d[ |   |
| ancel | tasks       |                                        | dp |   |
| ]{#ca |             |                                        | to |   |
| ncel} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sc    | Schedule a  | \[+\]\<time\> \[\<cause\>\]            | mo |   |
| hed[h | hangup in   |                                        | d[ |   |
| angup | the future  |                                        | dp |   |
| ]{#ha |             |                                        | to |   |
| ngup} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sch   | Enable      | \[0\|\<seconds\>\]                     | mo |   |
| ed[he | Scheduled   |                                        | d[ |   |
| artbe | Heartbeat   |                                        | dp |   |
| at]{# |             |                                        | to |   |
| heart |             |                                        | ol |   |
| beat} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Schedule a  | \[+\]\<time\> \<extension\>            | mo |   |
| ched[ | transfer in | \<dialplan\> \<context\>               | d[ |   |
| trans | the future  |                                        | dp |   |
| fer]{ |             |                                        | to |   |
| #tran |             |                                        | ol |   |
| sfer} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| send  | send the    |                                        | mo |   |
|       | message     |                                        | d[ |   |
|       | as-is       |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sen   | Send        | > \<text\>                             | mo |   |
| d[dis | session a   |                                        | d[ |   |
| play] | new display |                                        | dp |   |
| {#dis |             |                                        | to |   |
| play} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| se    | Send dtmf   | > \<dtmf[data]{#data}\>                | mo |   |
| nd[dt | to be sent  |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| se    | Send info   | > \<info\>                             | mo |   |
| nd[in |             |                                        | d[ |   |
| fo]{# |             |                                        | dp |   |
| info} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| ses   | sessio      | > \<level\>                            | mo |   |
| sion[ | n[loglevel] |                                        | d[ |   |
| logle | {#loglevel} |                                        | dp |   |
| vel]{ |             |                                        | to |   |
| #logl |             |                                        | ol |   |
| evel} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set   | set a       |                                        | mo |   |
|       | variable    |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set   | Set a       | \<varname\>=\<value\>                  | mo |   |
|       | channel     |                                        | d[ |   |
|       | variable    |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set[a | set volume  |                                        | mo |   |
| udio_ |             |                                        | d[ |   |
| level |             |                                        | dp |   |
| ]{#au |             |                                        | to |   |
| dio_l |             |                                        | ol |   |
| evel} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set[g | Set a       | \<varname\>=\<value\>                  | mo |   |
| lobal | global      |                                        | d[ |   |
| ]{#gl | variable    |                                        | dp |   |
| obal} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set[m | Set Media   |                                        | mo |   |
| edia_ | Stats       |                                        | d[ |   |
| stats |             |                                        | dp |   |
| ]{#me |             |                                        | to |   |
| dia_s |             |                                        | ol |   |
| tats} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | set mute    |                                        | mo |   |
| et[mu |             |                                        | d[ |   |
| te]{# |             |                                        | dp |   |
| mute} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Name the    | \<name\>                               | mo |   |
| et[na | channel     |                                        | d[ |   |
| me]{# |             |                                        | dp |   |
| name} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set[p | Set a       | \<varname\>=\<value\>                  | mo |   |
| rofil | caller      |                                        | d[ |   |
| e_var | profile     |                                        | dp |   |
| ]{#pr | variable    |                                        | to |   |
| ofile |             |                                        | ol |   |
| _var} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Set a User  | \<user\>@\<domain\> \[prefix\]         | mo |   |
| et[us |             |                                        | d[ |   |
| er]{# |             |                                        | dp |   |
| user} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| set[z | Enable      |                                        | mo |   |
| ombie | Zombie      |                                        | d[ |   |
| _exec | Execution   |                                        | dp |   |
| ]{#zo |             |                                        | to |   |
| mbie_ |             |                                        | ol |   |
| exec} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sleep | Pause a     | \<pausemilliseconds\>                  | mo |   |
|       | channel     |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Connect to  | \<ip\>\[:\<port\>\]                    | mo |   |
| ocket | a socket    |                                        | d[ |   |
|       |             |                                        | ev |   |
|       |             |                                        | en |   |
|       |             |                                        | t_ |   |
|       |             |                                        | so |   |
|       |             |                                        | ck |   |
|       |             |                                        | et |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #e |   |
|       |             |                                        | ve |   |
|       |             |                                        | nt |   |
|       |             |                                        | _s |   |
|       |             |                                        | oc |   |
|       |             |                                        | ke |   |
|       |             |                                        | t} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | private     | > \<uuid\>                             | mo |   |
| ofia[ | sofia sla   |                                        | d[ |   |
| sla]{ | function    |                                        | so |   |
| #sla} |             |                                        | fi |   |
|       |             |                                        | a] |   |
|       |             |                                        | {# |   |
|       |             |                                        | so |   |
|       |             |                                        | fi |   |
|       |             |                                        | a} |   |
+-------+-------------+----------------------------------------+----+---+
| so    | Put a       | > \<unhold key\> \[\<moh[a]{#a}\>\]    | mo |   |
| ft[ho | bridged     | > \[\<moh[b]{#b}\>\]                   | d[ |   |
| ld]{# | channel on  |                                        | dp |   |
| hold} | hold        |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sou   | Analyze     |                                        | mo |   |
| nd[te | Audio       |                                        | d[ |   |
| st]{# |             |                                        | dp |   |
| test} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | Detect TDD  |                                        | mo |   |
| andsp | data        |                                        | d[ |   |
| [dete |             |                                        | sp |   |
| ct_td |             |                                        | an |   |
| d]{#d |             |                                        | ds |   |
| etect |             |                                        | p] |   |
| _tdd} |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | Send TDD    |                                        | mo |   |
| andsp | data        |                                        | d[ |   |
| [inje |             |                                        | sp |   |
| ct_td |             |                                        | an |   |
| d]{#i |             |                                        | ds |   |
| nject |             |                                        | p] |   |
| _tdd} |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| spa   | Send TDD    |                                        | mo |   |
| ndsp[ | data        |                                        | d[ |   |
| send_ |             |                                        | sp |   |
| tdd]{ |             |                                        | an |   |
| #send |             |                                        | ds |   |
| _tdd} |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | Detect dtmf |                                        | mo |   |
| andsp |             |                                        | d[ |   |
| [star |             |                                        | sp |   |
| t_dtm |             |                                        | an |   |
| f]{#s |             |                                        | ds |   |
| tart_ |             |                                        | p] |   |
| dtmf} |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| span  | start fax   | \<app\>\[ \<arg\>\]\[ \<timeout\>\]\[  | mo |   |
| dsp[s | detect      | \<tone[type]{#type}\>\]                | d[ |   |
| tart_ |             |                                        | sp |   |
| fax_d |             |                                        | an |   |
| etect |             |                                        | ds |   |
| ]{#st |             |                                        | p] |   |
| art_f |             |                                        | {# |   |
| ax_de |             |                                        | sp |   |
| tect} |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Start       | \<name\>                               | mo |   |
| pands | background  |                                        | d[ |   |
| p[sta | tone        |                                        | sp |   |
| rt_to | detection   |                                        | an |   |
| ne_de | with        |                                        | ds |   |
| tect] | cadence     |                                        | p] |   |
| {#sta |             |                                        | {# |   |
| rt_to |             |                                        | sp |   |
| ne_de |             |                                        | an |   |
| tect} |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | stop        |                                        | mo |   |
| andsp | sending tdd |                                        | d[ |   |
| [stop |             |                                        | sp |   |
| _dete |             |                                        | an |   |
| ct_td |             |                                        | ds |   |
| d]{#s |             |                                        | p] |   |
| top_d |             |                                        | {# |   |
| etect |             |                                        | sp |   |
| _tdd} |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| spand | stop inband |                                        | mo |   |
| sp[st | dtmf        |                                        | d[ |   |
| op_dt |             |                                        | sp |   |
| mf]{# |             |                                        | an |   |
| stop_ |             |                                        | ds |   |
| dtmf} |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | stop fax    |                                        | mo |   |
| andsp | detect      |                                        | d[ |   |
| [stop |             |                                        | sp |   |
| _fax_ |             |                                        | an |   |
| detec |             |                                        | ds |   |
| t]{#s |             |                                        | p] |   |
| top_f |             |                                        | {# |   |
| ax_de |             |                                        | sp |   |
| tect} |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| sp    | stop        |                                        | mo |   |
| andsp | sending tdd |                                        | d[ |   |
| [stop |             |                                        | sp |   |
| _inje |             |                                        | an |   |
| ct_td |             |                                        | ds |   |
| d]{#s |             |                                        | p] |   |
| top_i |             |                                        | {# |   |
| nject |             |                                        | sp |   |
| _tdd} |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| span  | Stop        |                                        | mo |   |
| dsp[s | background  |                                        | d[ |   |
| top_t | tone        |                                        | sp |   |
| one_d | detection   |                                        | an |   |
| etect | with        |                                        | ds |   |
| ]{#st | cadence     |                                        | p] |   |
| op_to |             |                                        | {# |   |
| ne_de |             |                                        | sp |   |
| tect} |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| speak | Speak text  | \<engine\>[\|\<                        | mo |   |
|       |             | voice\>\|](##SUBST##|<voice>|)\<text\> | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| sta   | Detect dtmf |                                        | mo |   |
| rt[dt |             |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Generate    |                                        | mo |   |
| tart[ | dtmf        |                                        | d[ |   |
| dtmf_ |             |                                        | dp |   |
| gener |             |                                        | to |   |
| ate]{ |             |                                        | ol |   |
| #dtmf |             |                                        | s] |   |
| _gene |             |                                        | {# |   |
| rate} |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | stop        |                                        | mo |   |
|       | execution   |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| stop  | Do Nothing  |                                        | mo |   |
|       |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Stop        | \<path\>                               | mo |   |
| top[d | Displace    |                                        | d[ |   |
| ispla | File        |                                        | dp |   |
| ce_se |             |                                        | to |   |
| ssion |             |                                        | ol |   |
| ]{#di |             |                                        | s] |   |
| splac |             |                                        | {# |   |
| e_ses |             |                                        | dp |   |
| sion} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| st    | stop inband |                                        | mo |   |
| op[dt | dtmf        |                                        | d[ |   |
| mf]{# |             |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| stop[ | stop inband | \[write\]                              | mo |   |
| dtmf_ | dtmf        |                                        | d[ |   |
| gener | generation  |                                        | dp |   |
| ate]{ |             |                                        | to |   |
| #dtmf |             |                                        | ol |   |
| _gene |             |                                        | s] |   |
| rate} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| st    | Stop Record | \<path\>                               | mo |   |
| op[re | Session     |                                        | d[ |   |
| cord_ |             |                                        | dp |   |
| sessi |             |                                        | to |   |
| on]{# |             |                                        | ol |   |
| recor |             |                                        | s] |   |
| d_ses |             |                                        | {# |   |
| sion} |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | stop        |                                        | mo |   |
| top[t | detecting   |                                        | d[ |   |
| one_d | tones       |                                        | dp |   |
| etect |             |                                        | to |   |
| ]{#to |             |                                        | ol |   |
| ne_de |             |                                        | s] |   |
| tect} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| st    | Stop video  | > \<path\>                             | mo |   |
| op[vi | write       |                                        | d[ |   |
| deo_w | overlay     |                                        | dp |   |
| rite_ |             |                                        | to |   |
| overl |             |                                        | ol |   |
| ay]{# |             |                                        | s] |   |
| video |             |                                        | {# |   |
| _writ |             |                                        | dp |   |
| e_ove |             |                                        | to |   |
| rlay} |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| st    | Stop FAX    |                                        | mo |   |
| opfax | Application |                                        | d[ |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| str   | strftime    | \[\<epoch\>\|\]\<format string\>       | mo |   |
| ftime |             |                                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | execute a   |                                        | mo |   |
| ystem | system      |                                        | d[ |   |
|       | command     |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| s     | Execute a   | > \<command\>                          | mo |   |
| ystem | system      |                                        | d[ |   |
|       | command     |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| t3    | Convert to  |                                        | mo |   |
| 8[gat | T38 Gateway |                                        | d[ |   |
| eway] | if tones    |                                        | sp |   |
| {#gat | are heard   |                                        | an |   |
| eway} |             |                                        | ds |   |
|       |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| t     | three way   | \<uuid\>                               | mo |   |
| hree[ | call with a |                                        | d[ |   |
| way]{ | uuid        |                                        | dp |   |
| #way} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| t     | Detect      |                                        | mo |   |
| one[d | tones       |                                        | d[ |   |
| etect |             |                                        | dp |   |
| ]{#de |             |                                        | to |   |
| tect} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| tra   | Transfer a  | > \<exten\> \[\<dialplan\>             | mo |   |
| nsfer | channel     | > \<context\>\]                        | d[ |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| t     | Transfer    | \<\                                    | mo |   |
| ransf | variables   | ~variable[prefix]{#prefix}\|variable\> | d[ |   |
| er[va |             |                                        | dp |   |
| rs]{# |             |                                        | to |   |
| vars} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| txfax | FAX         | \<filename\>                           | mo |   |
|       | Transmit    |                                        | d[ |   |
|       | Application |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sp |   |
|       |             |                                        | an |   |
|       |             |                                        | ds |   |
|       |             |                                        | p} |   |
+-------+-------------+----------------------------------------+----+---+
| un    | Unbind a    | \[\<key\>\]                            | mo |   |
| bind[ | key from an |                                        | d[ |   |
| meta_ | application |                                        | dp |   |
| app]{ |             |                                        | to |   |
| #meta |             |                                        | ol |   |
| _app} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| unblo | Stop        |                                        | mo |   |
| ck[dt | blocking    |                                        | d[ |   |
| mf]{# | DTMF        |                                        | dp |   |
| dtmf} |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| u     | Send a      |                                        | mo |   |
| nhold | un-hold     |                                        | d[ |   |
|       | message     |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| u     | Tell        |                                        | mo |   |
| nloop | loopback to |                                        | d[ |   |
|       | unfold      |                                        | lo |   |
|       |             |                                        | op |   |
|       |             |                                        | ba |   |
|       |             |                                        | ck |   |
|       |             |                                        | ]{ |   |
|       |             |                                        | #l |   |
|       |             |                                        | oo |   |
|       |             |                                        | pb |   |
|       |             |                                        | ac |   |
|       |             |                                        | k} |   |
+-------+-------------+----------------------------------------+----+---+
| unset | unset a     |                                        | mo |   |
|       | variable    |                                        | d[ |   |
|       |             |                                        | sm |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | sm |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| unset | Unset a     | > \<varname\>                          | mo |   |
|       | channel     |                                        | d[ |   |
|       | variable    |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| un    | Set a       | \<varname\>=\<value\>                  | mo |   |
| shift | channel     |                                        | d[ |   |
|       | variable    |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| val   | valet[p     | > \<lotname\> \<extension\>[\|\[ask    | mo |   |
| et[pa | ark]{#park} | > \[\<min\>\] \[\<max\>\] \[\<to\>\]   | d[ |   |
| rk]{# |             | > \[\<prompt\>\]\|](##SUBST##|[ask [   | va |   |
| park} |             | <min>] [<max>] [<to>] [<prompt>]|)auto | le |   |
|       |             | > \[in\|out\] \[min\] \[max\]\]        | t_ |   |
|       |             |                                        | pa |   |
|       |             |                                        | rk |   |
|       |             |                                        | in |   |
|       |             |                                        | g] |   |
|       |             |                                        | {# |   |
|       |             |                                        | va |   |
|       |             |                                        | le |   |
|       |             |                                        | t_ |   |
|       |             |                                        | pa |   |
|       |             |                                        | rk |   |
|       |             |                                        | in |   |
|       |             |                                        | g} |   |
+-------+-------------+----------------------------------------+----+---+
| verb  | Make ALL    |                                        | mo |   |
| ose[e | Events      |                                        | d[ |   |
| vents | verbose.    |                                        | dp |   |
| ]{#ev |             |                                        | to |   |
| ents} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| vi    | Set video   | \[\                                    | mo |   |
| deo[d | decode.     | [on[\|wait\]\|](##SUBST##|wait]|)off\] | d[ |   |
| ecode |             |                                        | dp |   |
| ]{#de |             |                                        | to |   |
| code} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| vide  | Send video  | \[manual\|auto\]                       | mo |   |
| o[ref | refresh.    |                                        | d[ |   |
| resh] |             |                                        | dp |   |
| {#ref |             |                                        | to |   |
| resh} |             |                                        | ol |   |
|       |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| v     | Video write | \<path\> \[\<pos\>\] \[\<alpha\>\]     | mo |   |
| ideo[ | overlay     |                                        | d[ |   |
| write |             |                                        | dp |   |
| _over |             |                                        | to |   |
| lay]{ |             |                                        | ol |   |
| #writ |             |                                        | s] |   |
| e_ove |             |                                        | {# |   |
| rlay} |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| wait  | Wait for    |                                        | mo |   |
| [for_ | call to be  |                                        | d[ |   |
| answe | answered    |                                        | dp |   |
| r]{#f |             |                                        | to |   |
| or_an |             |                                        | ol |   |
| swer} |             |                                        | s] |   |
|       |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
| w     | wait[for_   | > \<silence[thresh]{#thresh}\>         | mo |   |
| ait[f | silence]{#f | > \<silence[hits]{#hits}\>             | d[ |   |
| or_si | or_silence} | > \<listen[hits]{#hits}\>              | dp |   |
| lence |             | > \<timeout[ms]{#ms}\> \[\<file\>\]    | to |   |
| ]{#fo |             |                                        | ol |   |
| r_sil |             |                                        | s] |   |
| ence} |             |                                        | {# |   |
|       |             |                                        | dp |   |
|       |             |                                        | to |   |
|       |             |                                        | ol |   |
|       |             |                                        | s} |   |
+-------+-------------+----------------------------------------+----+---+
