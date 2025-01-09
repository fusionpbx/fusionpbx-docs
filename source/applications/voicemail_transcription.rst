Voicemail Transcription in FusionPBX 5.3

Log in to FusionPBX

  Access the FusionPBX administrative interface.

Check for the "Transcribe" Option

  Navigate to Advanced > Default Settings.

  Use the drop-down filter to select "Transcribe".

  If the "Transcribe" option exists, skip to step 5. Otherwise, continue to step 3.

Install the Transcribe and Speech Apps

  SSH into your server and run the following commands:

  cd /var/www/fusionpbx/app

  git clone https://github.com/fusionpbx/fusionpbx-app-transcribe.git transcribe

  git clone https://github.com/fusionpbx/fusionpbx-app-speech.git speech

  chown -R www-data:www-data /var/www/fusionpbx

  php /var/www/fusionpbx/core/upgrade/upgrade.php

Reload the FusionPBX Interface

  Navigate back to Advanced > Default Settings.

  The "Transcribe" section should now be available.

Configure Transcription Settings

  In the **"Transcribe"**category, find and enable the following settings:

    api_key: Enter your API key for the transcription service.

    enabled: Set to True.

    engine: Type your transcription provider (e.g., openai, google, azure, etc.).

    api_url: Leave this blank

  Click Reload to apply the changes.

Enable Transcription for one Extension

  Navigate to Accounts > Extensions.

  Select the desired extension.

  Set Transcription Enabled to True.

Enable Transcription by Default for Everyone.

  Navigate to Advanced > Default Settings.

  Use the drop-down filter to select "Voicemail".

  Find and enable the setting transcription_enabled_default.

Test the Service

  Leave a voicemail for that extension to verify the transcription works correctly.