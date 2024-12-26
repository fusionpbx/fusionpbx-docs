##########
Command
##########

Provides a conventient way to execute system, PHP, switch and SQL commands. 

.. image:: ../_static/images/fusionpbx_command.jpg
        :scale: 85%



*  Click the **drop down box** on the right to choose from **Switch**, **PHP**, Shell and SQL to execute commands.


Install
--------

::

 cd /var/www/fusionpbx/app
 git clone https://github.com/fusionpbx/fusionpbx-app-command.git command
 chown -R www-data:www-data /var/www/fusionpbx/app/command

- Run Advanced > Upgrade > Menu Defaults
- Run Advanced > Upgrade > Permission Defaults
- Log out and then Log back in

Upgrade
--------

::

- cd /var/www/fusionpbx/app/command
- git pull
