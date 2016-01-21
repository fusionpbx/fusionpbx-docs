************
Extensions
************

|
|

Welcome to the adding Extensions section.  Here you will find how to add Extensions. 

|
|


Goto **Accounts** then click **Extensions**

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153364/86f061b8-b487-11e5-8667-5a753994a3b9.jpg

|
|


Then click the

 .. image:: https://cloud.githubusercontent.com/assets/13131198/11783217/fbb7a2e6-a243-11e5-9c06-e3a55882ea51.png

on the right.

|


.. image:: https://cloud.githubusercontent.com/assets/13131198/12153359/86e7c814-b487-11e5-91ef-c1a1d89198c5.jpg

|
|

Enter the desired *extension* starting number.  From the dropdown *Range* box you can choose the desired block of extensions to start with. This can be done again later if needing more extensions.  Click **save** once entry is completed.  Entry can be customized for each idividual extension after this point.

|
|

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153358/86e71cd4-b487-11e5-8e46-4d78dd358db1.jpg

|
|




We now have extensions. Each extension has and edit icon beside it.  Click the edit icon

|
|

 .. image:: https://cloud.githubusercontent.com/assets/13131198/12153361/86eba8b2-b487-11e5-9e81-c6bac7fa355b.jpg

to customize internal, external, emergency caller id and other fine tuned options.  You can also access **Call Control** from here. 



|
|


.. image:: https://cloud.githubusercontent.com/assets/13131198/12153360/86ea9db4-b487-11e5-8b6a-2c6bf8768e74.jpg

|
|




Enter information as needed.

|

- **Extenson:** This is the extension number or name if used with Number Alias
- **Number Alias:** Number extension if extension is a name
- **Password:** mouse over to see the password
- **User List:** Add a user for this extesnion to login to the FusionPBX GUI interface
- **Voicemail Password:** Password for this extensions voicemail
- **Device Provisioning:** Used for hardware devices like voip phones and ata's
- **Account Code:** Can be used for billing
- **Effective Caller ID Name:** Used for internal caller id
- **Effective Caller ID Number:** Used for internal caller id
- **Outbound Caller ID Name:** Used for external (public) caller id
- **Outbound Caller ID Number:** Used for external (public) caller id
- **Emergency Caller ID Name:** Can be set to a national standard or local emergency entity
- **Emergency Caller ID Number:** Can be set to a national standard or local emergency entity

.. image:: https://cloud.githubusercontent.com/assets/13131198/12153357/86e5a980-b487-11e5-81ad-2944bff0f0bf.jpg

|
|



************
Registering Phones
************

|
|

Welcome to the Registering Phones section.  Here you will find how to configure some of the most popular phones to use with FusionPBX. 

|

Use this to configure your SIP extensions.

|

Grandstream
============

.. image:: https://cloud.githubusercontent.com/assets/13131198/12453792/d9aa7b2e-bf62-11e5-9ddd-30ad751e9ce8.jpg

|

Registering an **Extension** using a hardware phone or adapter (ata) using Grandstream. 

|

Granstream is one of the common brand of phone and adapters for voip.  From call centers to offices and home offices Grandstream products can be found.  Grandstream has a large selection of hardware from phones, video phones to analog telephone adapters.

|

In our example we will register an analog telephone adapter (ata) model HT701.

|

1. Goto the device ip address. The default password should be admin. Enter admin and click login

.. image:: https://cloud.githubusercontent.com/assets/13131198/12453076/8dc6fbcc-bf5f-11e5-89bc-56bcb1bc2d00.jpg

|

2. Click on the **FXS PORT** tab on the top right.

| ``Primary Sip Server: subdomain.domain.com``
| ``Failover SIP Server: subdomain1.domain.com (this can be left blank or can use Primary if only 1 sip server)``
| ``SIP User ID: 1000``
| ``Authenticated Password: thepassword``

|

Click **Update** then click **Apply** at the bottom

|

.. image:: https://cloud.githubusercontent.com/assets/13131198/12453075/8dc38cf8-bf5f-11e5-9e41-606241e41379.jpg

|

3. Click the **Status** tab on the top left.  You should see the *Registration* as **Registered** and the *User ID* **1000**

.. image:: https://cloud.githubusercontent.com/assets/13131198/12453074/8dc0ce6e-bf5f-11e5-8f78-95473e500900.jpg

|

- Troubleshooting tips

|

* Check, double check that the correct extension number and password is being used.
* Reboot the device.
* Check Fail2ban and see if the ip got blocked.
* Make sure you have created an DNS A record for the domain being used and there are no typos
* Nat, firewalls and router settings.  Some brands of routers can cause issues.  Google the make and model of router or firewall appliance for common settings or remedies.
* Visit Grandstream Supoprt http://www.grandstream.com/support
|
|

Zoiper
=======

|
|

Registering an **Extension** using the softphone Zoiper.

|

In the ever changing world of voip businesses are moving away from hardware phones.  From call centers to home offices Zoiper and many other softphones make use of software for communication needs for not only voice but video and faxing. This example will show how to register an extension using Zoiper for Windows. *Note* Zoiper can be used on several operating systems and mobile devices.

|
1. Download the software. .. Zoiper: http://www.zoiper.com/
2. Install the software.
3. If the software isn't open click the Zoiper icon to open from the desktop or start menu.


.. image:: https://cloud.githubusercontent.com/assets/13131198/12450587/b9878e46-bf52-11e5-99bb-8744091d62c8.jpg

|

4. Click on **Settings**

.. image:: https://cloud.githubusercontent.com/assets/13131198/12450588/b98939da-bf52-11e5-807d-bd29b612671b.jpg

|

5. Click on **Preferences**

.. image:: https://cloud.githubusercontent.com/assets/13131198/12450591/b98e0366-bf52-11e5-8633-b4079385940b.jpg

|

6. Click on **Create account**

.. image:: https://cloud.githubusercontent.com/assets/13131198/12450589/b98abf76-bf52-11e5-9f57-e77adabd3ea8.jpg

|

7. Enter the user, password and domain name.

| ``user: 1000``
| ``password: thepassword``
| ``domain: sub.domain.com``

|

.. image:: https://cloud.githubusercontent.com/assets/13131198/12450590/b98d9552-bf52-11e5-9e46-650e8bc846b1.jpg

|

8. Click ok.  You should have **Registered** at the top right

.. image:: https://cloud.githubusercontent.com/assets/13131198/12450586/b986d690-bf52-11e5-892d-7eb5e96d44a3.jpg

|

- Troubleshooting tips

|

* Check, double check that the correct extension number and password is being used.
* Check Fail2ban and see if the ip got blocked.
* Make sure you have created an DNS A record for the domain being used and there are no typos
* Nat, firewalls and router settings.  Some brands of routers can cause issues.  Google the make and model of router or firewall appliance for common settings or remedies.
* Visit Zoiper Community Supoprt http://community.zoiper.com/
|
|






.. toctree::
  :maxdepth: 3
  :glob:

  Extensions-IVR/Extensions.rst
