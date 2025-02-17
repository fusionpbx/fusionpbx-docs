# Voicemail Transcription in FusionPBX 5.3

## Overview

This document provides a step-by-step guide for setting up the email
transcription service in FusionPBX version 5.3. It supports various
service providers such as OpenAI, Google, Azure, or a custom solution.

### Step-by-step

1.  **Log in to FusionPBX**
    -   Access the FusionPBX administrative interface.
2.  **Check for the \"Transcribe\" Option**
    -   Navigate to **Advanced** \> **Default Settings**.
    -   Use the drop-down filter to select \"\*\*Transcribe\*\*\".
    -   If the \"\*\*Transcribe\*\*\" option is already available, skip
        to step **5**. Otherwise, proceed to step **3**.
3.  **Install the Transcribe and Speech Apps**
    -   SSH into your server and run the following commands:

        ``` console
        cd /var/www/fusionpbx/app
        git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
        git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
        chown -R www-data:www-data /var/www/fusionpbx
        php /var/www/fusionpbx/core/upgrade/upgrade.php
        ```
4.  **Reload the FusionPBX Interface**
    -   Navigate back to **Advanced** \> **Default Settings**.
    -   The \"\*\*Transcribe\*\*\" section should now be available.
5.  **Configure Transcription Settings**
    -   In the \"\*\*Transcribe\*\*\" category, enable the following
        settings:

          Subcategory      Type      Value               Enabled   Description
          ---------------- --------- ------------------- --------- ----------------------------------------------------------------
          api[key]{#key}   text      secret[key]{#key}   true      Speech to Text API key
          api[url]{#url}   text      <https://api>\...   false     **\*Leave this alone unless you are using a custom service**\*
          enabled          boolean   true                true      Speech to Text Enabled
          engine           text      openai              true      Options: openai, google, azure, custom

    -   Click **Reload** to apply the changes.
6.  **Enable Transcription for a Single Extension**
    -   Navigate to **Accounts** \> **Extensions**.
    -   Select the desired extension.
    -   Set **Transcription Enabled** to **True**.
7.  **Enable Transcription by Default for All Extensions**
    -   Navigate to **Advanced** \> **Default Settings**.
    -   Use the drop-down filter to select \"\*\*Voicemail\*\*\".
    -   Enable the **transcription_enabled_default** setting.
8.  **Test the Service**
    -   Leave a voicemail for the enabled extension to verify that the
        transcription works correctly.

:::: note
::: title
Note
:::

The primary function handling voicemail transcriptions is defined in
[transcribe.php](https://github.com/fusionpbx/fusionpbx/blob/master/app/email_queue/resources/functions/transcribe.php).
::::

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Voicemail Transcription in FusionPBX
5.2 and older \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

| 

Uses API services to transcribe voicemails into text to be used in the
app-sms and the voicemail to email options. Bing\'s Speech API or other
generic APIs can be used.

## IBM Watson API

Sign up and language information is located on [IBM Watson\'s
Site](https://cloud.ibm.com/catalog/services/speech-to-text)

:::: warning
::: title
Warning
:::

We cannot use mod[shout]{#shout} to record Voicemails because the
transcription service needs an uncompressed version of the audio.
Therefore we will record in WAV and then use LAME to re-encode in MP3.
This could cause added resource utilization to your system.
::::

**Goto Advanced \> Default Settings.** Add the following entries

> +---------+-----------------+--------+--------------------+--------+
> | > C     | > Subcategory   | > Type | > Value            | > E    |
> | ategory |                 |        |                    | nabled |
> +=========+=================+========+====================+========+
> | > vo    | > t             | > text | > watson           | > True |
> | icemail | ranscribe[provi |        |                    |        |
> |         | der]{#provider} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > wa            | > text | > { your watson    | > True |
> | icemail | tson[key]{#key} |        | > key }            |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > wa            | > text | > { watson url }   |        |
> | icemail | tson[url]{#url} |        | > \| True \|       |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > t             | > text | > en-US            | > True |
> | icemail | ranscribe[langu |        |                    |        |
> |         | age]{#language} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | >               | > b    | > true             | > True |
> | icemail |  transcribe[ena | oolean |                    |        |
> |         | bled]{#enabled} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > json[ena      | > b    | > true             | > True |
> | icemail | bled]{#enabled} | oolean |                    |        |
> +---------+-----------------+--------+--------------------+--------+

*NOTE: Watson URL used for testing was the following:
https://example.url.api.us-south.speech-to-text.watson.cloud.ibm.com/instances/{GUID}/v1/recognize?model=en-US_Telephony&smart_formatting=true*

**List of available IBM Watson speech to text models**
<https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models>

> Click \"Reload\" at the top of the page.

**Goto Status \> Sip Status.**

Click \"Flush Cache\", \"Reload XML\" and \"Rescan\".

If you entered your key\'s correctly, you should now start getting
transcriptions delivered in your voicemail to email and you will also
see them on the Messages page.

## Azure API

**Goto Advanced \> Default Settings.** Add the following entries

> +---------+-----------------+--------+--------------------+--------+
> | > C     | > Subcategory   | > Type | > Value            | > E    |
> | ategory |                 |        |                    | nabled |
> +=========+=================+========+====================+========+
> | > vo    | > t             | > text | > azure            | > True |
> | icemail | ranscribe[provi |        |                    |        |
> |         | der]{#provider} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > a             | > text | > { your azure key | > True |
> | icemail | zure[key]{#key} |        | > }                |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > azure[        | > text | > { your server    | > True |
> | icemail | server_region]{ |        | > region }         |        |
> |         | #server_region} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > t             | > text | > en-US            | > True |
> | icemail | ranscribe[langu |        |                    |        |
> |         | age]{#language} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | >               | > b    | > true             | > True |
> | icemail |  transcribe[ena | oolean |                    |        |
> |         | bled]{#enabled} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > json[ena      | > b    | > true             | > True |
> | icemail | bled]{#enabled} | oolean |                    |        |
> +---------+-----------------+--------+--------------------+--------+
>
> Click \"Reload\" at the top of the page.

**Goto Status \> Sip Status.**

Click \"Flush Cache\", \"Reload XML\" and \"Rescan\".

If you entered your key\'s correctly, you should now start getting
transcriptions delivered in your voicemail to email and you will also
see them on the Messages page.

## Google API

**Goto Advanced \> Default Settings.** Add the following entries

> +---------+-----------------+--------+--------------------+--------+
> | > C     | > Subcategory   | > Type | > Value            | > E    |
> | ategory |                 |        |                    | nabled |
> +=========+=================+========+====================+========+
> | > vo    | > t             | > text | > google           | > True |
> | icemail | ranscribe[provi |        |                    |        |
> |         | der]{#provider} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > go            | > text | > { your google    | > True |
> | icemail | ogle[key]{#key} |        | > key }            |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > go            | > text | > { your google    | > True |
> | icemail | ogle[url]{#url} |        | > url }            |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > t             | > text | > en-US            | > True |
> | icemail | ranscribe[langu |        |                    |        |
> |         | age]{#language} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | >               | > b    | > true             | > True |
> | icemail |  transcribe[ena | oolean |                    |        |
> |         | bled]{#enabled} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > json[ena      | > b    | > true             | > True |
> | icemail | bled]{#enabled} | oolean |                    |        |
> +---------+-----------------+--------+--------------------+--------+
>
> Click \"Reload\" at the top of the page.

**Goto Status \> Sip Status.**

Click \"Flush Cache\", \"Reload XML\" and \"Rescan\".

If you entered your key\'s correctly, you should now start getting
transcriptions delivered in your voicemail to email and you will also
see them on the Messages page.

## Bing API

Recommend using Azure as an alternative to Bing.

Sign up and language information is located on [Microsoft
Site](https://www.microsoft.com/cognitive-services/en-us/Speech-api/documentation/API-Reference-REST/BingVoiceRecognition)
Note: The Bing Speech API is deprecated as of October 2018, this works
for now but needs to be ported to [the new
API](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Speech-Service/how-to-migrate-from-bing-speech.md)

:::: warning
::: title
Warning
:::

We cannot use mod[shout]{#shout} to record Voicemails because the
transcription service needs an uncompressed version of the audio.
Therefore we will record in WAV and then use LAME to re-encode in MP3.
This could cause added resource utilization to your system.
::::

**Goto Advanced \> Default Settings.** Add the following entries

> +---------+-----------------+--------+--------------------+--------+
> | > C     | > Subcategory   | > Type | > Value            | > E    |
> | ategory |                 |        |                    | nabled |
> +=========+=================+========+====================+========+
> | > vo    | > t             | > text | > microsoft        | > True |
> | icemail | ranscribe[provi |        |                    |        |
> |         | der]{#provider} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > microso       | > text | > {your microsoft  | > True |
> | icemail | ft[key1]{#key1} |        | > key #1}          |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > microso       | > text | > {your microsoft  | > True |
> | icemail | ft[key2]{#key2} |        | > key #2}          |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | > t             | > text | > en-US            | > True |
> | icemail | ranscribe[langu |        |                    |        |
> |         | age]{#language} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
> | > vo    | >               | > b    | > true             | > True |
> | icemail |  transcribe[ena | oolean |                    |        |
> |         | bled]{#enabled} |        |                    |        |
> +---------+-----------------+--------+--------------------+--------+
>
> Click \"Reload\" at the top of the page.

**Goto Status \> Sip Status.**

Click \"Flush Cache\", \"Reload XML\" and \"Rescan\".

If you entered your key\'s correctly, you should now start getting
transcriptions delivered in your voicemail to email and you will also
see them on the Messages page.

## Custom API

Currently does not work with the FusionPBX email[queue]{#queue}.

API info from the Speech to Text provider of your choice is needed, or
you can self host a transcription engine like [Mozilla
DeepSpeech](https://git.callpipe.com/fusionpbx/deepspeech_frontend) or
[Kaldi ASR](https://github.com/dialogflow/asr-server)

**Goto Advanced \> Default Settings.** Add the following entries

> +--------+---------------+-------+-----------------+-------+--------+
> | > Ca   | > Subcategory | >     | > Value         | > En  | > Req  |
> | tegory |               |  Type |                 | abled | uired? |
> +========+===============+=======+=================+=======+========+
> | > voi  | > trans       | >     | > custom        | >     |        |
> | cemail | cribe[provide |  text |                 |  True |        |
> |        | r]{#provider} |       |                 |       |        |
> +--------+---------------+-------+-----------------+-------+--------+
> | > voi  | > tran        | >     | > <http         | >     |        |
> | cemail | scription[ser |  text | s://yourserver> |  True |        |
> |        | ver]{#server} |       |                 |       |        |
> +--------+---------------+-------+-----------------+-------+--------+
> | > voi  | > json[enabl  | > bo  | > true          | >     | > Op   |
> | cemail | ed]{#enabled} | olean |                 |  True | tional |
> +--------+---------------+-------+-----------------+-------+--------+
> | > voi  | > a           | text  | > your[api      | >     | > Op   |
> | cemail | pi[key]{#key} |       | _key]{#api_key} |  True | tional |
> +--------+---------------+-------+-----------------+-------+--------+
> | > voi  | > trans       | >     | > en-US         | >     |        |
> | cemail | cribe[languag |  text |                 |  True |        |
> |        | e]{#language} |       |                 |       |        |
> +--------+---------------+-------+-----------------+-------+--------+
> | > voi  | > tra         | > bo  | > true          | >     |        |
> | cemail | nscribe[enabl | olean |                 |  True |        |
> |        | ed]{#enabled} |       |                 |       |        |
> +--------+---------------+-------+-----------------+-------+--------+
>
> Click \"Reload\" at the top of the page.

**Goto Status \> Sip Status.**

Click \"Flush Cache\", \"Reload XML\" and \"Rescan\".

If you entered your key\'s correctly, you should now start getting
transcriptions delivered in your voicemail to email and you will also
see them on the Messages page.
