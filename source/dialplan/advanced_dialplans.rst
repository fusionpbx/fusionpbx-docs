####################
Advanced Dialplans
####################

FusionPBX installs several default dialplans. FusionPBX also gives the option to make new dialplans. This gives you the power for more advanced functions, and produce the desired result.    




Adding a Dialplan
^^^^^^^^^^^^^^^^^^^

You can create a new dialplan or copy and modify an existing dialplan.

* Go to Dialplan > Dialplan Manager

* Click the **ADD** icon at the top right.

.. image:: ../_static/images/dialplan/fusionpbx_dialplan_advanced1.png
        :scale: 60%

* Complete required fields and click save.

.. image:: ../_static/images/dialplan/fusionpbx_dialplan_advanced2.png
        :scale: 60%


Edit a Dialplan
^^^^^^^^^^^^^^^^^

Find the dialplan you want to edit and click the edit icon.

.. image:: ../_static/images/dialplan/fusionpbx_dialplan_advanced3.png
        :scale: 60%

Once you enter data into the empty fields at the bottom and click save, more blank fileds will populate if needed.

.. image:: ../_static/images/dialplan/fusionpbx_dialplan_advanced4.png
        :scale: 60%


Enable a Dialplan Destination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dialplans that have a value in the **Number** filed can be enabled and used in `Dialplan > Destinations <../dialplan/destinations.html>`_. Setting the **destination** field to **True** will enable the dialplan to be visable and used as an action in `Dialplan > Destinations <../dialplan/destinations.html>`_.

.. image:: ../_static/images/dialplan/fusionpbx_dialplan_advanced5.png
        :scale: 60%

Cross Tenant Calling
~~~~~~~~~~~~~~~~~~~~~~

This would require a prefix of 5 followed by 4 digit extensions. The prefix can be any number that you choose to use and the 4 digit extension must match the destination tenant. So if the destination extensions are 3 digit then you would use 3 instead of 4.

+-----------+---------------------------+------------------------------------------+-------+--------+-------+-------+
| Tag       | Type                      | Data                                     | Break | Inline | Group | Order |
+===========+===========================+==========================================+=======+========+=======+=======+
| condition | ${destination_number}     | ^5(\d{4})$                               |       |        |       | 5     |
+-----------+---------------------------+------------------------------------------+-------+--------+-------+-------+
| action    | set                       | domain_name=customer.domain.tld          |       | True   |       | 10    |
+-----------+---------------------------+------------------------------------------+-------+--------+-------+-------+
| action    | set                       | domain_uuid=correct-uuid-for-the-domain  |       | True   |       | 15    |
+-----------+---------------------------+------------------------------------------+-------+--------+-------+-------+
| action    | transfer                  | $1 XML ${domain_name}                    |       |        |       | 20    |
+-----------+---------------------------+------------------------------------------+-------+--------+-------+-------+

* Be sure to set the **Continue dropdown box True**

* Finally we have the desired dialplan to call from tenant A to tenant B.


.. image:: ../_static/images/dialplan/fusionpbx_custom_dialplan.jpg
        :scale: 85%




.. note::
      A quick way to find a domains uuid is by going to Advanced > Domains.  Then click the edit icon on the domain you want to know the uuid of.  The uuid will be at the end of the url.



