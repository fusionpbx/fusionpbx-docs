###################
Freeswitch install
###################

|

| **Upgrade Move Source**

::

 mv /usr/src/freeswitch freeswitch-version

| **Git Release**

::

 cd /usr/src
 git clone -b v1.4 https://freeswitch.org/stash/scm/fs/freeswitch.git
 cd freeswitch
 ./bootstrap.sh

| or

| **Git Head**

::

 cd /usr/src
 git clone https://freeswitch.org/stash/scm/fs/freeswitch.git
 cd freeswitch
 ./bootstrap.sh

| or

| **files.freeswitch.org**

::

 cd /usr/src
 wget http://files.freeswitch.org/freeswitch-1.4.26.zip
 unzip freeswitch-1.4.26.zip
 cd freeswitch-1.4.26

| **Ubuntu Dependencies**

::

 apt-get install autoconf automake devscripts gawk g++ git-core libjpeg-dev libncurses5-dev libtool make python-dev gawk pkg-config libtiff-dev libperl-dev libgdbm-dev libdb-dev gettext libssl-dev libcurl4-openssl-dev libpcre3-dev libspeex-dev libspeexdsp-dev libsqlite3-dev libedit-dev libldns-dev libpq-dev memcached libmemcached-dev

| **Debian Dependencies**

::

 apt-get install autoconf automake devscripts gawk g++ git-core libjpeg-dev libncurses5-dev libtool libtool-bin make python-dev gawk pkg-config libtiff5-dev libperl-dev libgdbm-dev libdb-dev gettext libssl-dev libcurl4-openssl-dev libpcre3-dev libspeex-dev libspeexdsp-dev libsqlite3-dev libedit-dev libldns-dev libpq-dev memcached libmemcached-dev

| **CentOS**

::

 yum install git gcc-c++ autoconf automake libtool wget python ncurses-devel zlib-devel libjpeg-devel openssl-devel e2fsprogs-devel sqlite-devel libcurl-devel pcre-devel speex-devel ldns-devel libedit-devel libmemcached-devel

| Configure services to auto start

::

 chkconfig --add memcached && chkconfig --levels 33 memcached on
 chkconfig --add freeswitch && chkconfig --levels 35 freeswitch on

| **modules.conf**

| uncomment the FreeSWITCH modules that are needed.

::

 mod_avmd
 mod_callcenter
 mod_memcache
 mod_cidlookup
 mod_curl

| Used for MP3 support

::

 mod_shout

| **Postgres driver**

::

 ./configure --enable-core-pgsql-support

| **Run Make**

 make

| **Remove FreeSWITCH files**

| This step is only needed for a FreeSWITCH upgrade. 
| Once it has been confirmed that the compile was successful then remove files from previous version of FreeSWITCH
 
::
 
 rm -rf /usr/local/freeswitch/{lib,mod,bin}/*
 

| **Install**

::

 make install

| **File Permissions**

| Set the file permissions instructions may vary based on the OS and install directory.


| Debian and Ubuntu

::

 chown -R www-data:www-data /usr/local/freeswitch
 
 
