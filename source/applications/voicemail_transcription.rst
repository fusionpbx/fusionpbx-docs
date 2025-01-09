*****************
Voicemail Transcription in FusionPBX 5.3
*****************

- Log in to FusionPBX

  - Access the FusionPBX administrative interface.

- Check for the "Transcribe" Option

  - Navigate to Advanced > Default Settings.

  - Use the drop-down filter to select "Transcribe".

  - If the "Transcribe" option exists, skip to step 5. Otherwise, continue to step 3.

- Install the Transcribe and Speech Apps

  - SSH into your server and run the following commands::

    cd /var/www/fusionpbx/app

    git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe

    git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech

    chown -R www-data:www-data /var/www/fusionpbx

    php /var/www/fusionpbx/core/upgrade/upgrade.php

- Reload the FusionPBX Interface

  - Navigate back to Advanced > Default Settings.

  - The "Transcribe" section should now be available.

- Configure Transcription Settings

  - In the **"Transcribe"**category, find and enable the following settings:

    - api_key: Enter your API key for the transcription service.

    - enabled: Set to True.

    - engine: Type your transcription provider (e.g., openai, google, azure, etc.).

    - api_url: Leave this blank

  - Click Reload to apply the changes.

- Enable Transcription for one Extension

  - Navigate to Accounts > Extensions.

  - Select the desired extension.

  - Set Transcription Enabled to True.

- Enable Transcription by Default for Everyone.

  - Navigate to Advanced > Default Settings.

  - Use the drop-down filter to select "Voicemail".

  - Find and enable the setting transcription_enabled_default.

- Test the Service

  - Leave a voicemail for that extension to verify the transcription works correctly.



*****************
Voicemail Transcription in FusionPBX 5.2 and older
*****************

|

Uses API services to transcribe voicemails into text to be used in the app-sms and the voicemail to email options. Bing's Speech API or other generic APIs can be used.


IBM Watson API
====================


Sign up and language information is located on `IBM Watson's Site <https://cloud.ibm.com/catalog/services/speech-to-text>`_ 

.. warning:: We cannot use mod_shout to record Voicemails because the transcription service needs an uncompressed version of the audio. Therefore we will record in WAV and then use LAME to re-encode in MP3. This could cause added resource utilization to your system.

**Goto Advanced > Default Settings.**
Add the following entries

  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  Category   |  Subcategory          |  Type     |  Value                    |  Enabled  |
  +=============+=======================+===========+===========================+===========+
  |  voicemail  |  transcribe_provider  |  text     |  watson                   |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  watson_key           |  text     |  { your watson key }      |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  watson_url           |  text     |  { watson url }          |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  json_enabled         |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+

*NOTE: Watson URL used for testing was the following:
https://example.url.api.us-south.speech-to-text.watson.cloud.ibm.com/instances/{GUID}/v1/recognize?model=en-US_Telephony&smart_formatting=true*

**List of available IBM Watson speech to text models**
https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models

 Click "Reload" at the top of the page.

**Goto Status > Sip Status.**

Click "Flush Cache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.


Azure API
====================

**Goto Advanced > Default Settings.**
Add the following entries

  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  Category   |  Subcategory          |  Type     |  Value                    |  Enabled  |
  +=============+=======================+===========+===========================+===========+
  |  voicemail  |  transcribe_provider  |  text     |  azure                    |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  azure_key            |  text     |  { your azure key }       |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  azure_server_region  |  text     |  { your server region }   |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  json_enabled         |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+

 Click "Reload" at the top of the page.

**Goto Status > Sip Status.**

Click "Flush Cache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.


Google API
====================

**Goto Advanced > Default Settings.**
Add the following entries

  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  Category   |  Subcategory          |  Type     |  Value                    |  Enabled  |
  +=============+=======================+===========+===========================+===========+
  |  voicemail  |  transcribe_provider  |  text     |  google                   |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  google_key           |  text     |  { your google key }      |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  google_url           |  text     |  { your google url }      |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  json_enabled         |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+

 Click "Reload" at the top of the page.

**Goto Status > Sip Status.**

Click "Flush Cache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.



Bing API
====================

Recommend using Azure as an alternative to Bing.

Sign up and language information is located on `Microsoft Site <https://www.microsoft.com/cognitive-services/en-us/Speech-api/documentation/API-Reference-REST/BingVoiceRecognition>`_ Note: The Bing Speech API is deprecated as of October 2018, this works for now but needs to be ported to `the new API <https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Speech-Service/how-to-migrate-from-bing-speech.md>`_

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

Click "Flush Cache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.


Custom API
====================

Currently does not work with the FusionPBX email_queue.

API info from the Speech to Text provider of your choice is needed, or you can self host a transcription engine like `Mozilla DeepSpeech <https://git.callpipe.com/fusionpbx/deepspeech_frontend>`_ or `Kaldi ASR <https://github.com/dialogflow/asr-server>`_

**Goto Advanced > Default Settings.**
Add the following entries

  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  Category   |  Subcategory          |  Type     |  Value                    |  Enabled  |  Required?  |
  +=============+=======================+===========+===========================+===========+=============+
  |  voicemail  |  transcribe_provider  |  text     |  custom                   |  True     |             |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  voicemail  |  transcription_server |  text     |  https://yourserver       |  True     |             |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  voicemail  |  json_enabled         |  boolean  |  true                     |  True     |  Optional   |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  voicemail  |  api_key              | text      |  your_api_key             |  True     |  Optional   |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |             |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+
  |  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |             |
  +-------------+-----------------------+-----------+---------------------------+-----------+-------------+

 Click "Reload" at the top of the page.

**Goto Status > Sip Status.**

Click "Flush Cache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.
