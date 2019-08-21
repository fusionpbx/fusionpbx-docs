*****************
Voicemail Transcription
*****************

|

Uses API services to transcribe voicemails into text to be used in the app-sms and the voicemail to email options. Bing's Speech API or other generic APIs can be used.

Bing API
====================


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

Click "Flush Memcache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.

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
  |  voicemail  |  watson_url           |  text     |  { *watson url }          |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_language  |  text     |  en-US                    |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  transcribe_enabled   |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+
  |  voicemail  |  json_enabled         |  boolean  |  true                     |  True     |
  +-------------+-----------------------+-----------+---------------------------+-----------+

*NOTE: Watson URL used for testing was the following:
https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-US_NarrowbandModel*

 Click "Reload" at the top of the page.

**Goto Status > Sip Status.**

Click "Flush Memcache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.

Custom API
====================


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

Click "Flush Memcache", "Reload XML" and "Rescan".

If you entered your key's correctly, you should now start getting transcriptions delivered in your voicemail to email and you will also see them on the Messages page.
