# Phone

The Phone application is a WebRTC browser-based phone (softphone) built for FusionPBX and FreeSWITCH. It lets you make and receive calls entirely from a web browser — no desk phone required — with support for both audio and video calls.

The phone connects to FreeSWITCH over a secure WebSocket (WSS) using SIP.js and registers automatically as the logged in user's extension. Call media flows directly between the browser and FreeSWITCH using WebRTC.

:::{note}
The phone requires the web page to be served over HTTPS. Browsers only grant access to the microphone and camera on secure (HTTPS) pages, so a valid SSL certificate on your FusionPBX web server is required.
:::

## Features

- **Audio calls** — place and receive voice calls from the browser
- **Video calls** — place and receive video calls (requires the H.264 codec and FreeSWITCH video support)
- **Screen sharing** — share your screen during a video call
- **Multi-call** — handle multiple concurrent calls and switch between them
- **Call control** — hold/unhold, mute/unmute audio, mute/unmute video, decline, hang up
- **Blind transfer** — transfer the active call to another number
- **Call history** — recent calls stored locally in the browser
- **Messages** — instant messaging with conversation history
- **Contacts** — search your contacts and call them directly
- **Device selection** — choose audio input, audio output, and video input devices
- **Ringtones** — select ringback and ringtone sounds
- **Themes** — light and dark theme
- **Dashboard search** — optional link to the FusionPBX dashboard/contacts search

## How It Works

1. Log in to the FusionPBX web interface and open the **Phone** menu item.
2. The phone opens a secure WebSocket connection to `wss://<your-domain>:7443` on FreeSWITCH.
3. It registers your extension (using your extension and password) with a registration expiry of 120 seconds.
4. When you place or receive a call, the audio/video media streams directly between your browser and FreeSWITCH via WebRTC.

The status bar at the bottom of the phone shows the registration state: *Connecting*, *Registered*, *Disconnected*, or *Registration Failed*.

## Requirements

- A working installation of FusionPBX and FreeSWITCH
- A valid SSL certificate on the FusionPBX web server (HTTPS)
- **WSS enabled on a SIP profile** (see [Enabling WSS](#enabling-wss-on-a-sip-profile))
- **FreeSWITCH set up with SSL** — certificates for the SIP profiles
- **H.264 codec enabled** in FreeSWITCH for video support
- **`mod_opus` and `mod_rtc`** FreeSWITCH modules started (see [FreeSWITCH Modules](#freeswitch-modules))
- A modern WebRTC-capable browser (Chrome, Edge, or Firefox recommended)

## Installation

The Phone app is installed as a separate Git repository alongside the FusionPBX application.

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-phone.git phone
chown -R www-data:www-data /var/www/fusionpbx
php /var/www/fusionpbx/core/upgrade/upgrade.php
```

This installs the app, sets ownership, and registers its schema, permissions, and menu item. After installation, the **Phone** menu item will be available in the FusionPBX interface. If the menu item does not appear, go to **Advanced** > **Menu Manager** and click **Restore Defaults**, then log out and back in.

## Enabling WSS on a SIP Profile

The phone requires **WebSockets over SSL (WSS)** to be enabled on one of the SIP profiles. The phone connects to the SIP profile on the WSS port (default `:7443`).

There are two ways to configure this:

### Option 1: Use the Internal SIP Profile (Default)

On a default system, enable WSS on the **Internal** SIP profile.

- Go to **Advanced** > **SIP Profiles** > **Internal SIP Profile**.
- In the settings table, find the **wss-binding** setting and set it to `:7443` with **Enabled** set to **True**.

```
Name          = wss-binding
Value         = :7443
Enabled       = True
```

### Option 2: Create a Dedicated WSS Profile

Alternatively, you can copy the Internal SIP profile and create a dedicated WSS profile to avoid changing the default profile.

- Go to **Advanced** > **SIP Profiles** and copy the **Internal** SIP profile.
- Set the **Name** to `internal-5070`.
- Update the ports:
  - **sip-port** value: `5070`
  - **tls-sip-port** value: `5071`
  - **wss-binding** value: `:7443`
- Set **Enabled** to **True**.

```
Name          = internal-5070
sip-port      = 5070
tls-sip-port  = 5071
wss-binding   = :7443
Enabled       = True
```

:::{note}
The WSS binding uses a separate certificate. FreeSWITCH needs `wss.pem` in the certificates directory (`$${certs_dir}`); if it is not present, one will be created automatically.
:::

After making changes, restart the affected SIP profile(s) for the settings to take effect.

## FreeSWITCH Modules

The phone requires certain FreeSWITCH modules to be running. These can be managed in FusionPBX under **Advanced** > **Modules**.

- **`mod_rtc`** — Required for WebRTC support. This module provides the WebRTC media handling (DTLS-SRTP, ICE, etc.).
- **`mod_opus`** — The Opus audio codec, which is the primary codec used by WebRTC.

To enable a module:

1. Go to **Advanced** > **Modules**.
2. Find **`mod_opus`** and **`mod_rtc`** in the module list.
3. Enable (start) both modules.
4. Restart FreeSWITCH so the modules are loaded.

### H.264 Codec for Video

For **video** support, the **H.264** codec must be enabled in FreeSWITCH. Without the H.264 codec, video calls will not work.

- Audio-only calls work with the Opus audio codec alone.
- To support video calls, enable the **H.264** video codec in the FreeSWITCH configuration, then restart FreeSWITCH.
- The FreeSWITCH `vars.xml` file contains a commented-out codec preferences line that includes `H263` and `H264`, which can be used as a reference when enabling the video codec.

:::{important}
Audio-only calls work with `mod_opus` and `mod_rtc`. Video calls additionally require the **H.264** codec to be enabled. If video is not working, confirm H.264 is enabled and FreeSWITCH has been restarted.
:::

## SSL Configuration

FreeSWITCH must be set up with **SSL** for the WSS (and TLS SIP) transport to work.

- Ensure valid SSL certificates are in place for FreeSWITCH (in the certificates directory).
- The SIP profile's TLS settings (`tls`, `tls-cert-dir`, `tls-sip-port`) must be enabled and pointing to the correct certificates.
- The FusionPBX web server must also serve the phone page over **HTTPS** so the browser will allow microphone and camera access.

Refer to the [SIP TLS](../additional_information/sip_tls.md) and [Let's Encrypt](../getting_started/lets_encrypt.md) documentation for setting up certificates.

## Using the Phone

1. Log in to the FusionPBX web interface.
2. Open the **Phone** menu item.
3. The phone connects and registers your extension automatically — your extension number and password are used, so no manual login is needed.
4. Check the status bar: once it shows **Registered**, you are ready to make and receive calls.

**Making a call:**

- Use the dial pad to enter a number and press **Call** (audio) or the video button to place a video call.
- You can also select a contact from the **Contacts** tab, or a number from your **History**, and call it directly.

**During a call:**

- **Hold / Unhold** — place the call on hold.
- **Mute / Unmute** — mute or unmute your audio.
- **Video Mute** — turn your camera on or off during a video call.
- **Screen Share** — share your screen during a video call.
- **Blind Transfer** — transfer the call to another number.
- **Hang Up** — end the call.

With multiple concurrent calls, the phone shows each active call and lets you switch between them. Non-selected calls are placed on hold automatically.

**Settings:**

Open the phone settings to choose your audio input (microphone), audio output, and video input (camera) devices, select ringback and ringtone sounds, and switch between the light and dark theme.

## Default Settings

The Phone app registers the following default settings, which can be adjusted under **Advanced** > **Default Settings** (category `phone`):

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `phone.search_enabled` | boolean | true | Enable the dashboard search link (disabled by default). |
| `phone.search_domain` | text | *(blank)* | The domain to search. Defaults to the logged in user's domain. |
| `phone.search_path` | text | `/core/contacts/contacts.php` | The page path used for the search. |
| `phone.search_parameter` | text | `search` | The URL parameter used for the search. |
| `phone.search_target` | text | *(blank)* | Window target for the search link: `_blank` or `_self`. |
| `phone.search_width` | numeric | *(blank)* | Width of the search window popup. |
| `phone.search_height` | numeric | *(blank)* | Height of the search window popup. |

## Browser Support

The phone uses [SIP.js](https://sipjs.org) and standard WebRTC browser APIs. Any modern WebRTC-capable browser will work; Chrome, Edge, and Firefox are recommended. The browser must be able to reach the FreeSWITCH WSS port (`7443`) and the WebRTC media ports.

## Troubleshooting

- **Status bar shows *Disconnected* or *Registration Failed*:**
  - Confirm WSS is enabled on the SIP profile and `wss-binding` is set to `:7443`.
  - Confirm the SIP profile has been restarted after the change.
  - Make sure port `7443` is open in the firewall and reachable from the browser.
  - Verify the extension and password are correct (check **Status** > **Registrations**).
  - Open the browser developer console to view connection errors.

- **No audio:**
  - Grant microphone access when the browser prompts you.
  - Check the selected audio input/output device in the phone settings.
  - Confirm `mod_opus` is started in **Advanced** > **Modules**.

- **No video:**
  - Confirm the **H.264** codec is enabled in FreeSWITCH.
  - Confirm `mod_rtc` and `mod_opus` are started in **Advanced** > **Modules**.
  - Grant camera access when the browser prompts you and check the selected video input device.

- **Mixed content warning:** The phone page must be loaded over **HTTPS**. If the page is served over HTTP, the browser will block microphone and camera access.

- **Calls connect but there is no sound or video over NAT:** Verify the FreeSWITCH NAT settings are configured correctly (see [NAT](../additional_information/nat.md)) so that the WebRTC media ports are reachable.

## Files

| File | Description |
|------|-------------|
| `/var/www/fusionpbx/app/phone/phone.php` | Main phone page; renders the UI and injects the user's registration details |
| `/var/www/fusionpbx/app/phone/app_config.php` | App definition: menu item, permissions, and default settings |
| `/var/www/fusionpbx/app/phone/app_languages.php` | Multi-language strings |
| `/var/www/fusionpbx/app/phone/resources/phone.js` | Core phone logic (SIP.js user agent, calls, video, messages, contacts) |
| `/var/www/fusionpbx/app/phone/resources/sip-0.7.8.js` | SIP.js library |
| `/var/www/fusionpbx/app/phone/resources/styles.css` | Phone styling (light and dark themes) |
| `/var/www/fusionpbx/app/phone/resources/contacts_search.php` | Contact search endpoint |
| `/var/www/fusionpbx/app/phone/resources/sounds/` | Ringback tones and ringtones |

## References

- [SIP.js — SIP stack for JavaScript](https://sipjs.org)
- [WebRTC (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API)
- [FreeSWITCH mod_rtc](https://developer.signalwire.com/freeswitch/develop/Modules/mod_rtc/)
- [FreeSWITCH Developer Documentation](https://developer.signalwire.com/freeswitch/develop/)
- [RFC 7118 — Session Initiation Protocol (SIP) Extension for the WebSocket Transport](https://datatracker.ietf.org/doc/html/rfc7118)
