# Email Queue

Manage sending emails in a queue. Also works with the transcription of
audio files with IBM Watson, Azure, or Google.

# Install Instructions

-   Make sure to upgrade to the latest FusionPBX version
-   Update the database structure
    -   Advanced -\> Upgrade -\> Schema
-   Update App Defaults
    -   Advanced -\> Upgrade -\> App Defaults
-   Run the following commands to install as a service

<!-- -->

    cp /var/www/fusionpbx/app/email_queue/resources/service/debian.service /etc/systemd/system/email_queue.service
    systemctl enable email_queue
    systemctl start email_queue
    systemctl daemon-reload

-   or as a cron job

<!-- -->

    crontab -e
    * * * * * cd /var/www/fusionpbx && /usr/bin/php /var/www/fusionpbx/app/email_queue/resources/service/email_queue.php

# Default Settings

Be sure all **Email** category settings are configured properly within
Default Settings, or emails will fail to send properly.
