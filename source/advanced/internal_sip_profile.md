# Internal SIP Profile

-   Advanced \> SIP Profiles \> Internal SIP Profile

![FusionPBX Internal SIP Profile](../_static/images/fusionpbx_internal_sip_profile.jpg)

- **Hostname**: Should be left blank and is for advanced use.

| Name                                | Value                                      | Enabled | Description                                                  |
|-------------------------------------|--------------------------------------------|---------|--------------------------------------------------------------|
| accept-blind-auth                   | true                                       | False   |                                                              |
| accept-blind-reg                    | true                                       | False   |                                                              |
| aggressive-nat-detection            | true                                       | True    |                                                              |
| alias                               | sip:10.0.1.251:5555                        | False   |                                                              |
| apply-inbound-acl                   | domains                                    | True    |                                                              |
| apply-nat-acl                       | nat.auto                                   | True    |                                                              |
| apply-register-acl                  | domains                                    | False   |                                                              |
| auth-all-packets                    | false                                      | True    |                                                              |
| auth-calls                          | $${internal_auth_calls}                    | True    |                                                              |
| auto-jitterbuffer-msec              | 60                                         | False   |                                                              |
| auto-rtp-bugs                       |                                            | False   |                                                              |
| bind-params                         | transport=udp                              | False   |                                                              |
| bitpacking                          | aal2                                       | False   |                                                              |
| caller-id-type                      | rpid                                       | False   |                                                              |
| caller-id-type                      | pid                                        | False   |                                                              |
| caller-id-type                      | none                                       | False   |                                                              |
| challenge-realm                     | auto_to                                    | True    |                                                              |
| cid-in-1xx                          | false                                      | False   |                                                              |
| context                             | public                                     | True    |                                                              |
| dbname                              | share_presence                             | False   |                                                              |
| debug                               | 0                                          | True    |                                                              |
| delete-subs-on-register             | false                                      | False   |                                                              |
| dialplan                            | XML                                        | True    |                                                              |
| disable-naptr                       | false                                      | False   |                                                              |
| disable-register                    | true                                       | False   |                                                              |
| disable-rtp-auto-adjust             | true                                       | False   |                                                              |
| disable-srv                         | false                                      | False   |                                                              |
| disable-srv503                      | true                                       | False   |                                                              |
| disable-transcoding                 | true                                       | False   |                                                              |
| disable-transfer                    | true                                       | False   |                                                              |
| dtmf-duration                       | 2000                                       | True    |                                                              |
| dtmf-type                           | rfc2833                                    | True    |                                                              |
| enable-100rel                       | true                                       | False   |                                                              |
| enable-3pcc                         | true                                       | False   |                                                              |
| enable-compact-headers              | true                                       | False   |                                                              |
| enable-timer                        | false                                      | False   |                                                              |
| extended-info-parsing               | true                                       | False   |                                                              |
| ext-rtp-ip                          | $${external_rtp_ip}                        | True    |                                                              |
| ext-sip-ip                          | $${external_rtp_ip}                        | True    |                                                              |
| force-register-db-domain            | $${domain}                                 | False   |                                                              |
| force-register-domain               | $${domain}                                 | False   |                                                              |
| force-subscription-domain           | $${domain}                                 | False   |                                                              |
| force-subscription-expires          | 60                                         | False   |                                                              |
| forward-unsolicited-mwi-notify      | false                                      | True    |                                                              |
| hold-music                          | $${hold_music}                             | True    |                                                              |
| inbound-bypass-media                | true                                       | False   |                                                              |
| inbound-codec-negotiation           | generous                                   | True    |                                                              |
| inbound-codec-prefs                 | $${global_codec_prefs}                     | True    |                                                              |
| inbound-late-negotiation            | true                                       | False   |                                                              |
| inbound-proxy-media                 | true                                       | False   |                                                              |
| inbound-reg-force-matching-username | true                                       | True    |                                                              |
| liberal-dtmf                        | true                                       | False   |                                                              |
| local-network-acl                   | localnet.auto                              | True    |                                                              |
| log-auth-failures                   | true                                       | True    |                                                              |
| manage-presence                     | true                                       | True    |                                                              |
| manage-shared-appearance            | true                                       | True    |                                                              |
| manual-redirect                     | true                                       | False   |                                                              |
| max-proceeding                      | 1000                                       | False   |                                                              |
| media-option                        | bypass-media-after-att-xfer                | False   |                                                              |
| media-option                        | resume-media-on-hold                       | False   |                                                              |
| minimum-session-expires             | 120                                        | False   |                                                              |
| multiple-registrations              | contact                                    | False   | Enables registrations on multiple endpoints                  |
| nat-options-ping                    | true                                       | False   |                                                              |
| NDLB-broken-auth-hash               | true                                       | False   |                                                              |
| NDLB-force-rport                    | safe                                       | True    | Enables rport                                                |
| NDLB-received-in-nat-reg-contact    | true                                       | False   |                                                              |
| nonce-ttl                           | 60                                         | True    |                                                              |
| odbc-dsn                            | $${dsn}                                    | False   |                                                              |
| outbound-codec-prefs                | $${global_codec_prefs}                     | True    |                                                              |
| pass-callee-id                      | false                                      | False   |                                                              |
| pass-rfc2833                        | true                                       | False   |                                                              |
| presence-hosts                      | $${domain},$${local_ip_v4}                 | False   |                                                              |
| presence-privacy                    | $${presence_privacy}                       | True    |                                                              |
| presence-probe-on-register          | true                                       | True    |                                                              |
| presence-proto-lookup               | true                                       | False   |                                                              |
| record-path                         | $${recordings_dir}                         | True    |                                                              |
| record-template  | \${domain_name}/<br>archive/<br>\${strftime(%Y)}/<br>\${strftime(%b)}/<br>\${strftime(%d)}/<br>\${uuid}.\${record_ext} | True    |       |
| registration-thread-frequency       | 30                                         | False   |                                                              |
| renegotiate-codec-on-hold           | true                                       | False   |                                                              |
| rfc2833-pt                          | 101                                        | True    |                                                              |
| rtcp-audio-interval-msec            | 5000                                       | False   |                                                              |
| rtcp-video-interval-msec            | 5000                                       | False   |                                                              |
| rtp-autofix-timing                  | false                                      | False   |                                                              |
| rtp-autoflush-during-bridge         | false                                      | False   |                                                              |
| rtp-hold-timeout-sec                | 1800                                       | True    |                                                              |
| rtp-ip                              | $${local_ip_v4}                            | True    |                                                              |
| rtp-rewrite-timestamps              | true                                       | False   |                                                              |
| rtp-timeout-sec                     | 300                                        | True    |                                                              |
| rtp-timer-name                      | soft                                       | True    |                                                              |
| send-message-query-on-register      | True                                       | False   |                                                              |
| send-presence-on-register           | true                                       | False   |                                                              |
| session-timeout                     | 1800                                       | False   |                                                              |
| shutdown-on-fail                    | true                                       | False   |                                                              |
| sip-capture                         | no                                         | True    |                                                              |
| sip-ip                              | $${local_ip_v4}                            | True    |                                                              |
| sip-port                            | $${internal_sip_port}                      | True    |                                                              |
| sip-trace                           | no                                         | True    |                                                              |
| suppress-cng                        | true                                       | False   |                                                              |
| timer-T1                            | 500                                        | False   |                                                              |
| timer-T1X64                         | 32000                                      | False   |                                                              |
| timer-T2                            | 4000                                       | False   |                                                              |
| timer-T4                            | 4000                                       | False   |                                                              |
| tls                                 | $${internal_ssl_enable}                    | True    |                                                              |
| tls-bind-params                     | transport=tls                              | True    |                                                              |
| tls-cert-dir                        | $${internal_ssl_dir}                       | True    |                                                              |
| tls-only                            | false                                      | True    |                                                              |
| tls-passphrase                      |                                            | True    |                                                              |
| tls-sip-port                        | $${internal_tls_port}                      | True    |                                                              |
| tls-verify-date                     | true                                       | True    |                                                              |
| tls-verify-depth                    | 2                                          | True    |                                                              |
| tls-verify-in-subjects              |                                            | True    |                                                              |
| tls-verify-policy                   | all\|subjects_all                          | False   |                                                              |
| tls-version                         | $${sip_tls_version}                        | True    |                                                              |
| unregister-on-options-fail          | true                                       | False   |                                                              |
| user-agent-string                   | FreeSWITCH                                 | True    |                                                              |
| vad                                 | out                                        | False   |                                                              |
| watchdog-enabled                    | no                                         | True    |                                                              |
| watchdog-event-timeout              | 30000                                      | True    |                                                              |
| watchdog-step-timeout               | 3000                                       | True    |                                                              |
