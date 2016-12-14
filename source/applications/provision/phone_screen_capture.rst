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

1. Direct your broswer to: http://IP_address_of_phone/admin/screendump.bmp

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
