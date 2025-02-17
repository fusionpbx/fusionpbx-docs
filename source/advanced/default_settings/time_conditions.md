# Time Conditions

Time Conditions specific default settings.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Default Setting Subcategory Default   Default Setting Value                                                                                     Default   Default Setting
                              Setting                                                                                                             Setting   Description
                              Name                                                                                                                Enabled   
  --------------------------- --------- --------------------------------------------------------------------------------------------------------- --------- -------------------
  region                      text      usa                                                                                                       TRUE      What region to use
                                                                                                                                                            by default when
                                                                                                                                                            choosing Time
                                                                                                                                                            Conditions

  preset[england]{#england}   array     {\"new[years_day]{#years_day}\":{\"mday\":\"1\",\"mon\":\"1\"}}                                           TRUE      England Holiday

  preset[england]{#england}   array     {\"may[day]{#day}\":{\"mon\":\"5\",\"mday\":\"1-7\",\"wday\":\"2\"}}                                      TRUE      England Holiday

  preset[england]{#england}   array     {\"august[bank_holiday]{#bank_holiday}\":{\"mon\":\"8\",\"mday\":\"25-31\",\"wday\":\"2\"}}               TRUE      England Holiday

  preset[england]{#england}   array     {\"christmas[day]{#day}\":{\"mday\":\"25\",\"mon\":\"12\"}}                                               TRUE      England Holiday

  preset[england]{#england}   array     {\"boxing[day]{#day}\":{\"mday\":\"26\",\"mon\":\"12\"}}                                                  TRUE      England Holiday

  preset[usa]{#usa}           array     {\"new[years_day]{#years_day}\":{\"mday\":\"1\",\"mon\":\"1\"}}                                           TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"presidents[day]{#day}\":{\"wday\":\"2\",\"mon\":\"2\",\"mday\":\"15-21\"}}                             TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"memorial[day]{#day}\":{\"mday\":\"25-31\",\"wday\":\"2\",\"mon\":\"5\"}}                               TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"independence[day]{#day}\":{\"mday\":\"4\",\"mon\":\"7\"}}                                              TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"labor[day]{#day}\":{\"wday\":\"2\",\"mon\":\"9\",\"mday\":\"1-7\"}}                                    TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"columbus[day]{#day}\":{\"wday\":\"2\",\"mon\":\"10\",\"mday\":\"8-14\"}}                               TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"veterans[day]{#day}\":{\"mday\":\"11\",\"mon\":\"11\"}}                                                TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"black[friday]{#friday}\":{\"wday\":\"6\",\"mon\":\"11\",\"mday\":\"23-29\"}}                           TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"christmas[day]{#day}\":{\"mday\":\"25\",\"mon\":\"12\"}}                                               TRUE      USA Holiday

  preset[canada]{#canada}     array     {\"new[years_day]{#years_day}\":{\"mday\":\"1\",\"mon\":\"1\"}}                                           TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"family[day]{#day}\":{\"wday\":\"2\",\"mon\":\"2\",\"mday\":\"8-14\"}}                                  TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"victoria[day]{#day}\":{\"wday\":\"2\",\"mon\":\"5\",\"mday\":\"18-24\"}}                               TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"canada[day]{#day}\":{\"mday\":\"1\",\"mon\":\"7\"}}                                                    TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"bc[day]{#day}\":{\"wday\":\"2\",\"mon\":\"8\",\"mday\":\"1-7\"}}                                       TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"remembrance[day]{#day}\":{\"mday\":\"11\",\"mon\":\"11\"}}                                             TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"christmas[day]{#day}\":{\"mday\":\"25\",\"mon\":\"12\"}}                                               TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"boxing[day]{#day}\":{\"mday\":\"26\",\"mon\":\"12\"}}                                                  TRUE      Canada Holiday

  preset[canada]{#canada}     array     {\"labour[day]{#day}\":{\"wday\":\"2\",\"mon\":\"9\",\"mday\":\"1-7\"}}                                   TRUE      Canada Holiday

  preset[england]{#england}   array     {\"spring[bank_holiday]{#bank_holiday}\":{\"mon\":\"5\",\"mday\":\"25-31\",\"wday\":\"2\"}}               TRUE      England Holiday

  preset[usa]{#usa}           array     {\"martin[luther_king_jr_day]{#luther_king_jr_day}\":{\"wday\":\"2\",\"mon\":\"1\",\"mday\":\"15-21\"}}   TRUE      USA Holiday

  preset[usa]{#usa}           array     {\"thanksgiving[day]{#day}\":{\"wday\":\"5\",\"mon\":\"11\",\"mday\":\"22-28\"}}                          TRUE      USA Holiday

  preset[canada]{#canada}     array     {\"thanksgiving[day]{#day}\":{\"wday\":\"2\",\"mon\":\"10\",\"mday\":\"8-14\"}}                           TRUE      Canada Holiday
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
