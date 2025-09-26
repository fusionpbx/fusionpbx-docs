# Voicemail

To edit voicemail settings, click the pencil edit icon on the right of the extension number.

![Voicemail Settings](../_static/images/applications/voicemail/fusionpbx_voicemails1.png)

Here you can edit voicemail settings:

- **Play Tutorial**: Play the voicemail tutorial after the next voicemail login
- **Greeting**: When you dial ***97**, record a greeting and set a number you can choose which greeting to use
- **Alternate Greet ID**: An alternative greet ID used in the default greeting
- **Options**: Define caller options for the voicemail greeting
- **Mail to**: Have voicemails emailed to this address
- **Voicemail File**: Select a listening option to include with the email notification
- **Keep Local**: Choose whether to keep the voicemail in the system after sending the email notification
- **Forward Destinations**: Forward voicemail messages to additional destinations
- **Enabled**: Enable or disable the voicemail box

![Voicemail Settings Continued](../_static/images/applications/voicemail/fusionpbx_voicemails3.png)

![Voicemail Settings Continued](../_static/images/applications/voicemail/fusionpbx_voicemails2.png)

:::{note}   
Starting version 4.2, remote access to voicemail by interrupting the greeting message   
by pressing "*" and entering the password is disabled by default.   
:::

To enable remote access to voicemail:

1. Go to your FusionPBX installation menu.
2. Navigate to **Advanced**.
3. Select **Default Settings**.
4. Go to the **Voicemail** category.
5. Enable and set `remote_access` to `true`.

## Voicemail Options

To access an extension’s voicemail **away** from the extension:

- Dial the extension and interrupt the greeting with the ***star** key.

| Key       | Description                                      |
|-----------|--------------------------------------------------|
| ***97**   | To access **that** extension’s voicemail **from the extension** or the voicemail button |
| ***98**   | To access **any** extension’s voicemail          |
| ***99[ext]** | To access **a specific** extension voicemail  |

### Main Menu

| Key       | Action                  |
|-----------|-------------------------|
| **press 5** | For advanced options  |

### Advanced Options

| Key       | Action                  |
|-----------|-------------------------|
| **press 1** | Record a greeting     |
| **press 2** | Choose a greeting     |
| **press 3** | Record name           |
| **press 6** | Change password       |
| **press 0** | For main menu         |

### Email Setup/Default Settings
Click the link for setting up email server settings: [Email Setup/Default Settings](http://docs.fusionpbx.com/en/latest/advanced/default_settings.html#email). These are the settings needed to enable your FusionPBX installation to send email notifications.

### Voicemail Variables
Using switch variables provides the ability to adjust FusionPBX Voicemail features. These variables can be set in either **Dialplan > Global Variables** or per domain with **Domain Variables Dialplan**.

#### Leave a Voicemail

| Name                      | Value          |
|---------------------------|----------------|
| skip_greeting             | true or false  |
| skip_instructions         | true or false  |
| voicemail_greeting_number | 0-9            |
| vm_disk_quota             | 0-3600 seconds |
| vm_message_ext            | wav or mp3     |

#### Check Voicemails

| Name                      | Value          |
|---------------------------|----------------|
| voicemail_authorized      | true or false  |
| vm_say_caller_id_number   | true or false  |
| vm_say_date_time          | true or false  |

:::{note}   
The 'wav' format is the default voicemail message file type. A value of 'mp3' requires *mod_shout* be installed and running.   
:::

### Not Found Message
When an extension is unavailable and no voicemail is configured, there is an option to play a message to the caller alerting them to this.

To enable/disable this, change the option for the **not_found_message** setting in **Advanced > Default Settings > Voicemail** category to suit your preference.

:::{warning}   
Enabling this option means that the call must be answered in order to play the message to the caller, and so the call will complete with a 200 OK rather than a 480 Unavailable or 486 Busy. In some jurisdictions, this could potentially be illegal as it turns an otherwise toll-free call into a chargeable one.   
:::

## Voicemail Transcription
FusionPBX supports Voicemail Transcription, where emails will include a transcribed version of the voicemail the email was sent in regards to. To configure this feature, see [Voicemail Transcription](http://docs.fusionpbx.com/en/latest/applications/voicemail_transcription.html).
