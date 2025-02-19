# Call Routing

Directs incoming calls for the extension

![image](../_static/images/fusionpbx_call_routing1.jpg)

-   To access call routing goto Accounts \> click the edit pencil icon
    on the right of the extension

![image](../_static/images/fusionpbx_call_routing.jpg)

-   Click **CALL ROUTING** on the top right

## Call Forward and Do No Disturb

This will allow phones to sync CFWD and DND over SIP.

A few things need to be configured to enable this feature and restart
freeswitch:

Uncomment this line in lua.conf.xml.
```
    <hook event="PHONE_FEATURE_SUBSCRIBE" subclass="" script="app.lua feature_event"/>
```

Add to Default Settings:
```
    Category = device
    Subcategory = feature_sync
    Type = boolean
    Value = true
```

### Enable Feature Sync on the Device

-   Yealink
    -   Web Interface -\> Features -\> General Information -\> Feature
        Key Synchronization set to Enabled
    -   Config Files -\>
        features.feature[key_sync.enable]{#key_sync.enable}
    -   Might be addition settings needed for the latest firmware. I
        tested with 81.0.110
    -   FusionPBX Default Settings -\> Provision -\>
        yealink[feature_key_sync]{#feature_key_sync}
-   Polycom
    -   reg.{\$row.line[number]{#number}}.serverFeatureControl.cf=\"1\"
    -   reg.{\$row.line[number]{#number}}.serverFeatureControl.dnd=\"1\"
    -   FusionPBX Default Settings -\> Provision -\>
        polycom[feature_key_sync]{#feature_key_sync}
-   Cisco SPA
    -   \<[Feature_Key_Sync_1]()
        group=\"Ext1/Call[Feature_Settings]{#feature_settings}\"\>Yes\</[Feature_Key_Sync_1]()\>
    -   FusionPBX Default Settings -\> Provision -\>
        spa[feature_key_sync]{#feature_key_sync}
-   Grandstream GXP and GRP
    -   Web Interface -\> Accounts -\> Account X -\> SIP Settings -\>
        Advanced Features -\> Feature Key Synchronization
    -   Config file P2325
    -   FusionPBX Default Settings -\> Provision -\>
        grandstream[feature_key_sync]{#feature_key_sync}
