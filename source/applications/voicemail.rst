##########
Voicemail
##########


To edit voicemail settings click the pencil edit icon on the right of the extension number.

.. image:: ../_static/images/voicemail/fusionpbx_voicemail.jpg
        :scale: 85%


Here you can edit voicemail settings.

*  Play Tutorial- Play the voicemail tutorial after the next voicemail login
*  Greeting- When you dial ***97**, record a greeting and set a number you can choose which greeting to use
*  Alternate Greet ID- An alternative greet id used in the default greeting 
*  Options- Define caller options for the voicemail greeting
*  Mail to- have voicemails emailed to this address
*  Voicemail File- Select a listening option to include with the email notification
*  Keep Local- Choose whether to keep the voicemail in the system after sending the email notification
*  Forward Destinations- Forward voicemail messages to additional destinations
*  Enabled- Enable or disable the voicemail box

.. image:: ../_static/images/voicemail/fusionpbx_voicemail2.jpg
        :scale: 85%

.. note::

 Starting version 4.2 remote access to voicemail by interupting the greeting message by pressing "*" and entering the password is disabled by default.


Voicemail Options
====================


To access an extensions voicemail **away** from the extension.

*  Dial the extension and interupt the greeting with the ***star** key.

+-------------+-----------------------+------------------------------+-----------------------------------+
| ***97**     | To access **that** extensions voicemail **from the extension** or the voicemail button   |
+-------------+-----------------------+------------------------------+-----------------------------------+
| ***98**     | To access **any** extensions voicemail                                                   |
+-------------+-----------------------+------------------------------+-----------------------------------+
| ***99[ext]**| To access **a specific** extension voicemail                                             |
+-------------+-----------------------+------------------------------+-----------------------------------+


+-------------+-----------------------+
|             |   **Main Menu**       |
+-------------+-----------------------+
| **press 5** | For advanced options  |
+-------------+-----------------------+


+-------------+-----------------------+
|             | **Advanced Options**  |
+-------------+-----------------------+
| **press 1** | Record a greeting     |
+-------------+-----------------------+
| **press 2** | Choose a greeting     |
+-------------+-----------------------+
| **press 3** | Record name           |
+-------------+-----------------------+
| **press 6** | Change password       |
+-------------+-----------------------+
| **press 0** | For main menu         |
+-------------+-----------------------+



Voicemail Transcription
====================

|

Uses API services to transcribe voicemails into text to be used in the app-sms and the voicemail to email options.

The following services are supported. Others can be added but would need to be developed.

*  Microsoft Bing
Sign up and language information is located on `Microsoft Site <https://www.microsoft.com/cognitive-services/en-us/Speech-api/documentation/API-Reference-REST/BingVoiceRecognition>`_

.. warning:: We cannot use mod_shout to record Voicemails because the transcription service needs an uncompressed version of the audio. Therefore we will record in WAV and then use LAME to re-encode in MP3. This could cause added resource utilization to your system.

**Goto Advanced > Default Settings.**
Add the following entries

+-------------+-----------------------+-----------+---------------------------+-----------+
|  Category   |  Subcategory          |  Type     |  Value                    |  Enabled  |
+=============+=======================+===========+===========================+===========+
|  voicemail  |  transcribe_provider  |  text     |  microsoft                |  True     |
+-------------+-----------------------+-----------+---------------------------+-----------+
|  voicemail  |  microsoft_key1       |  text     |  {your microsoft key #1}  |  True     |
+-------------+-----------------------+-----------+---------------------------+-----------+
|  voicemail  |  microsoft_key2       |  text     |  {your microsoft key #2}  |  True     |
+-------------+-----------------------+-----------+---------------------------+-----------+
|  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |
+-------------+-----------------------+-----------+---------------------------+-----------+
|  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |
+-------------+-----------------------+-----------+---------------------------+-----------+
 
 Click "Reload" at the top of the page.
 
**Goto Status > Sip Status.**

Click "Flush Memcache", "Reload XML" and "Rescan".
 
If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.

**Variables**

These variables can be set in advanced -> variables or in the dialplan.

+---------------------------+----------------+
| Name                      | Value          |
+---------------------------+----------------+
| vm_say_date_time          | true or false  |
+---------------------------+----------------+
| skip_greeting             | true or false  |
+---------------------------+----------------+
| skip_instructions         | true or false  |
+---------------------------+----------------+
| voicemail_greeting_number | 0-9            |
+---------------------------+----------------+
| vm_disk_quota             | 0-3600 seconds |
+---------------------------+----------------+
| vm_message_ext            | wav or mp3     | 
+---------------------------+----------------+
| voicemail_authorized      | true or false  | 
+---------------------------+----------------+
| vm_say_caller_id_number   | true or false  | 
+---------------------------+----------------+
| vm_say_date_time          | true or false  | 
+---------------------------+----------------+

Wav file is the default voicemail message file type.
MP3 requires mod_shout to be installed and running.

**Not Found Message**

When an extension is unavailable and no voicemail is configured, there is an option to play a message to the caller alerting them to this.

To enable/disable this, change the option for the **not_found_message** setting in **Advanced > Default Settings > Voicemail** category to suit your preference.

Please note that enabling this option means that the call must be answered in order to play the message to the caller and so the call will complete with a 200 OK rather than a 480 Unavailable or 486 Busy. In some jurisdictions this could potentially be illegal as it turns an otherwise toll free call into a chargeable one.
