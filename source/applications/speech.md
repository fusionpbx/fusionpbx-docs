## Speech

Text-to-speech is used to make recordings that are typically used for IVR Menus, Voicemail Greetings, Ring Group Greeting, and more. Text-to-speech is available in FusionPBX 5.3.x and newer versions.

* Application -> Recordings
* Application -> Voicemail -> Greetings

---

### Dependencies

When MP3 is used, the following dependencies are required.
```
apt install sox libsox-fmt-all
```

---

### Install

The code changes below allow the new transcribe application to be used. To use the new version, you must upgrade FusionPBX to the latest version and then update the transcribe application.
```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe
git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

---

### Upgrade
```
cd /var/www/fusionpbx/app/speech
git pull
```

---

### Default Settings

Make sure to set enabled to true to use the default settings.

* **Category** 
  * **speech**
* **Subcategory**
  * **api_key**     Get the key from the provider
  * **engine**      Options: openai, elevenlabs
  * **enabled**     Options: true, false

---
