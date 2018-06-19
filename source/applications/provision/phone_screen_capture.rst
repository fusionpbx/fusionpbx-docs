Phone Screen Capture
^^^^^^^^^^^^^^^^^^^^^

Snom
=====

In order to show the content of the phone display on a computer you need to enter the following URL in a browser: 

::

 http://[phoneIP]/screen.bmp

This feature is working on all snom desktop phones. For snom 300 this feature is available in version 8.7.3.7 and later.  

Cisco/Linksys SPA 50x and SPA 30x
==================================

1. Direct your browser to: http://IP_address_of_phone/admin/screendump.bmp

2. Use the browser to save the file as: anyname.bmp 

::
 
 You now have a 128x64 pixel screen shot in BMP format of you phone's display.
  

Polycom
=========

Since SIP 3.2.0 you can capture the current screen on a SoundPoint IP, SoundStation IP orVVX phone through the web interface to the phone.


In order to utilize this facility the Parameter

::
 
 <up up.screenCapture.enabled="1" /> 
 above needs to be added to the Configuration via the Provisioning Server.



Username: Polycom

Password: 456


This does not automatically allow a User to capture the Screen, the functionality needs to be activated by the Phone User.


Note: You need to re-enable the Screen Capture feature after every phone restart or reboot (repeat below).


Press the Menu Key

Select Settings

Select Basic

Select Preferences

Scroll down and select Screen Capture

Enable or disable the Functionality.

As the browser address, enter http://<phone’s IP address>/captureScreen .

The current screen that is shown on the phone is shown in the browser window. The image can be saved as a file.

Please consult your Admin Guide matching your SIP / UC Software Version. 

Yealink
=========

1. Yealink SIP phone with V73 or higher version

2. Login on the WEB interface and fill the *Action URI allow IP List* (path: Features > Remote Control > Action URI allow IP List) with *any* or *IP address or your PC*, then click *Confirm*.

1.png

3. In the Brower, fill *http://PhoneIP/screencapture* in the address bar (Phone IP is the IP address of your phone), then press *Enter* key.

.. image:: http://support.yealink.com/upload/image/20150513/1431509282172062831.png
        :scale: 85%



4. In the first time, for security consideration, the phone will display a message *Allow remote control*. Please press *OK*. Then repeat step 3.

5. You will get the screen capture of the phone as below:


.. image:: http://support.yealink.com/upload/image/20150513/1431509312543075406.png
        :scale: 85%




Product Models
^^^^^^^^^^^^^^^^^^^^^

SIP-T48G , SIP-T46G , SIP-T42G , SIP-T41P , SIP-T29G , SIP-T28P , SIP-T27P , SIP-T26P , SIP-T23G , SIP-T23P , SIP-T22P , SIP-T21P E2
