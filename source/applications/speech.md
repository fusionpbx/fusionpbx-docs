# Speech

The Speech application provides text-to-speech (TTS) and is used in
FusionPBX 5.3.x and newer versions. It converts text into audio
recordings using an AI text-to-speech provider (OpenAI, ElevenLabs,
Inworld) or a self-hosted transcription server.

The generated recordings are typically used for IVR Menus, Voicemail
Greetings, Ring Group Greetings, and more. Text-to-speech is available
from:

- **Application → Recordings** - create a recording from text
- **Application → Voicemail → Greetings** - generate a greeting from text
- **Application → Ring Groups** - generate the ring group greeting
- **Application → IVR Menus** - generate the IVR prompts

For speech-to-text (transcription) see
[Transcribe](transcribe.md).

---

## Required Dependency

Speech uses sox to convert the generated audio to the format that the
file extension expects (for example, when an mp3 file is regenerated
by a wav engine).

```
apt install sox libsox-fmt-all
```

---

## Install

To use the Speech application, upgrade FusionPBX to the latest
version and then install the speech application.

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

Speech is often installed together with the
[Transcribe](transcribe.md) application. In that case, clone both
before running the upgrade script:

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

## Upgrade

```
cd /var/www/fusionpbx/app/speech
git pull
chown -R www-data:www-data /var/www/fusionpbx/app/speech
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

## Default Settings

Go to **Advanced → Default Settings** and use the drop-down filter to
select the **speech** category. All of the settings are disabled by
default - make sure to set **enabled** to true to use the application.

| Subcategory | Type | Default | Description |
|---|---|---|---|
| enabled | boolean | true (not enabled) | Text to Speech API enabled. |
| engine | text | openai | Text to Speech API engine. Options: openai, elevenlabs, inworld, local |
| api_key | text | | Text to Speech API key. Get the key from the provider. |
| api_url | text | | Text to Speech API URL. Overrides the provider URL, or points at a self-hosted server (local engine). |

After making changes, click **Reload**.

---

## Engines

The **engine** setting selects the text-to-speech provider. Each
engine has its own voices, output format, and supported options.

| Engine | API key | API URL | Format | Speed | Voices |
|---|---|---|---|---|---|
| openai | required | optional (default https://api.openai.com/v1/audio/speech) | wav | yes | fixed list |
| elevenlabs | required | fixed | mp3 | yes | from your account |
| inworld | required (Basic/Base64) | fixed | wav | no | from the API, by language |
| local | not used | required (default http://localhost:8001/speech) | wav | no | fixed list |

**OpenAI** - Set engine to **openai** and add your api_key. The
api_url defaults to https://api.openai.com/v1/audio/speech and can be
left as is. The voices (alloy, ash, coral, echo, fable, nova, onyx,
sage, shimmer) are a fixed list and speed control is available from
0.25x to 4.0x.

**ElevenLabs** - Set engine to **elevenlabs** and add your api_key
(x-api-key). The api_url is fixed to the ElevenLabs API. The audio is
generated as an mp3. The available voices and model are retrieved
automatically from your ElevenLabs account, and speed control is
available.

**Inworld** - Set engine to **inworld** and add the api_key. Inworld
uses a Basic (Base64) key, not a bearer key. The available voices are
retrieved from the Inworld API and grouped by language; the audio is
generated as a wav file.

**Local** - Set engine to **local** to use a self-hosted
text-to-speech server. Set the api_url to the server address, for
example http://localhost:8001/speech. No api_key is required. The
audio is generated as a wav file.

---

## How it Works

On the edit pages (for example Recordings and Voicemail Greetings),
the **voice** drop-down is populated from the selected engine and the
**speed** drop-down is only shown when the engine supports speed
control. Enter the text in the message field and, when a voice and a
message are both set, clicking **Add** (or the create/update option
when editing) generates the audio file from the text.

Each engine outputs its own native format (wav for openai, local and
inworld, mp3 for elevenlabs). If the file name uses a different
extension than the engine output, the audio is transcoded with sox so
the content matches the extension. The file name is never changed, so
existing references from IVR menus, ring groups, voicemail and so on
remain valid. This is why the sox dependency is required.
