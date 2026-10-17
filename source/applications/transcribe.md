# Transcribe

The Transcribe application provides speech-to-text and is used in
FusionPBX 5.3.x and newer versions. Audio is converted to text by a
speech-to-text provider (OpenAI, Google, Azure, Watson, Inworld) or a
self-hosted transcription server.

Transcription is available from:

- **Application → Recordings** - transcribe existing recordings
- **Application → Voicemail → Messages** - transcribe on demand
- **Application → Voicemail → Email Queue** - transcribe the voicemail before the email is sent
- **Application → Call Recordings** - add call recordings to the transcribe queue
- **Status → Transcribe Queue** - view and manage queued transcriptions (superadmin)

For a step-by-step guide to voicemail transcription see
[Voicemail Transcription](voicemail_transcription.md).

---

## Required Dependency

Transcribe uses ffmpeg to convert audio files to the format the
provider expects.

```
apt install ffmpeg
```

---

## Install

To use the Transcribe application, upgrade FusionPBX to the latest
version and then install the transcribe application.

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

## Upgrade

```
cd /var/www/fusionpbx/app/transcribe
git pull
chown -R www-data:www-data /var/www/fusionpbx/app/transcribe
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

## Upgrading from FusionPBX 5.2.x to 5.3.x

- Use the menu to go to **Advanced → Default Settings**
- **Watson**
  - Go to the voicemail category, copy the watson_key, and put the value in transcribe subcategory api_key
  - Go to the voicemail category, copy the watson_url, and put the value in transcribe subcategory api_url
  - In the transcribe category, set the engine to **watson**
- **Google**
  - Go to the voicemail category, copy the google_key, and put the value in transcribe subcategory api_key
  - Go to the voicemail category, copy the google_url and put the value in transcribe subcategory api_url
    - https://speech.googleapis.com/v1p1beta1/speech
  - In the transcribe category, set the engine to **google**
  - Set the category to transcribe and language value to **en-US**
  - Set the category to transcribe and alternate_language value to **es-US**
- **Azure**
  - Go to the voicemail category, copy the azure_key, and put the value in transcribe subcategory api_key
  - Go to the voicemail category, change the category to transcribe, and set **language** to **en-US**
  - The **api_url** is required. It should be set to the region, for example, **southcentralus**
  - Voicemail subcategory azure_server_region will now use the api_url for the region. It may be changed to a region in the future.
- **OpenAI**
  - Go to the category voicemail, then subcategory openai_key. Change the category to transcribe and the subcategory to api_key
  - Voicemail subcategory openai_url is not required
  - Voicemail subcategory openai_model is not required

---

## Default Settings

Go to **Advanced → Default Settings** and use the drop-down filter to
select the **transcribe** category. Make sure to set **enabled** to
true to use the application.

| Subcategory | Type | Default | Description |
|---|---|---|---|
| enabled | boolean | true (not enabled) | Speech to Text API enabled. |
| engine | text | openai | Speech to Text API engine. Options: openai, google, azure, watson, inworld, local |
| api_key | text | | Speech to Text API key. Get the key from the provider. |
| api_url | text | | Speech to Text API URL. Used by: google, watson, azure. Optional for the other engines. |
| limit | numeric | 3 | Limit the transcribe queue records to process at one time. |
| interval | numeric | 1 | How often to process the transcribe queue. |
| save_response | boolean | false | Save the Transcribe response in the transcribe queue. Use this for debugging the transcribe response. |

Additional settings read by the engines can be added to the
transcribe category as needed:

| Subcategory | Used by | Description |
|---|---|---|
| api_model | openai, inworld, local | Model to use. Defaults: openai **gpt-transcribe**, inworld **inworld/inworld-stt-1**, local **whisper-1** |
| language | google, azure, watson | Language of the audio, for example **en-US** |
| alternate_language | google | Alternate language, for example **es-US** |
| application_credentials | google | Google application credentials (service account) |
| diarize | openai, inworld | Enable speaker diarization for multi-channel recordings |
| sample_rate | inworld | Sample rate of the audio, default **16000** |
| stale_timeout | transcribe queue service | Seconds before a job stuck in processing is reset to pending. Default **3600** |

## Engines

**OpenAI** - Set engine to **openai** and add your api_key. The
api_url defaults to
https://api.openai.com/v1/audio/transcriptions. The default model is
**gpt-transcribe**; **whisper-1** is used when the audio file has
multiple channels. Note that gpt-transcribe has no timing or
diarization, so it is not a good option for conversational call
recording transcription - use an alternative provider such as
**inworld** for that.

**Google** - Set engine to **google**, add the api_key and set the
api_url (for example
https://speech.googleapis.com/v1p1beta1/speech), language and
alternate_language. Alternatively the
application_credentials setting can be used.

**Azure** - Set engine to **azure**, add the api_key, and set the
api_url to the service region, for example **southcentralus**. Set
the language of the audio.

**Watson** - Set engine to **watson**, add the api_key, api_url and
language.

**Inworld** - Set engine to **inworld** and add the api_key. The
api_url defaults to https://api.inworld.ai/stt/v1/transcribe and the
model defaults to **inworld/inworld-stt-1**. Single channel
recordings are transcribed directly; multi channel recordings are
transcribed with speaker diarization.

**Local** - Set engine to **local** to use a self-hosted
transcription server, for example a Whisper server. The api_url
defaults to http://127.0.0.1:8000/transcribe and the model defaults
to **whisper-1**.

---

## Transcribe Queue

Long running audio, such as call recordings, is transcribed in the
background through the transcribe queue. Entries are added with a
status of **pending** and are picked up by the transcribe queue
service. Job statuses are **pending**, **processing**,
**completed** and **failed**.

The **Status → Transcribe Queue** page (superadmin) lists the queued
jobs with their status and transcription. Open a job to view the
transcription or change its status - for example, set a failed job
back to **pending** to retry it, or delete a job.

Each queue entry records the hostname of the server that queued it,
and the queue service only processes jobs for its own hostname, so in
a multi-server setup each server processes its own queued jobs.

## Transcribe Queue Service

The transcribe queue is processed by a background service that runs
the app queue script. Service files are included in the app for
Debian (systemd) and FreeBSD.

Install the Debian service:

```
cp /var/www/fusionpbx/app/transcribe/resources/service/debian/transcribe_queue.service /etc/systemd/system/transcribe_queue.service
systemctl daemon-reload
systemctl enable --now transcribe_queue.service
```

The service processes up to **limit** jobs at a time (default 3),
checks the queue every **interval** seconds, and resets jobs stuck in
**processing** for longer than **stale_timeout** seconds (default
3600) back to **pending** so the queue does not get clogged after a
crash.
