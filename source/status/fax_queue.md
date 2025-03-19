# Fax Queue

Manage sending FAX in a queue. Sending a new FAX will go into the queue
as **Waiting**. Updated to send once they have succeeded or failed
after multiple attempts.

## Install Instructions

Make sure to upgrade to the latest FusionPBX version.

-   First, navigate to the upgrade page **Advanced** > **Upgrade**
-   Select and run both Schema and App Defaults
-   Then run the following commands to install as a service

```
    cp /var/www/fusionpbx/app/fax_queue/resources/service/debian.service /etc/systemd/system/fax_queue.service
    systemctl daemon-reload
    systemctl enable fax_queue
    systemctl start fax_queue
```

-   or as a cron job

```
    crontab -e
    * * * * * cd /var/www/fusionpbx && php /var/www/fusionpbx/app/fax_queue/resources/job/fax_queue.php
```

## Default Settings

Be sure all **FAX Queue** category settings are configured properly
within Default Settings, or emails will fail to send properly.
