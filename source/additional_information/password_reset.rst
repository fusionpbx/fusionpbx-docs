##############
Password Reset
##############


The steps below are outdated but useful for older installations. `Click here for the new youtube video on password recovery. <https://youtu.be/YrlfscQ_3ew>`_ 

| Here some rough steps to change the password of the database. The password can only be changed and not recovered.

|

| The database contains a table called **v_users** which contains the username, password and salt. The password is the md5 hash of the password and the salt. 

**Password Hash**
^^^^^^^^^^^^^^^^^

| Use the following commands to generate the password hash. Don't forget to provide your own salt and password.

::

 echo '<?php $salt = "random-salt-goes-here";$password = "put your password here"; echo md5($salt.$password)."\n"; ?>' > /tmp   /test.php


| Run the php file from command line.

::

 php /tmp/test.php


**SQLite**
^^^^^^^^^^^

| Install sqlite3 which can be be used to modify the database fusionpbx.db. Then open the database with the following:
 
::

 sqlite3 fusionpbx.db

**PostgreSQL**
^^^^^^^^^^^^^^^

| Connect to the PostgreSQL database. Once you are running psql you can use:

* \\l to list the databases.
* \\c to connect to one of them.
* After running the SQL Query then use \q to quit.

::

 su postgres
 psql
 \c fusionpbx


**Change the Password**
^^^^^^^^^^^^^^^^^^^^^^^^

The hashed password and the salt can be updated using the command:

::

 update v_users set password = 'replace-with-password-hash-from-php-script', salt = 'replace-with-your-random-salt' where       username = 'superadmin';
 
 
