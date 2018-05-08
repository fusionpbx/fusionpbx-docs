####################
Number Translations
####################


Use this to translate numbers from the original number to a new number using regular expressions.


.. image:: ../_static/images/advanced/fusionpbx_advanced_number_translations.jpg
        :scale: 85%

Activating mod-translate:
1. Install the package "freeswitch-mod-translate" via aptitude/apt-get etc.
2. Configure the module to your likes via the GUI: Advanced -> Number Translations. 
3. Activate the module in FusionPBX Advanced -> Modules in the Applications section

The documentation for mod-translate can be found under https://freeswitch.org/confluence/display/FREESWITCH/mod_translate

To use mod-translate to modify inbound calls before they hit the dialplan the following setting for the SIP-profile must be modified:
  dialplan "XML" -> dialplan "Translate,XML"
To activate this setting, the SIP-profile needs to be restarted and memcache flushed.
