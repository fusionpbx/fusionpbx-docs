************
Ring Group
************

|

A ring group is a set of destinations that can be called with a ring strategy.

To add a ring group click the plus. `Click for the youtube video <https://youtu.be/sULuuLOSvLQ>`_ .

.. image:: ../_static/images/fusionpbx_ring_group.jpg
        :scale: 85%


*  **Name** Simply the meaningful name of the Ring group (shows after the Extension in menu selections).
*  **Extension** The Dial-able extension for this group standard config states as a 2-7 number extension.
*  **Strategy** The selectable way in which the destinations are being used.
*      **Simultaneous** Rings all defined Destinations.
*      **Sequence**  Where order that is lower goes first.
*      **Enterprise** Works with follow me.
*      **Rollover** calls destinations in sequence and skips busy destinations.
*      **Random** A random destination will ring.
*  **Destinations** The extensions that this ring group applies to.
*  **Prompt** Where you determine if the call must have a dial to confirm before a pickup event.
*  **CID Name Prefix** The string that is added to the caller ID when it displays on the ringing extension.
*  **CID Number Prefix** The **Number** that is added to the caller ID when it displays on the ringing extension.
*  **Ring Back** What the caller hears when they are waiting for the **Destinations** to answer.
*  **Context** The grouping that this ring group will search as specified in the configuration of your Extensions (if this excludes an extension it will not ring)

.. image:: ../_static/images/fusionpbx_ring_group1.jpg
        :scale: 85%


Ring Group Example
~~~~~~~~~~~~~~~~~~~~

In our example we will have 4 extensions all ring at the same time until one of them pick up first.  Click the + to create a ring group.  Fill in the fields that are in **bold**.  In the Extension box type a number that is **NOT** allready created.  This new extention won't be in the extension list.  The strategy will be Simultaneous. Enter in the destination the 4 extensions 1001, 1002, 1003, 1004.


.. image:: ../_static/images/fusionpbx_ring_group2.jpg
        :scale: 85%

