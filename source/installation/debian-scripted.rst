*************************
Debian - Scripted Install
*************************

.. note::

  This is currently the **recommended** installation method.


Requirements
------------

Software
~~~~~~~~

* **Database** : PostgreSQL 9.x / SQLite *(PostgreSQL recommended)*
* **Web Server** : nginx / apache *(nginx recommended)*
* **PHP** : 5.x *(Version 5.5 recommended)*
* **FreeSWITCH** : 1.4.x * *(Version 1.4.26 recommended)*

Hardware
~~~~~~~~


* **RAM** : 512MB *(1GB+ recommended)*
* **DISK** : 10GB *(20GB+ recommended)*
* **CPU** : Single core 2266 MHz *(Dual core 2266 MHz+ recommended)*



Installation Guide
------------------

# 1 - Debian ISO Download
~~~~~~~~~~~~~~~~~~~~~~~~~

`Download <http://www.debian.org/distrib/netinst>`_ Debian Jessie net install ISO 

# 2 - nginx Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Sample contents of ``nginx.conf``

.. code-block:: nginx

  user www www;
  worker_processes  2;
  
  events {
      worker_connections  1024;
      multi_accept on;
  }
  
  
  http {
      server_names_hash_bucket_size 64;
      include       mime.types;
      default_type text/html;
      server_tokens off;
      sendfile        on;
      tcp_nopush     on;
      add_header rt-Fastcgi-Cache $upstream_cache_status;
      keepalive_timeout  20;
      client_header_timeout 20;
      client_body_timeout 20;
      reset_timedout_connection on;
      send_timeout 20;
      open_file_cache max=10000 inactive=1m;
      open_file_cache_valid    2m;
      open_file_cache_min_uses 1;
      open_file_cache_errors   on;
      client_max_body_size 40m;
  
      gzip  on;
      gzip_vary on;
      gzip_min_length 1100;
      gzip_buffers    16 8k;
      gzip_types text/css text/x-component application/json application/x-javascript  application/javascript text/javascript text/x-js text/richtext image/svg+xml   text/plain text/xsd text/xsl text/xml image/x-icon;
      gzip_proxied  any;
      gzip_comp_level 4;
      gzip_disable “MSIE [1-6].(?!.*SV1)”;
      ignore_invalid_headers  on;
  
       include /opt/local/etc/nginx/sites-enabled/*;
       }

