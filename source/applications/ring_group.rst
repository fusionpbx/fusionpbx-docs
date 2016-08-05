***********
Ring Groups
***********

|

A ring group is a set of destinations that can be called with a ring strategy.

To add a ring group click the plus.

.. image:: ../_static/images/fusionpbx_ring_group.jpg
        :scale: 85%


*  **Name** Simply the meaningful name of the Ring group (shows after the Extension in menu selections).
*  **Extension** The Dial-able extension for this group standard config states as a 2-7 number extension.
*  **Strategy** The selectable way in which the destinations are being used.
-      **Simultaneous** Rings all defined Destinations.
-      **Sequence**  Where order that is lower goes first.
-      **Enterprise** Works with follow me.
-      **Rollover** calls destinations in sequence and skips busy destinations.
-      **Random** A random destination will ring.
*  **Destinations** The extensions that this ring group applies to.
*  **Prompt** Where you determine if the call must have a dial to confirm before a pickup event.
*  **CID Name Prefix** The string that is added to the caller ID when it displays on the ringing extension.
*  **CID Number Prefix** The **Number** that is added to the caller ID when it displays on the ringing extension.
*  **Ring Back** What the caller hears when they are waiting for the **Destinations** to answer.
*  **Context** The grouping that this ring group will search as specified in the configuration of your Extensions (if this excludes an extension it will not ring)

.. image:: ../_static/images/fusionpbx_ring_group1.jpg
        :scale: 85%

