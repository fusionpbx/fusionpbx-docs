# Voicemail Transcription in FusionPBX 5.3

## Overview
This document provides a step-by-step guide for setting up the email transcription service in FusionPBX version 5.3. It supports various service providers such as OpenAI, Google, Azure, or a custom solution.

## Step-by-Step
1. **Log in to FusionPBX**
   - Access the FusionPBX administrative interface.   

2. **Check for the "Transcribe" Option**
   - Navigate to **Advanced** > **Default Settings**.
   - Use the drop-down filter to select "**Transcribe**".
   - If the "**Transcribe**" option is already available, skip to step **5**. Otherwise, proceed to step **3**.   

3. **Install the Transcribe and Speech Apps**
   - SSH into your server and run the following commands:

        ``` console
        cd /var/www/fusionpbx/app
        git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
        git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
        chown -R www-data:www-data /var/www/fusionpbx
        php /var/www/fusionpbx/core/upgrade/upgrade.php
        ```
        
4. **Reload the FusionPBX Interface**
- Navigate back to **Advanced** > **Default Settings**.
- The "**Transcribe**" section should now be available.

5. **Configure Transcription Settings**
- In the "**Transcribe**" category, enable the following settings:

| Subcategory | Type   | Value            | Enabled | Description                                           |
|-------------|--------|------------------|---------|-------------------------------------------------------|
| api_key     | text   | secret_key       | true    | Speech to Text API key                                |
| api_url     | text   | https://api...   | false   | ***Leave this alone unless using a custom service*** |
| enabled     | boolean| true            | true    | Speech to Text Enabled                                |
| engine      | text   | openai           | true    | Options: openai, google, azure, custom                |

- Click **Reload** to apply the changes.

6. **Enable Transcription for a Single Extension**
   - Navigate to **Accounts** > **Extensions**.
   - Select the desired extension.
   - Set **Transcription Enabled** to **True**.

7. **Enable Transcription by Default for All Extensions**
   - Navigate to **Advanced** > **Default Settings**.
   - Use the drop-down filter to select "**Voicemail**".
   - Enable the **transcription_enabled_default** setting.

8. **Test the Service**
   - Leave a voicemail for the enabled extension to verify that the transcription works correctly.

:::{note}   
The primary function handling voicemail transcriptions is defined in [transcribe.php](https://github.com/fusionpbx/fusionpbx/blob/master/app/email_queue/resources/functions/transcribe.php).   
:::

---

# Voicemail Transcription in FusionPBX 5.2 and Older

Uses API services to transcribe voicemails into text for use in the app-sms and voicemail-to-email options. Bing's Speech API or other generic APIs can be used.

## IBM Watson API
Sign up and language information is located on [IBM Watson's Site](https://cloud.ibm.com/catalog/services/speech-to-text).

:::{warning}   
We cannot use mod_shout to record voicemails because the transcription service needs an uncompressed version of the audio. Therefore, we will record in WAV and then use LAME to re-encode in MP3. This could cause added resource utilization to your system.   
:::

**Go to Advanced > Default Settings.**  
Add the following entries:

| Category  | Subcategory          | Type   | Value               | Enabled |
|-----------|----------------------|--------|---------------------|---------|
| voicemail | transcribe_provider  | text   | watson              | True    |
| voicemail | watson_key           | text   | {your watson key}   | True    |
| voicemail | watson_url           | text   | {watson url}        | True    |
| voicemail | transcribe_language  | text   | en-US               | True    |
| voicemail | transcribe_enabled   | boolean| true               | True    |
| voicemail | json_enabled         | boolean| true               | True    |

:::{note}   
Watson URL used for testing was:   
https://example.url.api.us-south.speech-to-text.watson.cloud.ibm.com/instances/{GUID}/v1/recognize?model=en-US_Telephony&smart_formatting=true*   
:::

**List of available IBM Watson speech-to-text models**:  
[https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models](https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models)

Click "Reload" at the top of the page.

**Go to Status > SIP Status.**  
Click "Flush Cache", "Reload XML", and "Rescan".

If you entered your keys correctly, you should now start getting transcriptions delivered in your voicemail-to-email and see them on the Messages page.

## Azure API
**Go to Advanced > Default Settings.**  
Add the following entries:

| Category  | Subcategory          | Type   | Value                 | Enabled |
|-----------|----------------------|--------|-----------------------|---------|
| voicemail | transcribe_provider  | text   | azure                 | True    |
| voicemail | azure_key            | text   | {your azure key}      | True    |
| voicemail | azure_server_region  | text   | {your server region}  | True    |
| voicemail | transcribe_language  | text   | en-US                 | True    |
| voicemail | transcribe_enabled   | boolean| true                  | True    |
| voicemail | json_enabled         | boolean| true                  | True    |

Click "Reload" at the top of the page.

**Go to Status > SIP Status.**  
Click "Flush Cache", "Reload XML", and "Rescan".

If you entered your keys correctly, you should now start getting transcriptions delivered in your voicemail-to-email and see them on the Messages page.

## Google API
**Go to Advanced > Default Settings.**  
Add the following entries:

| Category  | Subcategory          | Type   | Value               | Enabled |
|-----------|----------------------|--------|---------------------|---------|
| voicemail | transcribe_provider  | text   | google              | True    |
| voicemail | google_key           | text   | {your google key}   | True    |
| voicemail | google_url           | text   | {your google url}   | True    |
| voicemail | transcribe_language  | text   | en-US               | True    |
| voicemail | transcribe_enabled   | boolean| true               | True    |
| voicemail | json_enabled         | boolean| true               | True    |

Click "Reload" at the top of the page.

**Go to Status > SIP Status.**  
Click "Flush Cache", "Reload XML", and "Rescan".

If you entered your keys correctly, you should now start getting transcriptions delivered in your voicemail-to-email and see them on the Messages page.

## Bing API
Recommend using Azure as an alternative to Bing.

Sign up and language information is located on [Microsoft Site](https://www.microsoft.com/cognitive-services/en-us/Speech-api/documentation/API-Reference-REST/BingVoiceRecognition).  
Note: The Bing Speech API is deprecated as of October 2018; this works for now but needs to be ported to [the new API](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Speech-Service/how-to-migrate-from-bing-speech.md).

:::{warning}   
We cannot use mod_shout to record voicemails because the transcription service needs an uncompressed version of the audio. Therefore, we will record in WAV and then use LAME to re-encode in MP3. This could cause added resource utilization to your system.   
:::

**Go to Advanced > Default Settings.**  
Add the following entries:

| Category  | Subcategory          | Type   | Value                 | Enabled |
|-----------|----------------------|--------|-----------------------|---------|
| voicemail | transcribe_provider  | text   | microsoft             | True    |
| voicemail | microsoft_key1       | text   | {your microsoft key #1} | True  |
| voicemail | microsoft_key2       | text   | {your microsoft key #2} | True  |
| voicemail | transcribe_language  | text   | en-US                 | True    |
| voicemail | transcribe_enabled   | boolean| true                 | True    |

Click "Reload" at the top of the page.

**Go to Status > SIP Status.**  
Click "Flush Cache", "Reload XML", and "Rescan".

If you entered your keys correctly, you should now start getting transcriptions delivered in your voicemail-to-email and see them on the Messages page.

## Custom API
Currently does not work with the FusionPBX email_queue.

API info from the Speech-to-Text provider of your choice is needed, or you can self-host a transcription engine like [Mozilla DeepSpeech](https://git.callpipe.com/fusionpbx/deepspeech_frontend) or [Kaldi ASR](https://github.com/dialogflow/asr-server).

**Go to Advanced > Default Settings.**  
Add the following entries:

| Category  | Subcategory          | Type   | Value            | Enabled | Required? |
|-----------|----------------------|--------|------------------|---------|-----------|
| voicemail | transcribe_provider  | text   | custom           | True    |           |
| voicemail | transcription_server | text   | https://yourserver | True  |           |
| voicemail | json_enabled         | boolean| true            | True    | Optional  |
| voicemail | api_key              | text   | your_api_key     | True    | Optional  |
| voicemail | transcribe_language  | text   | en-US            | True    |           |
| voicemail | transcribe_enabled   | boolean| true            | True    |           |

Click "Reload" at the top of the page.

**Go to Status > SIP Status.**
