# Dialplan Manager

The dialplan is used to setup call destinations based on conditions and
context. You can use the dialplan to send calls to gateways, auto
attendants, external numbers, to scripts, or any destination.

| Dialplan Name                    | Dialplan Number                  |
| -------------------------------- | -------------------------------- |
| [caller-details](dialp           |                                  |
| lan_details.html#caller-details) |                                  |
| > -   *Details about the         |                                  |
| >     caller.*                   |                                  |
| **not-found:**                   |                                  |
| -   *Used to help trigger        |                                  |
|     fail2ban from bogus calls.*  |                                  |
| **call-limit:**                  |                                  |
| -   *Limit calls based on number |                                  |
|     of calls and more.*          |                                  |
| **speed_dial:**                  | \*0\[ext\]                       |
| -   *Uses LUA for extension      |                                  |
|     speed dial.*                 |                                  |
| **agent_status:**                | \*22                             |
| -   *Agent login to call         |                                  |
|     center.*                     |                                  |
| **page-extension:**              | \*8\[ext\]                       |
| -   *Password protected paging   |                                  |
|     of an extension.*            |                                  |
| **eavesdrop:**                   | \*33\[ext\]                      |
| -   *Password protected          |                                  |
|     evesdropping on extensions.* |                                  |
| **send_to_voicemail:**           | \*99\[ext\]                      |
| -   *Sending an active call to   |                                  |
|     an extensions voicemail.*    |                                  |
| **cf:**                          | cf                               |
| -                                |                                  |
| **echo:**                        | \*9196                           |
| -   *Real time echo test.*       |                                  |
| **milliwatt:**                   | \*9197                           |
| -   *Plays a milliwatt test      |                                  |
|     tone.*                       |                                  |
| **recordings:**                  | \*732                            |
| \* *Password protected way to    |                                  |
| record audio that can be used    |                                  |
| in* *other applications like     |                                  |
| IVR.*                            |                                  |
| **directory:**                   | \*411                            |
| -   *Directory of users.*        |                                  |
| **user_exists:**                 |                                  |
| -   *Determines if a user exists |                                  |
|     on the switch.*              |                                  |
| **caller-details:**              |                                  |
| -   *Logic to decifer caller     |                                  |
|     details.*                    |                                  |
| **call-direction:**              |                                  |
| -   *Determines the direction of |                                  |
|     the call.*                   |                                  |
| **variables:**                   |                                  |
| -   *Set variables on a domain   |                                  |
|     level.*                      |                                  |
| **is_local:**                    |                                  |
| -   *Can be used to evaluate     |                                  |
|     calls as local.*             |                                  |
| **call_block:**                  |                                  |
| -   *Block calls from reaching   |                                  |
|     endpoints.*                  |                                  |
| **user_record:**                 |                                  |
| -   *Used to record calls.*      |                                  |
| **redial:**                      | \*870                            |
| -   *Dial the last number that   |                                  |
|     was dialed.*                 |                                  |
| **default_caller_id:**           |                                  |
| -   *Caller ID that can be set   |                                  |
|     per domain.*                 |                                  |
| **agent_status_id:**             | \*23                             |
| -   *Status of the agent.*       |                                  |
| **provision:**                   | *11,*12                          |
| -   *Used with devices.*         |                                  |
| **clear_sip_auto_answer:**       |                                  |
| -                                |                                  |
| **nway_conference**              | nway                             |
| -                                |                                  |
| **cidlookup:**                   |                                  |
| -                                |                                  |
| **group-intercept:**             | \*8                              |
| -   *Intercepts a call from a    |                                  |
|     defined group.*              |                                  |
| **page:**                        | \*724                            |
| -   *Password protected paging   |                                  |
|     defined set of extensions.*  |                                  |
| **conf-xfer:**                   |                                  |
| -                                |                                  |
| **call_privacy:**                | \*67\[d+\]                       |
| -   *Send a privacy header to    |                                  |
|     the carrier to hide caller   |                                  |
|     id.*                         |                                  |
| **call_return:**                 | \*69                             |
| -   *Call the last number that   |                                  |
|     called the endpoint.*        |                                  |
| **extension_queue:**             | \*800\[ext\]                     |
| -                                |                                  |
| **intercept-ext:**               | \*\*\[ext\]                      |
| -   *Password protected          |                                  |
|     intercept of an extension.*  |                                  |
| **dx:**                          | dx                               |
| -   *Direct transfer.*           |                                  |
| **att_xfer:**                    | att[xfer]{#xfer}                 |
| -   *Attended transfer.*         |                                  |
| **extension-to-voicemail:**      | \[ext\]                          |
| -   *Used for extension to       |                                  |
|     voicemail.*                  |                                  |
| vmain                            | \*98                             |
| -   *Main menu to access any     |                                  |
|     voicemail using a pin        |                                  |
|     number.*                     |                                  |
| xfer[vm]{#vm}                    | xfer[vm]{#vm}                    |
| -   *Transfer to voicemail.*     |                                  |
| is[transfer]{#transfer}          | is[transfer]{#transfer}          |
| -   *Used for call transfering.* |                                  |
| [vmain_user]                     | \*97                             |
| (/en/latest/dialplan/dialplan_de |                                  |
| tails.html#voicemail-vmain-user) |                                  |
| -   *Endpoint\'s voicemail using |                                  |
|     a pin number.*               |                                  |
| delay[echo]{#echo}               | \*9195                           |
| -   *Play back an echo with a 5  |                                  |
|     second delay.*               |                                  |
| please[hold]{#hold}              |                                  |
| -   *Plays an audio file when on |                                  |
|     hold.*                       |                                  |
| is[zrtp_secure]{#zrtp_secure}    |                                  |
| -                                |                                  |
| is[secure]{#secure}              | is[secure]{#secure}              |
| -                                |                                  |
| tone[stream]{#stream}            | \*9198                           |
| -   *tones that stream and sound |                                  |
|     like Tetris music.*          |                                  |
| hold[music]{#music}              | \*9664                           |
| -   *Play music on hold. Good    |                                  |
|     for testing on an endpoint.* |                                  |
| fre                              | \*9888                           |
| eswitch[conference]{#conference} |                                  |
| -   *An easy way to join the     |                                  |
|     Cluecon Weekly call.*        |                                  |
| disa                             | \*3472                           |
| -   *Call in to a phone number   |                                  |
|     and provide a pin to dial    |                                  |
|     out.*                        |                                  |
| wake-up                          | \*925                            |
| -   *Schedule date and time for  |                                  |
|     an automated call.*          |                                  |
| extension[queue]{#queue}         |                                  |
| -                                |                                  |
| valet[park]{#park}               | park+\*5901-\*5999               |
| -   *Default range to valet park |                                  |
|     calls.*                      |                                  |
| valet[park_in]{#park_in}         | park+\*5900                      |
| -   *Default number to send      |                                  |
|     valet calls to.*             |                                  |
| valet[park_out]{#park_out}       | park+\*5901-\*5999               |
| -   *Default range to retreive   |                                  |
|     valet parked calls.*         |                                  |
| [operator]                       | 0                                |
| (dialplan_details.html#operator) |                                  |
| -   *Configurable option for an  |                                  |
|     operator.*                   |                                  |
| [operator-forward](dialpla       | \*000                            |
| n_details.html#operator-forward) |                                  |
| -   *Uses dial_string.lua.*      |                                  |
| [do-not-disturb](dialp           | *77,*78,\*79                     |
| lan_details.html#do-not-disturb) |                                  |
| -   *Turn on, toggle, turn off   |                                  |
|     do not disturb.*             |                                  |
| [call-forward](dia               | *72,*73,\*74                     |
| lplan_details.html#call-forward) |                                  |
| -   *Turn on, toggle on/off and  |                                  |
|     turn off call forwarding.*   |                                  |
| [follow-me](                     | \*21                             |
| dialplan_details.html#follow-me) |                                  |
| -   *Forwards call to defined    |                                  |
|     list of phone numbers or     |                                  |
|     extensions.*                 |                                  |
| [bind_digit_action](dialplan     |                                  |
| _details.html#bind-digit-action) |                                  |
| -                                |                                  |
| [call_screen](di                 | \[ext\]                          |
| alplan_details.html#call-screen) |                                  |
| \* *Play an audio file and give  |                                  |
| options to the caller to record  |                                  |
| a* *short message for the call   |                                  |
| recipient. Call recipient can    |                                  |
| then* *accept or reject the      |                                  |
| call.*                           |                                  |
| [local_extension](dialpl         | \[ext\]                          |
| an_details.html#local-extension) |                                  |
| -   *Examines to see if the      |                                  |
|     extension is local.*         |                                  |
| [voicemail](                     | \[ext\]                          |
| dialplan_details.html#voicemail) |                                  |
| -   *Voicemail for extensions.*  |                                  |
