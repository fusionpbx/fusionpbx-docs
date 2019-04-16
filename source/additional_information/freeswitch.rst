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
 git clone -b v1.6 https://freeswitch.org/stash/scm/fs/freeswitch.git
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
 
 1.4.x is considered EOL use the steps below for 1.6.x
 
 cd /usr/src
 wget http://files.freeswitch.org/freeswitch-1.6.20.zip
 unzip freeswitch-1.6.20.zip
 cd freeswitch-1.6.20

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
 mod_translate

| Used for MP3 support

::

 mod_shout

| **Postgres driver**

::

 ./configure --enable-core-pgsql-support

| **Run Make**

::

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
 
 


| CentOS or Other Unix operating systems
| (need make sure that the web server has access to IVR recordings, Fax, and Voicemail)

::

 adduser --disabled-password  --quiet --system --home /usr/local/freeswitch --gecos "FreeSWITCH Voice Platform" --ingroup daemon freeswitch
 chown -R freeswitch:daemon /usr/local/freeswitch/ 
 chmod -R o-rwx /usr/local/freeswitch/


| **Install Sound Files**

| Run this on new installs.

::

 cd /usr/src/freeswitch
 make sounds-install moh-install
 make hd-sounds-install hd-moh-install
 make cd-sounds-install cd-moh-install

**Startup Script**

| Run on new install only. Create the file '/etc/init.d/freeswitch' with the following code:

::

 #!/bin/bash
 ### BEGIN INIT INFO
 # Provides:          freeswitch
 # Required-Start:    $local_fs $remote_fs
 # Required-Stop:     $local_fs $remote_fs
 # Default-Start:     2 3 4 5
 # Default-Stop:      0 1 6
 # Description:       Freeswitch debian init script.
 # Author:            Matthew Williams
 #
 ### END INIT INFO
 # Do NOT "set -e"
 
 # PATH should only include /usr/* if it runs after the mountnfs.sh script
 PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin
 DESC="Freeswitch"
 NAME=freeswitch
 DAEMON=/usr/local/freeswitch/bin/$NAME
 DAEMON_ARGS="-nc -nonat -reincarnate"
 PIDFILE=/usr/local/freeswitch/run/$NAME.pid
 SCRIPTNAME=/etc/init.d/$NAME

 FS_USER=www-data #freeswitch
 FS_GROUP=www-data #daemon

 # Exit if the package is not installed
 [ -x "$DAEMON" ] || exit 0
 
 # Read configuration variable file if it is present
 [ -r /etc/default/$NAME ] && . /etc/default/$NAME
 
 # Load the VERBOSE setting and other rcS variables
 . /lib/init/vars.sh
 
 # Define LSB log_* functions.
 # Depend on lsb-base (>= 3.0-6) to ensure that this file is present.
 . /lib/lsb/init-functions
 
 #
 # Function that sets ulimit values for the daemon
 #
 do_setlimits() {
        ulimit -c unlimited
        ulimit -d unlimited
        ulimit -f unlimited
        ulimit -i unlimited
        ulimit -n 999999
        ulimit -q unlimited
        ulimit -u unlimited
        ulimit -v unlimited
        ulimit -x unlimited
        ulimit -s 240
        ulimit -l unlimited
        return 0
 }

 #
 # Function that starts the daemon/service
 #
 do_start()
 {
    # Set user to run as
        if [ $FS_USER ] ; then
      DAEMON_ARGS="`echo $DAEMON_ARGS` -u $FS_USER"
        fi
    # Set group to run as
        if [ $FS_GROUP ] ; then
          DAEMON_ARGS="`echo $DAEMON_ARGS` -g $FS_GROUP"
        fi

        # Return
        #   0 if daemon has been started
        #   1 if daemon was already running
        #   2 if daemon could not be started
        start-stop-daemon --start --quiet --pidfile $PIDFILE --exec $DAEMON --test > /dev/null -- \
                || return 1
        do_setlimits
        start-stop-daemon --start --quiet --pidfile $PIDFILE --exec $DAEMON --background -- \
                $DAEMON_ARGS \
                || return 2
        # Add code here, if necessary, that waits for the process to be ready
        # to handle requests from services started subsequently which depend
        # on this one.  As a last resort, sleep for some time.
 }
 
 #
 # Function that stops the daemon/service
 #
 do_stop()
 {
        # Return
        #   0 if daemon has been stopped
        #   1 if daemon was already stopped
        #   2 if daemon could not be stopped
        #   other if a failure occurred
        start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 --pidfile $PIDFILE --name $NAME
        RETVAL="$?"
        [ "$RETVAL" = 2 ] && return 2
        # Wait for children to finish too if this is a daemon that forks
        # and if the daemon is only ever run from this initscript.
        # If the above conditions are not satisfied then add some other code
        # that waits for the process to drop all resources that could be
        # needed by services started subsequently.  A last resort is to
        # sleep for some time.
        start-stop-daemon --stop --quiet --oknodo --retry=0/30/KILL/5 --exec $DAEMON
        [ "$?" = 2 ] && return 2
        # Many daemons don't delete their pidfiles when they exit.
        rm -f $PIDFILE
        return "$RETVAL"
 }
 
 #
 # Function that sends a SIGHUP to the daemon/service
 #
 do_reload() {
        #
        # If the daemon can reload its configuration without
        # restarting (for example, when it is sent a SIGHUP),
        # then implement that here.
        #
        start-stop-daemon --stop --signal 1 --quiet --pidfile $PIDFILE --name $NAME
        return 0
 }
 
 case "$1" in
  start)
        [ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
        do_start
        case "$?" in
                0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
        esac
        ;;
  stop)
        [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
        do_stop
        case "$?" in
                0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
        esac
        ;;
  status)
       status_of_proc -p $PIDFILE $DAEMON $NAME && exit 0 || exit $?
       ;;
  #reload|force-reload)
        #
        # If do_reload() is not implemented then leave this commented out
        # and leave 'force-reload' as an alias for 'restart'.
        #
        #log_daemon_msg "Reloading $DESC" "$NAME"
        #do_reload
        #log_end_msg $?
        #;;
  restart|force-reload)
        #
        # If the "reload" option is implemented then remove the
        # 'force-reload' alias
        #
        log_daemon_msg "Restarting $DESC" "$NAME"
        do_stop
        case "$?" in
          0|1)
                do_start
                case "$?" in
                        0) log_end_msg 0 ;;
                        1) log_end_msg 1 ;; # Old process is still running
                        *) log_end_msg 1 ;; # Failed to start
                esac
                ;;
          *)
                # Failed to stop
                log_end_msg 1
                ;;
        esac
        ;;
  *)
        #echo "Usage: $SCRIPTNAME {start|stop|restart|reload|force-reload}" >&2
        echo "Usage: $SCRIPTNAME {start|stop|restart|force-reload}" >&2
        exit 3
        ;;
 esac
 
 exit 0


Make the script executable and make it auto start on system boot:

::

 chmod +x /etc/init.d/freeswitch
 update-rc.d freeswitch defaults

|


Monit
------

Used to monitor processes on UNIX systems.

http://mmonit.com/monit/ 


Install
^^^^^^^^^

::

 apt-get install monit

Edit Monit /etc/default/monit and set the "startup" variable to 1 in order to allow monit to start.

Configure
^^^^^^^^^^

Fail2Ban
~~~~~~~~~~

::
 
 cd /etc/monit.d
 touch fail2ban
 nano fail2ban

Add the following to the file and save it.

::

 check process fail2ban with pidfile /var/run/fail2ban/fail2ban.pid
  group services
  start program = "/etc/init.d/fail2ban start"
  stop  program = "/etc/init.d/fail2ban stop"
  if 5 restarts within 5 cycles then timeout

SIP
~~~~~

To monitor SIP from local or remote server

::

 cd /etc/monit.d
 touch sip
 nano sip

::

 check host fusionpbx with address your-ip
     if failed port 5060 protocol sip with target monit@monit:5060
         then alert
         
FreeSWITCH
~~~~~~~~~~~~

::

 cd /etc/monit/conf.d

or

::

 cd /etc/monit.d

 touch freeswitch
 nano freeswitch

Add the following

::
 #check process freeswitch with pidfile /usr/local/freeswitch/run/freeswitch.pid
 check process freeswitch with pidfile /run/freeswitch/freeswitch.pid
 start program = "/usr/bin/service freeswitch start"
 stop program  = "/usr/bin/service freeswitch stop"

or

::
 #check process freeswitch with pidfile /usr/local/freeswitch/run/freeswitch.pid
 #start program = "/usr/local/freeswitch/bin/./freeswitch -nc -u www-data"
 #stop program  = "/usr/local/freeswitch/bin/./freeswitch -stop"
 check process freeswitch with pidfile /run/freeswitch/freeswitch.pid
 start program = "/usr/bin/./freeswitch -nc -u www-data"
 stop program  = "/usr/bin/./freeswitch -stop"


Additional Options
~~~~~~~~~~~~~~~~~~~

::

 if 5 restarts within 5 cycles then timeout
 if cpu > 60% for 2 cycles then alert
 if cpu > 80% for 5 cycles then alert
 if totalmem > 2000.0 MB for 5 cycles then restart
 if children > 2500 then restart

Monit Daemon Add to the main monit config file.

::

 #monit daemon
 set httpd port 2812 and
 use address localhost
 allow localhost

Monit Commands
~~~~~~~~~~~~~~~

::

 monit -h
 monit status




