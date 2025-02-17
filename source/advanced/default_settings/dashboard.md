# Dashboard

User level settings that control what is seen and not seen on the
dashboard for each user access level.

  -------------------------------------------------------------------------------------------------------
  Default       Default   Default Setting Value                 Default   Default Setting Description
  Setting       Setting                                         Setting   
  Subcategory   Name                                            Enabled   
  ------------- --------- ------------------------------------- --------- -------------------------------
  admin         array     voicemail                             TRUE      Enable Dashboard Voicemail
                                                                          block for users in the admin
                                                                          group.

  admin         array     missed                                TRUE      Enable Dashboard Missed Calls
                                                                          block for users in the admin
                                                                          group.

  admin         array     recent                                TRUE      Enable Dashboard Recent Calls
                                                                          block for users in the admin
                                                                          group.

  admin         array     limits                                FALSE     Enable Dashboard Domain Limits
                                                                          block for users in the admin
                                                                          group.

  admin         array     counts                                TRUE      Enable Dashboard Domain Counts
                                                                          block for users in the admin
                                                                          group.

  admin         array     ring[groups]{#groups}                 TRUE      Enable Dashboard Ring Group
                                                                          Forwarding controls for users
                                                                          in the admin group.

  admin         array     caller[id]{#id}                       FALSE     Enable changing Caller ID name
                                                                          and number.

  superadmin    array     voicemail                             TRUE      Enable Dashboard Voicemail
                                                                          block for users in the
                                                                          superadmin group.

  superadmin    array     missed                                TRUE      Enable Dashboard Missed Calls
                                                                          block for users in the
                                                                          superadmin group.

  superadmin    array     recent                                TRUE      Enable Dashboard Recent Calls
                                                                          block for users in the
                                                                          superadmin group.

  superadmin    array     limits                                FALSE     Enable Dashboard Domain Limits
                                                                          block for users in the
                                                                          superadmin group.

  superadmin    array     counts                                TRUE      Enable Dashboard System Counts
                                                                          block for users in the
                                                                          superadmin group.

  superadmin    array     call[routing]{#routing}               TRUE      Enable Dashboard Call Routing
                                                                          controls for users in the
                                                                          superadmin group.

  superadmin    array     caller[id]{#id}                       FALSE     Enable changing Caller ID name
                                                                          and number.

  superadmin    array     ring[groups]{#groups}                 TRUE      Enable Dashboard Ring Group
                                                                          Forwarding controls for users
                                                                          in the superadmin group.

  user          array     voicemail                             TRUE      Enable Dashboard Voicemail
                                                                          block for users in the users
                                                                          group.

  user          array     missed                                TRUE      Enable Dashboard Missed Calls
                                                                          block for users in the users
                                                                          group.

  user          array     recent                                TRUE      Enable Dashboard Recent Calls
                                                                          block for users in the users
                                                                          group.

  user          array     call[routing]{#routing}               TRUE      Enable Dashboard Call Routing
                                                                          controls for users in the users
                                                                          group.

  user          array     ring[groups]{#groups}                 TRUE      Enable Dashboard Ring Group
                                                                          Forwarding controls for users
                                                                          in the users group.

  user          array     caller[id]{#id}                       FALSE     Enable changing Caller ID name
                                                                          and number.

  admin         array     call[routing]{#routing}               TRUE      Enable Dashboard Call Routing
                                                                          controls for users in the admin
                                                                          group.

  superadmin    array     system                                TRUE      Enable Dashboard System Status
                                                                          block for users in the
                                                                          superadmin group.

  agent         array     call[center_agents]{#center_agents}   TRUE      Enable Dashboard Call Center
                                                                          Agent Status block for users in
                                                                          the agent group.
  -------------------------------------------------------------------------------------------------------
