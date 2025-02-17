# User

User specific default settings.

  ----------------------------------------------------------------------------------------------
  Default Setting Subcategory       Default   Default   Default    Default Setting Description
                                    Setting   Setting   Setting    
                                    Name      Value     Enabled    
  --------------------------------- --------- --------- ---------- -----------------------------
  password[special]{#special}       boolean   FALSE     TRUE       Set whether to require at
                                                                   least one special character
                                                                   in user passwords.

  unique                            text      global    FALSE      Make all user names unique on
                                                                   all domains.

  password[length]{#length}         numeric   10        TRUE       The default length of
                                                                   characters in a user
                                                                   password.

  password[number]{#number}         boolean   TRUE      TRUE       Set whether to require at
                                                                   least one number in user
                                                                   passwords.

  password[lowercase]{#lowercase}   boolean   TRUE      TRUE       Set whether to require at
                                                                   least one lowecase letter in
                                                                   user passwords.

  password[uppercase]{#uppercase}   boolean   TRUE      TRUE       Set whether to require at
                                                                   least one uppercase letter in
                                                                   user passwords.
  ----------------------------------------------------------------------------------------------
