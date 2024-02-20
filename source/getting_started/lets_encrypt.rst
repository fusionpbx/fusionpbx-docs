***************
Let's Encrypt
***************

Let's Encrypt is one of the most recent and widely used form of free SSL security and supports wildcard DNS.  You can use Let's Encrypt with your FusionPBX install and WebRTC like `Verto Communicator`_.


Dehydrated (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FusionPBX has an option to easliy and quickly install SSL with Let's Encrypt using **letsencrypt.sh**  With this script you can choose either to request an SSL certificate with wildcard (*.domain.tld) or hostnames (domain.tld).

The letsencrypt.sh will do the following:

* Download `dehydrated <https://github.com/lukas2511/dehydrated>`_.
* Request an SSL certificate from `Let's Encrypt <https://letsencrypt.com>`_.
* Configure NGINX to use the SSL certificate.
* Combine and place SSL certificate in the proper `FreeSWITCH <https://freeswitch.org/confluence/display/FREESWITCH/FreeSWITCH+Explained>`_ directory for using TLS.
* Test and make sure the SSL cert works and outputs if sucessful.

Using letsencrypt.sh
---------------------

With letsencrypt.sh you have the choice of creating an SSL certificate for a single domain (domain.tld), multiple sub domains(sub.domain.tld, sub1.domain.tld, etc.domain.tld) or wildcard (*.domain.tld).  The easy way however is using the hostname method. 

Hostname
~~~~~~~~~~

To create a hostname or multiple hostname SSL certificate go to:

::

 cd /usr/src/fusionpbx-install.sh/debian/resources/

Then execute the script.

::

 ./letsencrypt.sh
 
 
You should then see and follow the prompts.

::

 Domain Name: domain.tld
 Email Address: support@fusionpbx.com

Note you can enter multiple hostnames under the same domain such as `pbx1.domain.tld pbx2.domain.tld pbx3.domain.tld`.

After that, you should see the following output.

::

 Cloning into 'dehydrated'...
 remote: Counting objects: 1914, done.
 remote: Total 1914 (delta 0), reused 0 (delta 0), pack-reused 1914
 Receiving objects: 100% (1914/1914), 616.01 KiB | 0 bytes/s, done.
 Resolving deltas: 100% (1199/1199), done.
 # INFO: Using main config file /etc/dehydrated/config
 + Generating account key...
 + Registering account key with ACME server...
 + Done!
 # INFO: Using main config file /etc/dehydrated/config
 + Creating chain cache directory /etc/dehydrated/chains
 Processing domain.tld
 + Creating new directory /etc/dehydrated/certs/domain.tld ...
 + Signing domains...
 + Generating private key...
 + Generating signing request...
 + Requesting new certificate order from CA...
 + Received 1 authorizations URLs from the CA
 + Handling authorization for domain.tld
 + 1 pending challenge(s)
 + Deploying challenge tokens...
 + Responding to challenge for domain.tld authorization...
 + Challenge is valid!
 + Cleaning challenge tokens...
 + Requesting certificate...
 + Checking certificate...
 + Done!
 + Creating fullchain.pem...
 + Done!
 
 nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
 nginx: configuration file /etc/nginx/nginx.conf test is successful


Wildcard
~~~~~~~~~~~

To create a wildcard SSL certificate go to:

::

 cd /usr/src/fusionpbx-install.sh/debian/resources/


Then execute the script.

::

 ./letsencrypt.sh

You should then see and follow the prompts:

::

 Domain Name: *.domain.tld
 Email Address: support@fusionpbx.com
 
::

 Cloning into 'dns-01-manual'...
 remote: Counting objects: 9, done.
 remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 9
 Unpacking objects: 100% (9/9), done.
 Checking connectivity... done.
 # INFO: Using main config file /etc/dehydrated/config
 + Account already registered!
 # INFO: Using main config file /etc/dehydrated/config
 Processing *.domain.tld
 + Checking domain name(s) of existing cert... changed!
 + Domain name(s) are not matching!
 + Names in old certificate: domain.tld
 + Configured names: *.domain.tld
 + Forcing renew.
 + Checking expire date of existing cert...
 + Valid till Nov 19 16:08:32 2018 GMT (Longer than 30 days). Ignoring because renew was forced!
 + Signing domains...
 + Generating private key...
 + Generating signing request...
 + Requesting new certificate order from CA...
 + Received 1 authorizations URLs from the CA
 + Handling authorization for domain.tld
 + 1 pending challenge(s)
 + Deploying challenge tokens...


.. note::

      When you define the txt record with your domain registrar be sure to use the output of the script you are running and not what is in this example.

::

 Add the following to the zone definition of domain.tld:
 _acme-challenge.domain.tld. IN TXT "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"

 **Press enter to continue...**

::

 + Responding to challenge for domain.tld authorization...
 + Challenge is valid!
 + Cleaning challenge tokens...

::

 Now you can remove the following from the zone definition of domain.tld:
 _acme-challenge.domain.tld. IN TXT "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"

 **Press enter to continue...**

::

 + Requesting certificate...
 + Checking certificate...
 + Done!
 + Creating fullchain.pem...

 deploy_cert()

 Done!

 **done**

 nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
 nginx: configuration file /etc/nginx/nginx.conf test is successful

.. tip::

       Use the dig command to check that the txt record is correct.  dig -t txt _acme-challenge.domain.tld
       
       Output should show:
       
       ;; ANSWER SECTION:
       _acme-challenge.domain.tld. 1799 IN TXT  "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"



Setup for multiple domains on Let's Encrypt
===========================================

Before setting up multiple domains, make sure you have SSL working on your main domain using the instructions above.

**Create shared nginx host file for all domains**

``mkdir -p /etc/nginx/includes && vim /etc/nginx/includes/fusionpbx-default-config``
 
Paste the code below into the file

::
 
 ssl_protocols           TLSv1 TLSv1.1 TLSv1.2;
 ssl_ciphers             HIGH:!ADH:!MD5:!aNULL;
 #ssl_dhparam
 
 #redirect letsencrypt to dehydrated
 location ^~ /.well-known/acme-challenge {
 default_type "text/plain";
 auth_basic "off";
 alias /var/www/dehydrated;
 }
 
 #REST api
 if ($uri ~* ^.*/api/.*$) {
 rewrite ^(.*)/api/(.*)$ $1/api/index.php?rewrite_uri=$2 last;
 break;
 }
 
 #message media
 rewrite "^/app/messages/media/(.*)/(.*)" /app/messages/message_media.php?id=$1&action=download last;
 
 #algo
 rewrite "^.*/provision/algom([A-Fa-f0-9]{12})\.conf" /app/provision/?mac=$1&file=algom%7b%24mac%7d.conf last;
 
 #mitel
 rewrite "^.*/provision/MN_([A-Fa-f0-9]{12})\.cfg" /app/provision/index.php?mac=$1&file=MN_%7b%24mac%7d.cfg last;
 rewrite "^.*/provision/MN_Generic.cfg" /app/provision/index.php?mac=08000f000000&file=MN_Generic.cfg last;
 
 #grandstream
 rewrite "^.*/provision/cfg([A-Fa-f0-9]{12})(\.(xml|cfg))?$" /app/provision/?mac=$1;
 rewrite "^.*/provision/pb/([A-Fa-f0-9]{12})/phonebook\.xml$" /app/provision/?mac=$1&file=phonebook.xml;
 #grandstream-wave softphone by ext because Android doesn't pass MAC.
 rewrite "^.*/provision/([0-9]{5})/cfg([A-Fa-f0-9]{12}).xml$" /app/provision/?ext=$1;
 
 #aastra
 rewrite "^.*/provision/aastra.cfg$" /app/provision/?mac=$1&file=aastra.cfg;
 #rewrite "^.*/provision/([A-Fa-f0-9]{12})(\.(cfg))?$" /app/provision/?mac=$1 last;
 
 #yealink
 #rewrite "^.*/provision/(y[0-9]{12})(\.cfg|\.boot)?$" /app/provision/index.php?file=$1$2;
 rewrite "^.*/provision/(y[0-9]{12})(\.cfg)?$" /app/provision/index.php?file=$1.cfg;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})(\.(xml|cfg))?$" /app/provision/index.php?mac=$1 last;
 
 #polycom
 rewrite "^.*/provision/000000000000.cfg$" "/app/provision/?mac=$1&file={%24mac}.cfg";
 #rewrite "^.*/provision/sip_330(\.(ld))$" /includes/firmware/sip_330.$2;
 rewrite "^.*/provision/features.cfg$" /app/provision/?mac=$1&file=features.cfg;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-sip.cfg$" /app/provision/?mac=$1&file=sip.cfg;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-phone.cfg$" /app/provision/?mac=$1;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-registration.cfg$" "/app/provision/?mac=$1&file={%24mac}-registration.cfg";
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-directory.xml$" "/app/provision/?mac=$1&file={%24mac}-directory.xml";
 
 #cisco
 rewrite "^.*/provision/file/(.*\.(xml|cfg))" /app/provision/?file=$1 last;
 
 #Escene
 rewrite "^.*/provision/([0-9]{1,11})_Extern.xml$"       "/app/provision/?ext=$1&file={%24mac}_extern.xml" last;
 rewrite "^.*/provision/([0-9]{1,11})_Phonebook.xml$"    "/app/provision/?ext=$1&file={%24mac}_phonebook.xml" last;
 
 #Vtech
 rewrite "^.*/provision/VCS754_([A-Fa-f0-9]{12})\.cfg$" /app/provision/?mac=$1;
 rewrite "^.*/provision/pb([A-Fa-f0-9-]{12,17})/directory\.xml$" /app/provision/?mac=$1&file=directory.xml;
 
 access_log /var/log/nginx/access.log;
 error_log /var/log/nginx/error.log;
 
 client_max_body_size 80M;
 client_body_buffer_size 128k;
 
 location / {
 root /var/www/fusionpbx;
 index index.php;
 }
 
 location ~ \.php$ {
 fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
 #fastcgi_pass 127.0.0.1:9000;
 fastcgi_index index.php;
 include fastcgi_params;
 fastcgi_param   SCRIPT_FILENAME /var/www/fusionpbx$fastcgi_script_name;
 }
 
 # Allow the upgrade routines to run longer than normal
 location = /core/upgrade/index.php {
 fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
 #fastcgi_pass 127.0.0.1:9000;
 fastcgi_index index.php;
 include fastcgi_params;
 fastcgi_param   SCRIPT_FILENAME /var/www/fusionpbx$fastcgi_script_name;
 fastcgi_read_timeout 15m;
 }
 
 # Disable viewing .htaccess & .htpassword & .db & .git
 location ~ .htaccess {
 deny all;
 }
 location ~ .htpassword {
 deny all;
 }
 location ~^.+.(db)$ {
 deny all;
 }
 location ~ /.git/ {
 deny all;
 }


**Create a file to contain config for additional domains**

``touch /etc/nginx/includes/fusionpbx-domains``


**Make default file read configs for additional domains**

``echo "include /etc/nginx/includes/fusionpbx-domains;" >> /etc/nginx/sites-available/fusionpbx``


By now you are all set to start using SSL on multiple domains for your FusionPBX installation.


**Follow the steps below everytime your add a new domain**

Add the new domain to a new line at the bottom of

``vim /etc/dehydrated/domains.txt``


Obtain the cert from Let's Encrypt using Dehydrated

``dehydrated -c``


**Set cert to auto renew with other domains**

``vim /etc/crontab``
 
 
Add the following lines at the bottom of the crontab file

::

 0 1 * * 0  root  /usr/local/sbin/dehydrated -c
 5 1 * * 0  root  systemctl reload nginx


Finally add your new domain to be loaded

``vim /etc/nginx/includes/fusionpbx-domains``


Paste the below at the very end of the file (again replace example.com with your domain)

::

 server {
         listen 443 ssl;
         server_name example.com;
         ssl_certificate /etc/dehydrated/certs/example.com/fullchain.pem;
         ssl_certificate_key /etc/dehydrated/certs/example.com/privkey.pem;

         include /etc/nginx/includes/fusionpbx-default-config;
 }
 
 
Test your new NGINX config

``nginx -t``

You're all set! Restart nginx for changes to take effect

 ``systemctl nginx restart``


.. _link: https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx
.. _Verto Communicator: https://freeswitch.org/confluence/display/FREESWITCH/Verto+Communicator



