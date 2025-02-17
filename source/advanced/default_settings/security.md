# Security

Security specific default settings.

  -----------------------------------------------------------------------------------------------------------
  Default Setting Subcategory       Default   Default   Default   Default Setting Description
                                    Setting   Setting   Setting   
                                    Name      Value     Enabled   
  --------------------------------- --------- --------- --------- -------------------------------------------
  password[length]{#length}         numeric   15        TRUE      Set the required length for the generated
                                                                  passwords.

  password[number]{#number}         boolean   TRUE      FALSE     Set whether to require at least one number
                                                                  in passwords.

  password[uppercase]{#uppercase}   boolean   TRUE      FALSE     Set whether to require at least one
                                                                  uppercase letter in passwords.

  password[special]{#special}       boolean   TRUE      FALSE     Set whether to require at least one special
                                                                  character in passwords.

  session[rotate]{#rotate}          boolean   TRUE      TRUE      Whether to regenerate the session ID.

  password[lowercase]{#lowercase}   boolean   TRUE      TRUE      Set whether to require at least one
                                                                  lowecase letter in passwords.

  password[strength]{#strength}     numeric   4         TRUE      Set the default strength for generated
                                                                  passwords. Valid Options: 1 - Numeric Only,
                                                                  2 - Include Lower Apha, 3 - Include Upper
                                                                  Alpha, 4 - Include Special Characters.
  -----------------------------------------------------------------------------------------------------------
