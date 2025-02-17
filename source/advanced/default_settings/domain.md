# Domain

Domain specific defaults.

+-----+---+---------------------------------------+----+-------------+
| D   | D | Default Setting Value                 | D  | Default     |
| efa | e |                                       | ef | Setting     |
| ult | f |                                       | au | Description |
| S   | a |                                       | lt |             |
| ett | u |                                       | S  |             |
| ing | l |                                       | et |             |
| Su  | t |                                       | ti |             |
| bca | S |                                       | ng |             |
| teg | e |                                       | E  |             |
| ory | t |                                       | na |             |
|     | t |                                       | bl |             |
|     | i |                                       | ed |             |
|     | n |                                       |    |             |
|     | g |                                       |    |             |
|     | N |                                       |    |             |
|     | a |                                       |    |             |
|     | m |                                       |    |             |
|     | e |                                       |    |             |
+=====+===+=======================================+====+=============+
| dia | t | {sip[i                                | TR | > The dial  |
| l[s | e | nvite_domain]{#invite_domain}=\${doma | UE | > string    |
| tri | x | in[name]{#name}},leg[timeout]{#timeou |    | > used      |
| ng] | t | t}=\${call[timeout]{#timeout}},presen |    |             |
| {#s |   | ce[id]{#id}=\${dialed[user]{#user}}@\ |    |             |
| tri |   | ${dialed[domain]{#domain}}}\${sofia[c |    |             |
| ng} |   | ontact]{#contact}(\*/\${dialed[user]{ |    |             |
|     |   | #user}}@\${dialed[domain]{#domain}})} |    |             |
+-----+---+---------------------------------------+----+-------------+
| te  | n | default                               | TR | > The       |
| mpl | a |                                       | UE | > template  |
| ate | m |                                       |    | > used      |
|     | e |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
| m   | u | b4750c3f-2a86-b00d-b7d0-345c14eca286  | TR | > The menu  |
| enu | u |                                       | UE | > uuid      |
|     | i |                                       |    |             |
|     | d |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
| la  | c | en-us                                 | TR | > Choose    |
| ngu | o |                                       | UE | > the       |
| age | d |                                       |    | > language  |
|     | e |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
| c   | a |                                       | F  | > Allow     |
| idr | r |                                       | AL | > only      |
|     | r |                                       | SE | > specific  |
|     | a |                                       |    | > ip        |
|     | y |                                       |    | > addresses |
|     |   |                                       |    | > access    |
+-----+---+---------------------------------------+----+-------------+
| c   | c | us                                    | TR | > The       |
| oun | o |                                       | UE | > country   |
| try | d |                                       |    | > code      |
|     | e |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
| bri | t | outbound                              | TR | outbound,l  |
| dge | e |                                       | UE | oopback,lcr |
|     | x |                                       |    |             |
|     | t |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
| pag | n | 100                                   | TR | Set the     |
| ing | u |                                       | UE | maximum     |
|     | m |                                       |    | number of   |
|     | e |                                       |    | records     |
|     | r |                                       |    | displayed   |
|     | i |                                       |    | per page.   |
|     | c |                                       |    | (Default:   |
|     |   |                                       |    | 50)         |
+-----+---+---------------------------------------+----+-------------+
| ti  | n | America/Los[Angeles]{#angeles}        | TR | Time zone   |
| me[ | a |                                       | UE | used.       |
| zon | m |                                       |    | Follows     |
| e]{ | e |                                       |    | UNIX format |
| #zo |   |                                       |    |             |
| ne} |   |                                       |    |             |
+-----+---+---------------------------------------+----+-------------+
