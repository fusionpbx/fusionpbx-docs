# Fax

Specific default settings for fax server.

+----------+------+----------+-------+------------------------------+
| Default  | Def  | Default  | De    | Default Setting Description  |
| Setting  | ault | Setting  | fault |                              |
| Sub      | Set  | Value    | Se    |                              |
| category | ting |          | tting |                              |
|          | Name |          | En    |                              |
|          |      |          | abled |                              |
+==========+======+==========+=======+==============================+
| co       | text |          | TRUE  | Path to image/logo file      |
| ver[logo |      |          |       | displayed in the header of   |
| ]{#logo} |      |          |       | the cover sheet.             |
+----------+------+----------+-------+------------------------------+
| allowe   | a    | .pdf     | TRUE  | > Allowed extension to send  |
| d[extens | rray |          |       | > .pdf                       |
| ion]{#ex |      |          |       |                              |
| tension} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| allowe   | a    | .tif     | TRUE  | > Allowed extension to send  |
| d[extens | rray |          |       | > .tif                       |
| ion]{#ex |      |          |       |                              |
| tension} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| allowe   | a    | .tiff    | TRUE  | > Allowed extension to send  |
| d[extens | rray |          |       | > .tiff                      |
| ion]{#ex |      |          |       |                              |
| tension} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| cover[   | text |          | FALSE | Default information          |
| header]{ |      |          |       | displayed beneath the logo   |
| #header} |      |          |       | in the header of the cover   |
|          |      |          |       | sheet.                       |
+----------+------+----------+-------+------------------------------+
| p        | text | letter   | TRUE  | Set the default page size of |
| age[size |      |          |       | new faxes.                   |
| ]{#size} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| re       | text | fine     | TRUE  | Set the default transmission |
| solution |      |          |       | quality of new faxes.        |
+----------+------+----------+-------+------------------------------+
| variable | a    | f        | TRUE  | Enable T.38.                 |
|          | rray | ax[enabl |       |                              |
|          |      | e_t38]{# |       |                              |
|          |      | enable_t |       |                              |
|          |      | 38}=true |       |                              |
+----------+------+----------+-------+------------------------------+
| variable | a    | fa       | TRUE  | Send a T38 reinvite when a   |
|          | rray | x[enable |       | fax tone is detected.        |
|          |      | _t38_req |       |                              |
|          |      | uest]{#e |       |                              |
|          |      | nable_t3 |       |                              |
|          |      | 8_reques |       |                              |
|          |      | t}=false |       |                              |
+----------+------+----------+-------+------------------------------+
| variable | a    | ignore   | TRUE  | Ignore ringing to improve    |
|          | rray | [early_m |       | fax success rate.            |
|          |      | edia]{#e |       |                              |
|          |      | arly_med |       |                              |
|          |      | ia}=true |       |                              |
+----------+------+----------+-------+------------------------------+
| kee      | boo  | TRUE     | TRUE  | Keep the file after sending  |
| p[local] | lean |          |       | or receiving the fax.        |
| {#local} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| s        | text | queue    | FALSE | > Send mode. queue is        |
| end[mode |      |          |       | > default.                   |
| ]{#mode} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| send[re  | num  | 5        | TRUE  | Number of attempts to send   |
| try_limi | eric |          |       | fax (count only calls with   |
| t]{#retr |      |          |       | answer).                     |
| y_limit} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| send[    | num  | 15       | TRUE  | Delay before we make next    |
| retry_in | eric |          |       | call after answered call.    |
| terval]{ |      |          |       |                              |
| #retry_i |      |          |       |                              |
| nterval} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| sen      | num  | 3        | TRUE  | Number of unanswered         |
| d[no_ans | eric |          |       | attempts in sequence.        |
| wer_retr |      |          |       |                              |
| y_limit] |      |          |       |                              |
| {#no_ans |      |          |       |                              |
| wer_retr |      |          |       |                              |
| y_limit} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| s        | num  | 30       | TRUE  | Delay before we make next    |
| end[no_a | eric |          |       | call after no answered call. |
| nswer_re |      |          |       |                              |
| try_inte |      |          |       |                              |
| rval]{#n |      |          |       |                              |
| o_answer |      |          |       |                              |
| _retry_i |      |          |       |                              |
| nterval} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| send[no  | num  | 3        | TRUE  | Giveup reach the destination |
| _answer_ | eric |          |       | after this number of         |
| limit]{# |      |          |       | sequences.                   |
| no_answe |      |          |       |                              |
| r_limit} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| send[    | num  | 300      | TRUE  | Delay before next call       |
| no_answe | eric |          |       | sequence.                    |
| r_interv |      |          |       |                              |
| al]{#no_ |      |          |       |                              |
| answer_i |      |          |       |                              |
| nterval} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| stor     | text | base64   | FALSE | Store FAX in base64.         |
| age[type |      |          |       |                              |
| ]{#type} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| s        | text |          | TRUE  | > SMTP from address.         |
| mtp[from |      |          |       |                              |
| ]{#from} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
| smt      | text |          | TRUE  | > SMTP from name. Depends on |
| p[from_n |      |          |       | > the server, can be full    |
| ame]{#fr |      |          |       | > email or everything before |
| om_name} |      |          |       | > the @ sign.                |
+----------+------+----------+-------+------------------------------+
| co       | text | times    | FALSE | Font used to generate cover  |
| ver[font |      |          |       | page. Can be full path to    |
| ]{#font} |      |          |       | .ttf file or font name       |
|          |      |          |       | alredy installed.            |
+----------+------+----------+-------+------------------------------+
| cover[   | text |          | TRUE  | Notice displayed in the      |
| footer]{ |      |          |       | footer of the cover sheet.   |
| #footer} |      |          |       |                              |
+----------+------+----------+-------+------------------------------+
