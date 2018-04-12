########
WebRTC
########

WebRTC app for FusionPBX is made by editing an existing FusionPBX app code and adding the code from the "Master FreeSWITCH code example".  Also, keep in mind that you will need ssl certs working on the server.

.. image:: ../_static/images/fusionpbx_webrtc.jpg
        :scale: 85%

.. Note::

 There are two "sets" of code in this app. One being an existing app from FusionPBX and the code example from `Master FreeSWITCH book`_ in Chapter 8.

Prerequisites
^^^^^^^^^^^^^^

* Working install of FusionPBX
* Working set of SSL certs (Not self signed) on said install of FusionPBX
* Working mod_verto setup.
* Patience


Install Steps
^^^^^^^^^^^^^^

On your server

::

  cd /usr/src
  git clone https://github.com/fusionpbx/fusionpbx-apps
  Move the directory 'webrtc' into your main FusionPBX directory
  mv fusionpbx-apps/webrtc /var/www/fusionpbx/app
  chown -R www-data:www-data /var/www/fusionpbx/app/webrtc

::

 Log into the FusionPBX webpage
 Advanced -> Upgrade
 Menu Defaults and Permission Defaults.
 Log out and back in.


.. _Master FreeSWITCH book: https://www.packtpub.com/networking-and-servers/mastering-freeswitch
