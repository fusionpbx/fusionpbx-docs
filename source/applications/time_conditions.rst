*****************
Time Conditions
*****************

|

Dynamically route calls to an IVR menu, external numbers, scripts, or other destinations based on time conditions.  Fields in **bold** are mandatory.


*  **Name** Name of the Time Condition.
*  **Extension** Define an extension number that is NOT allready created.
*  Presets US Holiday presets.
*  Alternate Destination If the condition doesnt match the call will goto the defined alternate destination.
*  **Order** Changes the order of which condition is evaluated first.
*  **Enabled**  If the ring group is enabled.

.. image:: ../_static/images/fusionpbx_time_conditions.jpg
        :scale: 85%


Time Conditions Example
~~~~~~~~~~~~~~~~~~~~~~~~

In our example we have an employee that will receive calls during a set time range and set days.  Below is what the settings look like for Monday through Friday at 5:00pm to 11:00pm.  If the employee doesnt answer the call will be directed to the **Timeout Destination**.  Label the **Name as Oncall** and invent the **Extension as 10011**.  In the **Settings** choose from the dropdown lists for *Day of Week* for the condition, *Monday* for the Value and *Friday* for the Range. Next set of dropdown list choose *Time of Day* for the condition, *5:00 PM* for the value and *11:00 PM* for the Range.  If other options are needed just click the + to the right of Range. 

|

.. image:: ../_static/images/fusionpbx_time_conditions1.jpg
        :scale: 85%

|  

The next dropdown choose the extension where the call is intended for.  If the call is outside the date and time specified the call will goto the **Alternate Destination** dropdown.  Be sure **Enabled** is set *True* and click save.

|

.. image:: ../_static/images/fusionpbx_time_conditions2.jpg
        :scale: 85%
