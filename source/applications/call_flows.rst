*****************
Call Flows
*****************

Direct calls between two destinations by calling a feature code.


.. image:: ../_static/images/fusionpbx_call_flow1.jpg
        :scale: 50%

|
|

*  **Name:** Define the name of the call flow
*  **Extension:** Define what extension to use. (This will make an extension not allready created)
*  **Feature Code:** Define what *  number to use
*  **Context:** Domain context (typically leave as is)
*  Status: Define what currently is in use.
*  Pin Number: Define a pin number in order to execute either mode.
*  **Destination:** Define where the call will go in the intial mode.
*  Sound: Define the sound that will play once mode is engaged.
*  Destination: Define what the destination will be.
*  Alternative Label: Label that will show when alternative mode is in use.
*  Alternative Sound: Define the sound that will play once alternative mode is engaged.
*  **Alternative Destination:** Define where the call will go in the alternative mode.
*  **Description:** Label what this call flow does.

|
|

Call Flow Example
^^^^^^^^^^^^^^^^^^

In the Call Flow example below we have the name as Call Flow.  Made the Extension number 30 that didn't exist until now.  Feature code we made with a *code as *30.  Kept the context as is with `training.fusionpbx.com`_ . Status to show which mode. Made a pin number to help secure the call flow. Made the detination label as Day Mode. Picked a sound to familiarize which mode is activated. Choose a destination for the alternative mode. Made the alternative detination label as Night Mode. Picked an alternative sound to familiarize which mode is activated. Choose a destination for the alternative mode. Finally describe what this call flow does.

|
|

.. image:: ../_static/images/fusionpbx_call_flow.jpg
        :scale: 50%


.. _training.fusionpbx.com: https://fusionpbx.com/app/www/training_detail.php
