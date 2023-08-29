#############
Messages
#############



Send and receive SMS and MMS messages. This tool utilizes a service called, message_queue to send and receive messages. It relays SMS messages to registered endpoints including softphones and desk phones that support message_queue. This feature does support multiple Providers simultaneously.


.. Install::

::

 cd /var/www/fusionpbx/app
 git clone https://github.com/fusionpbx/fusionpbx-app-messages.git messages
 git clone https://github.com/fusionpbx/fusionpbx-app-providers.git providers
 php /var/www/fusionpbx/core/upgrade/upgrade.php

|

* **App Defaults** After getting the source code run Upgrade -> App Defaults
* **Upgrade Schema** Next run Advanced -> Upgrade -> Schema (checked) then press Execute
* **Permissions** From Advanced -> Upgrade -> Permission Defaults (checked) then press Execute
* **Menu** From Advanced -> Upgrade -> Menu Defaults (checked) then press Execute

.. Menu::

::

    If you used restore menu defaults you can skip this step.
    Providers
        Title: Providers
        Link: /app/providers/providers.php
        Parent Menu: Accounts
        Groups: superadmin
    Messages
        Title: Messages
        Link: /app/messages/messages.php
        Parent Menu: Applications
        Groups: superadmin

|

.. Install the Services::

::

  cp /var/www/fusionpbx/app/messages/resources/service/debian-message_queue.service /etc/systemd/system/message_queue.service
  systemctl enable message_queue
  systemctl start message_queue
  systemctl daemon-reload

|

::

  cp /var/www/fusionpbx/app/messages/resources/service/debian-message_events.service /etc/systemd/system/message_events.service
  systemctl enable message_events
  systemctl start message_events
  systemctl daemon-reload

|


.. Rewrite Rules for MMS::

* Add the NGINX rewrite rule to support the media URL to support MMS.

::

  nano /etc/nginx/sites-enabled/fusionpbx

|

* Add the message media rewrite below inside the server 443 section. Add it just below the REST API rewrite rule or just above the phone vendor rewrite rules.

::
        
server {
        listen 443;

|

* Rewrite rule

::

  #message media
  rewrite "^/app/messages/media/(.*)/(.*)" /app/messages/message_media.php?id=$1&action=download last;

|

Then restart nginx

::

  service nginx restart

|

.. Setup::
        
* Go to Menu Accounts -> Providers.
* Press the **ADD** button and find your provider and then press the **SETUP** button. After adding your provider will need to get Add your API key authorization to the settings that were added for your SMS provider.
* If your provider is not listed then you will need access to your Providers SMS API documentation and would need to compare with the other providers. When you are ready to add your provider press **Add a Provider** for a template to start from. You may need support to get through this step if you need to add your own VoIP provider. If you are observant and like to use your brain you do have a chance at working through this and get it working.

**Destinations -> Inbound**
* Assign the destination to a user or group.
  * In Dialplan -> Destinations make sure the number you have enabled for SMS is assigned to a user account and to a provider using the select list in inbound destinations.
* Make sure to set the Country Code. This helps to match the SMS destination number with an inbound destination. It makes it possible to the number without the country code, with the country code and e.164.

**Extensions**
* In Accounts -> Extensions make sure the user is assigned to an extension.

**Mobile**
* On your mobile phone send an SMS or MMS message to the number you set up for SMS with the provider.

**Messages**
* Application -> Messages from here you can use the New Messages button to send an SMS or MMS message.

**Providers**
* The providers are identified and allowed to use IP authentication.


