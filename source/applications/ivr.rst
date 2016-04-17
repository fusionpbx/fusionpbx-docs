************
IVR's
************

Welcome to the adding IVR section.  Here you will find how to add IVR's.

|
|

点击菜单 **Apps** 然后 **IVR Menu**

.. image:: ../_static/images/fusionpbx_ivr.jpg
        :scale: 85%

|
|

然后点击右边的

 .. image:: ../_static/images/plus.png
        :scale: 85%




.. image:: ../_static/images/fusionpbx_ivr1.jpg
        :scale: 85%

|
| *Options in* **bold** *are mandatory.*
| **Name:** 输入IVR名称
| **Extension:** Enter the extension number (This must a new extension that isn't allready created)
| **Greet Long:** The long greeting when entering the menu.
| Greet Short: The short greeting is played when returning to the menu.
| Options: Define caller options for the IVR menu.
| **Timeout:** The number of milliseconds to wait after playing the greeting or the confirm macro.
| Exit Action: Select the exit action to be performed if the ivr exists.
| **Direct Dial:** Define whether the callers can dial directly to registered extensions.
| Ring Back: Defines what the caller will hear while the destination is being called.
| Caller ID Name Prefix: Set a prefix on the caller ID name.
| Enabled: set the status of the IVR Menu.

|


.. image:: ../_static/images/fusionpbx_ivr2.jpg
        :scale: 85%

|

You can get very creative with IVR's and are almost limitless in possibilities. In the basic example below we **name** the IVR "IVR Main" , **Extension** "200" , **Greet Long** a phrase that was made from the **phrase section** under **apps** , entry in options for sales, billing, tech support, and after hours, made the **timeout** 3000 milliseconds, Exit Action to the extension 109 (after hours) , **Direct Dial** to False and Ring back to Default.

|


.. image:: ../_static/images/fusionpbx_ivr3.jpg
        :scale: 85%

|

You now have a list of IVR's to go back to and edit or delete as needed.

|


.. image:: ../_static/images/fusionpbx_ivr4.jpg
        :scale: 85%

|
|
