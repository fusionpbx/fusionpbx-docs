## Transcribe


The application for speech-to-text is used in FusionPBX 5.3.x and newer versions.

* Application -> Recordings (transcribe existing recordings)
* Application -> Voicemail -> Messages (transcribe on demand)
* Application -> Voicemail -> Email Queue (transcribe voicemail before sending)

---

### Required Dependency

```
apt install ffmpeg
```

---

### Install

The code changes below allow the new transcribe application to be used. To use the new version, you must upgrade FusionPBX to the latest version and then update the transcribe application.
```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

### Upgrade
```
cd /var/www/fusionpbx/app/transcribe
git pull
```

Upgrade from FusionPBX 5.2.x to 5.3.x 
- Use the menu to go to default settings
- **Watson**
  - Go to the voicemail category, copy the watson_key, and put the value in transcribe to subcategory api_key
  - Go to the voicemail category, copy the watson_url, and put the value in transcribe to subcategory api_url
  - In the transcribe category, set the engine to **watson**
- **Google**
  - Go to the voicemail category, copy the google_key, and put the value in transcribe to subcategory api_key
  - Go to the voicemail category, copy the google_url and put the value in transcribe to the subcategory api_url
    - https://speech.googleapis.com/v1p1beta1/speech
  - In the transcribe category, set the engine to **google**
  - Set the category to transcribe and language and value set to **en-US**
  - Set the category to transcribe and alternate_language and value set to **es-US**
- **Azure**
  - Go to the voicemail category, copy the azure_key, and put the value in transcribe to subcategory api_key
  - Go to the voicemail category, change the category to transcribe, and **language** and value set to **en-US**
  - The **api_url** is required. It should be set to the region, for example, **southcentralus**
  - Category voicemail and subcategory azure_server_region will now use the api_url for the region. At least at this time. It may be changed to a region in the future.
- **OpenAI**
  - Go to the category voicemail, then subcategory openai_key. Change the category to transcribe and the subcategory to api_key
  - Category voicemail and subcategory openai_url are not required
  - Category voicemail and subcategory openai_model are not required

---

### Voicemail transcription

Go [here](../applications/transcribe.md) to get more information on voicemail transcription.

### Default Settings

Make sure to set enabled to true to use the default settings.

* **Category** 
  * **transcribe**
* **Subcategory**
  * **api_key**        Get the key from the provider
  * **api_url**        Used by engine: google, watson, azure
  * **language** Used by engine: google, azure
  * **alternate_language**   Usedy by engine: google
  * **engine**         Options: openai, watson, google, azure
  * **enabled**        Options: true, false


---
