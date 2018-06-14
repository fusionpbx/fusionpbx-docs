Let's Encrypt
==============

Let's Encrypt is one of the most recent and widely used form of free SSL security but doesn't support wildcard DNS.  You can use Let's Encrypt with your FusionPBX install and WebRTC like `Verto Communicator`_.

More info on NGINX with Let's Encrypt
https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx

**Clone Let's Encrypt**

::

 
 git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt

**Execute certbot-auto**

::

 cd /opt/letsencrypt
 chmod a+x ./certbot-auto
 ./certbot-auto
 cd /etc/letsencrypt/
 mkdir -p configs
 cd configs
 
**Copy code example from** `link`_ **in step #2 section and edit domains, key size, email then put into: /etc/letsencrypt/configs/domain.tld.conf** (Edit domain.tld to reflect your domain)

::

 touch /etc/letsencrypt/configs/domain.tld.conf
 vim /etc/letsencrypt/configs/domain.tld.conf
 
**Edit /etc/nginx/sites-available/fusionpbx**

::

 vim  /etc/nginx/sites-available/fusionpbx
 Add this after the ssl_ciphers line
 
 location /.well-known/acme-challenge {
         root /var/www/letsencrypt;
     }
     
 Reload and check Nginx
 nginx -t && nginx -s reload
 Should output:
 nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
 nginx: configuration file /etc/nginx/nginx.conf test is successful

**Execute Let's Encrypt script**  (Edit domain.tld to reflect your domain)
You can make up to 100 subdomain requests with using -d sub.domain.tld -d sub1.domain.tld


::

 cd /opt/letsencrypt
 ./letsencrypt-auto --config /etc/letsencrypt/configs/domain.tld.conf certonly
 Should output:
 - Congratulations! And a paragraph about the keys made and where the live.


**Edit sites-available**  (Edit domain.tld to reflect your domain)

::

 Comment out and add
 vim  /etc/nginx/sites-available/fusionpbx
        #ssl_certificate         /etc/ssl/certs/nginx.crt;
        #ssl_certificate_key     /etc/ssl/private/nginx.key;
        ssl_certificate /etc/letsencrypt/live/domain.tld/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/domain.tld/privkey.pem;

Systemctl restart nginx

**Auto Renew certificate** 

::

 cd /etc/fusionpbx/
 touch renew-letsencrypt.sh
 Put code example from "Automating Renewal" section from https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx into renew-letsencrypt.sh
 Edit the my-domain.conf with the domain name you used a few steps earlier
 Create crontab -e
 0 0 1 JAN,MAR,MAY,JUL,SEP,NOV * /path/to/renew-letsencrypt.sh
 This executes every two months

chmod +x renew-letsencrypt.sh

Now check the padlock and see if it's green!

Setup for multiple domains on Let's Encrypt
===========================================

Before setting up multiple domains, make sure you have SSL working on your main domain using the instructions above.

**Create shared nginx host file for all domains**

``vim /etc/nginx/includes/fusionpbx-default-config``
 
Paste the code below into the file

::

 ssl_protocols           TLSv1 TLSv1.1 TLSv1.2;
 ssl_ciphers             HIGH:!ADH:!MD5:!aNULL;

 #letsencrypt
 location /.well-known/acme-challenge {
   root /var/www/letsencrypt;
 }

 #REST api
 if ($uri ~* ^.*/api/.*$) {
   rewrite ^(.*)/api/(.*)$ $1/api/index.php?rewrite_uri=$2 last;
   break;
 }

 #algo
 rewrite "^.*/provision/algom([A-Fa-f0-9]{12})\.conf" /app/provision/?mac=$1&file=algom%7b%24mac%7d.conf last;

 #mitel
 rewrite "^.*/provision/MN_([A-Fa-f0-9]{12})\.cfg" /app/provision/index.php?mac=$1&file=MN_%7b%24mac%7d.cfg last;
 rewrite "^.*/provision/MN_Generic.cfg" /app/provision/index.php?mac=08000f000000&file=MN_Generic.cfg last;

 #grandstriam
 rewrite "^.*/provision/cfg([A-Fa-f0-9]{12})(\.(xml|cfg))?$" /app/provision/?mac=$1;

 #aastra
 rewrite "^.*/provision/aastra.cfg$" /app/provision/?mac=$1&file=aastra.cfg;
 #rewrite "^.*/provision/([A-Fa-f0-9]{12})(\.(cfg))?$" /app/provision/?mac=$1 last;

 #yealink common
 rewrite "^.*/provision/(y[0-9]{12})(\.cfg)?$" /app/provision/index.php?file=$1.cfg;

 #yealink mac
 rewrite "^.*/provision/([A-Fa-f0-9]{12})(\.(xml|cfg))?$" /app/provision/index.php?mac=$1 last;

 #polycom
 rewrite "^.*/provision/000000000000.cfg$" "/app/provision/?mac=$1&file={%24mac}.cfg";
 #rewrite "^.*/provision/sip_330(\.(ld))$" /includes/firmware/sip_330.$2;
 rewrite "^.*/provision/features.cfg$" /app/provision/?mac=$1&file=features.cfg;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-sip.cfg$" /app/provision/?mac=$1&file=sip.cfg;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-phone.cfg$" /app/provision/?mac=$1;
 rewrite "^.*/provision/([A-Fa-f0-9]{12})-registration.cfg$" "/app/provision/?mac=$1&file={%24mac}-registration.cfg";

 #cisco
 rewrite "^.*/provision/file/(.*\.(xml|cfg))" /app/provision/?file=$1 last;

 #Escene
 rewrite "^.*/provision/([0-9]{1,11})_Extern.xml$"       "/app/provision/?ext=$1&file={%24mac}_extern.xml" last;
 rewrite "^.*/provision/([0-9]{1,11})_Phonebook.xml$"    "/app/provision/?ext=$1&file={%24mac}_phonebook.xml" last;

 access_log /var/log/nginx/access.log;
 error_log /var/log/nginx/error.log;

 client_max_body_size 80M;
 client_body_buffer_size 128k;

 location / {
   root /var/www/fusionpbx;
   index index.php;
 }

 location ~ \.php$ {
   fastcgi_pass unix:/var/run/php/php7.1-fpm.sock;
   #fastcgi_pass 127.0.0.1:9000;
   fastcgi_index index.php;
   include fastcgi_params;
   fastcgi_param   SCRIPT_FILENAME /var/www/fusionpbx$fastcgi_script_name;
 }

 # Disable viewing .htaccess & .htpassword & .db
 location ~ .htaccess {
   deny all;
 }
 location ~ .htpassword {
   deny all;
 }
 location ~^.+.(db)$ {
   deny all;
 }


**Create a file to contain config for additional domains**

``touch /etc/nginx/includes/fusionpbx-domains``


**make default file read configs for additional domains**

``vim /etc/nginx/sites-available/fusionpbx``


Add the line below at the very end of the file after the trailing "}"

``include /etc/nginx/includes/fusionpbx-domains;``


By now you are all set to start using SSL on multiple domains for your FusionPBX installation.


**Follow the steps below everytime your add a new domain**

Create a conf file for the new domain (repalce example.com with your own domain)

``vim /etc/letsencrypt/configs/example.com.conf``


Paste this into the .conf file (don't forget to change the defaults, especially the domain)

::

 # the domain we want to get the cert for;
 # technically it's possible to have multiple of this lines, but it only worked
 # with one domain for me, another one only got one cert, so I would recommend
 # separate config files per domain.
 domains = my-domain

 # increase key size
 rsa-key-size = 2048 # Or 4096

 # the current closed beta (as of 2015-Nov-07) is using this server
 server = https://acme-v01.api.letsencrypt.org/directory

 # this address will receive renewal reminders
 email = my-email

 # turn off the ncurses UI, we want this to be run as a cronjob
 text = True

 # authenticate by placing a file in the webroot (under .well-known/acme-upatechallenge/)
 # and then letting LE fetch it
 authenticator = webroot
 webroot-path = /var/www/letsencrypt/


Obtain the cert from Let's Encrypt (again, replce example.com with your domain)

::

 cd /opt/letsencrypt
 ./letsencrypt-auto --config /etc/letsencrypt/configs/example.com.conf certonly


**Set cert to auto renew with other domains**

::

 cd /etc/fusionpbx
 vim renew-letsencrypt.sh
 
 
Add the line below right below where it says "cd /opt/letsencrypt/" (again replace example.com with your domain)

``./certbot-auto --config /etc/letsencrypt/configs/example.com.conf certonly --non-interactive --keep-until-expiring --agree-tos --quiet``


Finally add your new domain to be loaded

``vim /etc/nginx/includes/fusionpbx-domains``


Paste the below at the very end of the file (again replace example.com with your domain)

::

 server {
         listen 443;
         server_name example.com;
         ssl                     on;
         ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
         ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

         include /etc/nginx/includes/fusionpbx-default-config;
 }
 
 
You're all set! Restart nginx for changes to take effect
 
 ``service nginx restart``


.. _link: https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx
.. _Verto Communicator: https://freeswitch.org/confluence/display/FREESWITCH/Verto+Communicator



