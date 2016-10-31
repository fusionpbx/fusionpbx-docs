Let's Encrypt
==============

Let's Encrypt is one of the most recent and widely used form of free SSL security but doesn't support wildcard DNS.  You can use Let's Encrypt with your FusionPBX install and WebRTC like `Verto Communicator`_.

More info on NGINX with Let's Encrypt
https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx

**Clone Let's Encrypt**

::

 cd /usr/src/
 git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt

**Execute certbot-auto**

::

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

 Vim  /etc/nginx/sites-available/fusionpbx
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

::

 cd /opt/letsencrypt
 ./letsencrypt-auto --config /etc/letsencrypt/configs/domain.tld.conf certonly
 Should output:
 - Congratulations! And a paragraph about the keys made and where the live.


**Edit sites-available**  (Edit domain.tld to reflect your domain)

::

 Comment out and add
 Vim  /etc/nginx/sites-available/fusionpbx
        #ssl_certificate         /etc/ssl/certs/nginx.crt;
        #ssl_certificate_key     /etc/ssl/private/nginx.key;
        ssl_certificate /etc/letsencrypt/live/domain.tld/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/domain.tld/privkey.pem;

**Auto Renew certificate**

::

 cd /etc/fusionpbx/
 touch renew-letsencrypt.sh
 Put code example from Automating Renewal section step#1 into renew-letsencrypt.sh
 Edit the my-domain.conf with the domain name you used a few steps earlier
 Create crontab -e
 0 0 1 JAN,MAR,MAY,JUL,SEP,NOV * /path/to/renew-letsencrypt.sh
 This executes every two months

Now check the padlock and see if it's green!


.. _link: https://www.nginx.com/blog/free-certificates-lets-encrypt-and-nginx
.. _Verto Communicator: https://freeswitch.org/confluence/display/FREESWITCH/Verto+Communicator



