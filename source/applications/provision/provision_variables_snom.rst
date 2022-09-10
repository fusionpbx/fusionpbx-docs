#######
SNOM
#######

Variables used for Provisioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Below are a list of variables/default settings that can be configured at the system level or the domain level to change how phones are provisioned.

snom_firmware_url
==================
This is the URL that phones will get their firmware from. This should exclude the model specific file. To set this to use Snom's servers, use the following value: `https://downloads.snom.com:443/fw/`

snom_firmware_dXXX
==================
Replace the XXX with the model number of the phone you are using. For example, d785. This is the specific file that will get downloaded for that particular model. This is used in conjunction with the `snom_firmware_url` to download the firmware.

snom_language
==================
The language the phone will use. This is by default set to "English" however more languages are available. Refer to [Snom's Docs](https://service.snom.com/display/wiki/language) to get a listing of languages supported per device.

snom_ntp_server
==================
The server that Snom will use for it's NTP. By default: 0.pool.ntp.org

snom_time_zone
==================
The time zone that the phone will use. This is disabled by default however should be set to avoid the phone asking for a valid timezone on every boot. Valid value can be found on [Snom's webpage](https://service.snom.com/display/wiki/timezone).

snom_provision_timer_seconds
==================
The time in seconds that the phone will wait before attempting to provision itself again. This is useful for automatically updating the directory when changes are made.