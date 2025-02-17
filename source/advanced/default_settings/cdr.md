# CDR

CDR Stat hour limit, call leg, format, limit, http[enabled]{#enabled},
archive database, and storage type settings can be set here.

  ---------------------------------------------------------------------------------------------------------
  Default Setting Subcategory                      Default     Default      Default      Default Setting
                                                   Setting     Setting      Setting      Description
                                                   Name        Value        Enabled      
  ------------------------------------------------ ----------- ------------ ------------ ------------------
  stat[hours_limit]{#hours_limit}                  numeric     24           FALSE        

  b[leg]{#leg}                                     array       outbound     FALSE        

  b[leg]{#leg}                                     array       inbound      FALSE        

  b[leg]{#leg}                                     array       local        FALSE        

  format                                           text        json         TRUE         

  limit                                            numeric     800          TRUE         

  http[enabled]{#enabled}                          boolean     TRUE         TRUE         

  archive[database_driver]{#database_driver}       text        pgsql        FALSE        Archive Database
                                                                                         Driver

  archive[database_host]{#database_host}           text                     FALSE        IP/Hostname of
                                                                                         Archive Database

  archive[database_password]{#database_password}   text                     FALSE        Archive Database
                                                                                         Password

  archive[database_port]{#database_port}           text        5432         FALSE        Archive Database
                                                                                         Port

  archive[database_username]{#database_username}   text                     FALSE        Archive Database
                                                                                         Username

  storage                                          text        db           TRUE         

  archive[database]{#database}                     boolean     FALSE        FALSE        Enable Dedicated
                                                                                         CDR Database
                                                                                         Access

  archive[database_name]{#database_name}           text        fusionpbx    FALSE        Archive Database
                                                                                         Name
  ---------------------------------------------------------------------------------------------------------
