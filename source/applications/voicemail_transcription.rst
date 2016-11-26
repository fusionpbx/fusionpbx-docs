*****************
Voicemail Transcription
*****************

|

Uses API services to transcribe voicemails into text to be used in the app-sms and the voicemail to email options. Currently (11/3/16) only supports microsoft bing

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
