# Dialplan Application

Dialplan Application uses FreeSWITCH **show application** to build the dropdown lists that are found in FusionPBX dialplans.
This is a list from a default install and the list can change depending on how many FreeSWITCH modules are installed.

| name | description | syntax | ikey |
|------|-------------|--------|------|
| answer | Answer the call | | mod_dptools |
| att_xfer | Attended Transfer | <channel_url> | mod_dptools |
| bgsystem | Execute a system command in the background | <command> | mod_dptools |
| bind_digit_action | bind a key sequence or regex to an action | <realm>,<digits\|~regex>,<string>[,<value>][,<dtmf target leg>][,<event target leg>] | mod_dptools |
| bind_meta_app | Bind a key to an application | <key> [a\|b\|ab] [a\|b\|o\|s\|i\|1] <app> | mod_dptools |
| block_dtmf | Block DTMF | | mod_dptools |
| break | Break | | mod_dptools |
| bridge | Bridge Audio | <channel_url> | mod_dptools |
| bridge_export | Export a channel variable across a bridge | <varname>=<value> | mod_dptools |
| callcenter | CallCenter | queue_name | mod_callcenter |
| capture | capture data into a var | <varname>\|<data>\|<regex> | mod_dptools |
| check_acl | Check an ip against an ACL list | <ip> <acl \| cidr> [<hangup_cause>] | mod_dptools |
| clear_digit_action | clear all digit bindings | <realm>\|all[,target] | mod_dptools |
| clear_speech_cache | Clear Speech Handle Cache | | mod_dptools |
| cng_plc | Do PLC on CNG frames | | mod_dptools |
| conference | conference | | mod_conference |
| respond | Send session respond | <respond_data> | mod_dptools |
| ring_ready | Indicate Ring_Ready | | mod_dptools |
| rxfax | FAX Receive Application | <filename> | mod_spandsp |
| say | say | <module_name>[:<lang>] <say_type> <say_method> [<say_gender>] <text> | mod_dptools |
| sched_broadcast | Schedule a broadcast in the future | [+]<time> <path> [aleg\|bleg\|both] | mod_dptools |
| sched_cancel | cancel scheduled tasks | [group] | mod_dptools |
| sched_hangup | Schedule a hangup in the future | [+]<time> [<cause>] | mod_dptools |
| sched_heartbeat | Enable Scheduled Heartbeat | [0\|<seconds>] | mod_dptools |
| sched_transfer | Schedule a transfer in the future | [+]<time> <extension> <dialplan> <context> | mod_dptools |
| send | send the message as-is | | mod_sms |
| send_display | Send session a new display | <text> | mod_dptools |
| send_dtmf | Send dtmf to be sent | <dtmf_data> | mod_dptools |
| send_info | Send info | <info> | mod_dptools |
| session_loglevel | session_loglevel | <level> | mod_dptools |
| set | set a variable | | mod_sms |
| set | Set a channel variable | <varname>=<value> | mod_dptools |
| set_audio_level | set volume | | mod_dptools |
| set_global | Set a global variable | <varname>=<value> | mod_dptools |
| set_media_stats | Set Media Stats | | mod_dptools |
| set_mute | set mute | | mod_dptools |
| set_name | Name the channel | <n> | mod_dptools |
| set_profile_var | Set a caller profile variable | <varname>=<value> | mod_dptools |
| set_user | Set a User | <user>@<domain> [prefix] | mod_dptools |
| set_zombie_exec | Enable Zombie Execution | | mod_dptools |
| sleep | Pause a channel | <pausemilliseconds> | mod_dptools |
| socket | Connect to a socket | <ip>[:<port>] | mod_event_socket |
| sofia_sla | private sofia sla function | <uuid> | mod_sofia |
| soft_hold | Put a bridged channel on hold | <unhold key> [<moh_a>] [<moh_b>] | mod_dptools |
| sound_test | Analyze Audio | | mod_dptools |
| spandsp_detect_tdd | Detect TDD data | | mod_spandsp |
| spandsp_inject_tdd | Send TDD data | | mod_spandsp |
| spandsp_send_tdd | Send TDD data | | mod_spandsp |
| spandsp_start_dtmf | Detect dtmf | | mod_spandsp |
| spandsp_start_fax_detect | start fax detect | <app>[ <arg>][ <timeout>][ <tone_type>] | mod_spandsp |
| spandsp_start_tone_detect | Start background tone detection with cadence | <n> | mod_spandsp |
| spandsp_stop_detect_tdd | stop sending tdd | | mod_spandsp |
| spandsp_stop_dtmf | stop inband dtmf | | mod_spandsp |
| spandsp_stop_fax_detect | stop fax detect | | mod_spandsp |
| spandsp_stop_inject_tdd | stop sending tdd | | mod_spandsp |
| spandsp_stop_tone_detect | Stop background tone detection with cadence | | mod_spandsp |
| speak | Speak text | <engine>\|<voice>\|<text> | mod_dptools |
| start_dtmf | Detect dtmf | | mod_dptools |
| start_dtmf_generate | Generate dtmf | | mod_dptools |
| stop | stop execution | | mod_sms |
| stop | Do Nothing | | mod_dptools |
| stop_displace_session | Stop Displace File | <path> | mod_dptools |
| stop_dtmf | stop inband dtmf | | mod_dptools |
| stop_dtmf_generate | stop inband dtmf generation | [write] | mod_dptools |
| stop_record_session | Stop Record Session | <path> | mod_dptools |
| stop_tone_detect | stop detecting tones | | mod_dptools |
| stop_video_write_overlay | Stop video write overlay | <path> | mod_dptools |
| stopfax | Stop FAX Application | | mod_spandsp |
| strftime | strftime | [<epoch>\|]<format string> | mod_dptools |
| system | execute a system command | | mod_sms |
| system | Execute a system command | <command> | mod_dptools |
| t38_gateway | Convert to T38 Gateway if tones are heard | | mod_spandsp |
| three_way | three way call with a uuid | <uuid> | mod_dptools |
| tone_detect | Detect tones | | mod_dptools |
| transfer | Transfer a channel | <exten> [<dialplan> <context>] | mod_dptools |
| transfer_vars | Transfer variables | <~variable_prefix\|variable> | mod_dptools |
| txfax | FAX Transmit Application | <filename> | mod_spandsp |
| unbind_meta_app | Unbind a key from an application | [<key>] | mod_dptools |
| unblock_dtmf | Stop blocking DTMF | | mod_dptools |
| unhold | Send a un-hold message | | mod_dptools |
| unloop | Tell loopback to unfold | | mod_loopback |
| unset | unset a variable | | mod_sms |
| unset | Unset a channel variable | <varname> | mod_dptools |
| unshift | Set a channel variable | <varname>=<value> | mod_dptools |
| valet_park | valet_park | <lotname> <extension>\|[ask [<min>] [<max>] [<to>] [<prompt>]\|auto [in\|out] [min] [max]] | mod_valet_parking |
| verbose_events | Make ALL Events verbose. | | mod_dptools |
| video_decode | Set video decode. | [[on\|wait]\|off] | mod_dptools |
| video_refresh | Send video refresh. | [manual\|auto] | mod_dptools |
| video_write_overlay | Video write overlay | <path> [<pos>] [<alpha>] | mod_dptools |
| wait_for_answer | Wait for call to be answered | | mod_dptools |
| wait_for_silence | wait_for_silence | <silence_thresh> <silence_hits> <listen_hits> <timeout_ms> [<file>] | mod_dptools |
