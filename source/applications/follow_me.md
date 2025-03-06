# Follow Me

Define alternate inbound call handling for the following extensions.

![Follow Me Settings](../_static/images/fusionpbx_follow_me.jpg)

- **Call Forward**: (Disabled or Enabled) Input the destination number
- **On Busy**: (Disabled or Enabled) If enabled, it overrides the value of voicemail enabling in extension
- **No Answer**: (Disabled or Enabled) If enabled, it overrides the value of voicemail enabling in extension
- **Not Registered**: (Disabled or Enabled) If endpoint is not reachable, forward to this destination before going to voicemail
- **Follow Me**: (Disabled or Enabled)
- **Destinations**: Can set Delay, Timeout, and Prompt to accept the call
- **Ignore Busy**: (Disabled or Enabled)
- **Do Not Disturb**: (Disabled or Enabled)

This example has both the extension 1301 itself and an external number to call. If you don’t include the extension itself, the extension won’t ring when in Follow Me. This is due to the flexible nature of FusionPBX—e.g., if you’re out of the office on a business trip and don’t want that extension to ring.

![Follow Me Example](../_static/images/fusionpbx_follow_me1.jpg)

## Follow Me Default Settings

Click the link above for Follow Me default settings: [Follow Me Default Settings](/en/latest/advanced/default_settings.html#id13)
