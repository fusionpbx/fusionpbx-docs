# Voicemail

Voicemail specific default settings.

+----------+-------+-------+--------+-------------------------------+
| Default  | De    | De    | D      | Default Setting Description   |
| Setting  | fault | fault | efault |                               |
| Sub      | Se    | Se    | S      |                               |
| category | tting | tting | etting |                               |
|          | Name  | Value | E      |                               |
|          |       |       | nabled |                               |
+==========+=======+=======+========+===============================+
| voicem   | text  | a     | true   | Define whether to attach      |
| ail[file |       | ttach |        | voicemail files to email      |
| ]{#file} |       |       |        | notifications, or only        |
|          |       |       |        | include a link.               |
+----------+-------+-------+--------+-------------------------------+
| kee      | bo    | true  | true   | Define whether to keep        |
| p[local] | olean |       |        | voicemail files on the local  |
| {#local} |       |       |        | system after sending attached |
|          |       |       |        | via email.                    |
+----------+-------+-------+--------+-------------------------------+
| stor     | text  | b     | false  | Define which storage type     |
| age[type |       | ase64 |        | (base64 stores in the         |
| ]{#type} |       |       |        | database).                    |
+----------+-------+-------+--------+-------------------------------+
| message[ | nu    | 300   | true   | Maximum length of a voicemail |
| max_leng | meric |       |        | (in seconds).                 |
| th]{#max |       |       |        |                               |
| _length} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| p        | nu    | 8     | true   | The default length of         |
| assword[ | meric |       |        | characters in a voicemail     |
| length]{ |       |       |        | password.                     |
| #length} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| di       | bo    | true  | false  | Enable display of             |
| splay[do | olean |       |        | \@domain[name]{#name} after   |
| main_nam |       |       |        | voicemail[id]{#id} when       |
| e]{#doma |       |       |        | rendering emails.             |
| in_name} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| remote[  | bo    | false | true   | Allow access to the voicemail |
| access]{ | olean |       |        | menu with the correct         |
| #access} |       |       |        | voicemail password.           |
+----------+-------+-------+--------+-------------------------------+
| messag   | text  | asc   | true   | Set message order to asc to   |
| e[order] |       |       |        | play oldest message first or  |
| {#order} |       |       |        | desc to play newest message   |
|          |       |       |        | first.                        |
+----------+-------+-------+--------+-------------------------------+
| p        | bo    | true  | false  | Enforce voicemail password    |
| assword[ | olean |       |        | complexity.                   |
| complexi |       |       |        |                               |
| ty]{#com |       |       |        |                               |
| plexity} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| p        | nu    | 4     | false  | Minimum voicemail password    |
| assword[ | meric |       |        | length.                       |
| min_leng |       |       |        |                               |
| th]{#min |       |       |        |                               |
| _length} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| s        | text  |       | true   | > SMTP From: specific to      |
| mtp[from |       |       |        | > Voicemail.                  |
| ]{#from} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| smt      | text  |       | true   | > SMTP From: Name specific to |
| p[from_n |       |       |        | > Voicemail.                  |
| ame]{#fr |       |       |        |                               |
| om_name} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| no       | bo    | false | true   | > Default for not found       |
| t[found_ | olean |       |        | > message.                    |
| message] |       |       |        |                               |
| {#found_ |       |       |        |                               |
| message} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
| g        | nu    | 90    | true   | Maximum length of a voicemail |
| reeting[ | meric |       |        | greeting (in seconds).        |
| max_leng |       |       |        |                               |
| th]{#max |       |       |        |                               |
| _length} |       |       |        |                               |
+----------+-------+-------+--------+-------------------------------+
