# STIR/SHAKEN Identity

The Identity application integrates [STIR/SHAKEN](https://en.wikipedia.org/wiki/STIR/SHAKEN) identity signing and verification into FusionPBX. STIR/SHAKEN is a framework for authenticating the origin of calls and preventing caller ID spoofing. The app signs outbound calls with a [PASSporT](https://datatracker.ietf.org/doc/html/rfc8225) (PASSport for Telephone Identity) token and can verify PASSporT tokens on inbound calls.

This is an optional add-on app that is not included in the default FusionPBX installation. It requires obtaining a valid signing certificate from an approved Certificate Authority (CA) in your country.

:::{note}
The STIR/SHAKEN framework is based on [RFC 8225](https://datatracker.ietf.org/doc/html/rfc8225) (PASSporT) and [RFC 8228](https://datatracker.ietf.org/doc/html/rfc8228) (Authentication, Authorization, and Accounting for the Secure Telephone Identity). The app uses the ES256 (ECDSA P-256) signing algorithm.
:::

## How It Works

- **Signing (Outbound):** When an outbound call is placed, the app generates a signed JWT (PASSporT) containing the caller's number, the destination number, an attestation level, and a unique call identifier. This token is attached to the SIP `Identity` header so the receiving network can verify the call's authenticity.

- **Verification (Inbound):** When an inbound call arrives with a SIP `Identity` header, the app downloads the sender's public certificate and verifies the PASSporT signature. It then reports the verification result and the attestation level.

### Attestation Levels

| Level | Description |
|-------|-------------|
| **A** | Full attestation — the service provider has fully verified the identity and number of the calling party. |
| **B** | Partial attestation — the service provider has verified the identity of the calling party but may not have a direct relationship to the number. |
| **C** | General attestation — the calling number is believed to be legitimate, but no specific identity verification is performed. |
| **T** | Test — indicates that the token was created for testing purposes only. |

## Installation

The Identity app is installed as a separate Git repository alongside the FusionPBX application.

```
cd /var/www/fusionpbx/app
git clone https://github.com/fusionpbx/fusionpbx-app-identity.git identity
cd /var/www/fusionpbx
php core/upgrade/upgrade.php --permissions
php core/upgrade/upgrade.php
```

This installs the app and registers its permissions and schema. After installation, the app files reside in `/var/www/fusionpbx/app/identity/`.

## Obtaining Certificates

STIR/SHAKEN requires that you obtain a signing certificate from a Certificate Authority (CA) that is approved by your country's telecommunications regulatory body.

The Administrator: Once authorized by the governance framework, the CAs are operationalized and managed via the STI-PA (Secure Telephone Identity Policy Administrator), a role currently fulfilled by iconectiv. The STI-PA maintains the official list of authorized CAs.

The Role of the FCC: The FCC sets the overarching legal mandates, enforcement rules, and deadlines requiring voice service providers to implement STIR/SHAKEN. They also manage the Robocall Mitigation Database (RMD), where carriers must register. However, the FCC does not directly vet, approve, or issue certificates for individual CAs.

Once you have obtained your private key and certificate, place them in the `/etc/fusionpbx/certs` directory.

```
mkdir -p /etc/fusionpbx/certs
```

By default, the files should be named:

| File | Purpose |
|------|---------|
| `identity_private.key` | Your private key used to sign calls |
| `identity_certificate.pem` | Your public certificate |

:::{important}
Ensure that the file permissions on the private key are restricted to the web server user (e.g. `www-data`) and that the file is not world-readable.
:::

## Configuration

Add the following settings to `/etc/fusionpbx/config.conf`:

```
#identity - STIR/SHAKEN
identity.path = '/etc/fusionpbx/certs'
identity.private_key_name = 'identity_private.key'
identity.certificate_name = 'identity_certificate.pem'
identity.certificate_url = 'https://certs.yourdomain.local/public_key.pem'
identity.allowed_cidr = '127.0.0.1/32'
identity.debug = false
```

**Setting Descriptions**

- **`identity.path`**: The directory where your private key and certificate files are stored.
- **`identity.private_key_name`**: The file name of your private key within the certificate directory.
- **`identity.certificate_name`**: The file name of your certificate within the certificate directory.
- **`identity.certificate_url`**: The publicly accessible URL where the receiving server can download your certificate to verify the PASSporT token. This must be a valid, reachable HTTPS URL.
- **`identity.allowed_cidr`**: A comma-separated list of CIDR addresses (or subnets) that are allowed to access the sign and verify endpoints over HTTP. For example: `127.0.0.1/32,192.168.1.0/24`. Remember to include the CIDR notation (e.g. `/32` for a single IP).
- **`identity.debug`**: Set to `true` to enable debug output (useful during setup). Set to `false` in production.

## Sign Endpoint (sign.php)

The `sign.php` script generates a signed STIR/SHAKEN PASSporT token for a given source and destination phone number. It can be called from the command line or over HTTP.

### Command Line

```
php /var/www/fusionpbx/app/identity/sign.php <source> <destination> [attest_level]
```

- `source` — The outbound caller ID number (E.164 format, `+` optional)
- `destination` — The destination number (E.164 format, `+` optional)
- `attest_level` — Optional: `A`, `B`, or `C` (defaults to `A`)

Example:

```
php /var/www/fusionpbx/app/identity/sign.php 18005551212 18005551313 A
```

### HTTP (cURL)

The numbers must be in E.164 format (country code + number), the `+` is optional.

```
curl -X POST \
     -d "source=18005551212" \
     -d "destination=18005551313" \
     http://127.0.0.1/app/identity/sign.php
```

The response is the base64url-encoded PASSporT JWT token, or `TN-Validation-Failed` if signing failed.

### Optional Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `source` | Originator phone number (required) | — |
| `destination` | Destination phone number (required) | — |
| `attest_level` | Attestation level: `A`, `B`, or `C` | `A` |

## Verify Endpoint (verify.php)

The `verify.php` script verifies a STIR/SHAKEN PASSporT token. It downloads the sender's public certificate (from the `x5u` field in the JWT header), extracts the public key, and validates the ECDSA signature.

### Command Line

```
php /var/www/fusionpbx/app/identity/verify.php <identity_header>
```

Example:

```
php /var/www/fusionpbx/app/identity/verify.php "eyJhbGciOiJFUzI1NiI..."
```

### HTTP (cURL)

```
curl -X POST \
     -d "identity=<PASSPOR_TOKEN>" \
     http://127.0.0.1/app/identity/verify.php
```

### Response Values

| Response | Meaning |
|----------|---------|
| `TN-Validation-Passed-<level>` | The PASSporT signature is valid. The level is the attestation level (A, B, C, or T). |
| `TN-Validation-Failed` | The PASSporT signature could not be verified. |
| `No-TN-Validation` | No Identity header was provided. |

## Outbound Route Integration

To sign all outbound calls automatically, add the following FreeSWITCH dialplan actions to your **Outbound Route**:

```xml
<action application="unset" data="sip_h_Identity"/>
<action application="curl" data="http://127.0.0.1/app/identity/sign.php POST source=${effective_caller_id_number}&destination=1$1"/>
<action application="export" data="exclude_outgoing_extra_header=sip_h_Identity"/>
<action application="set" data="sip_h_Identity=${curl_response_data}"/>
```

**What each action does:**

1. **`unset sip_h_Identity`** — Removes any existing `Identity` header to ensure a clean state.
2. **`curl`** — Calls the `sign.php` endpoint with the caller ID number and destination number. FreeSWITCH stores the HTTP response in the `curl_response_data` channel variable.
3. **`export exclude_outgoing_extra_header=sip_h_Identity`** — Prevents the `Identity` header from being added as a generic extra header (so it is not duplicated).
4. **`set sip_h_Identity`** — Sets the signed PASSporT token as the SIP `Identity` header on the outbound call.

:::{note}
Adjust the `destination` value in the curl action to match your dialing format. The example above prepends `1` for US 11-digit dialing. For international or different formats, modify accordingly.
:::

## Inbound Route Integration

To verify STIR/SHAKEN tokens on inbound calls, add a dialplan action to your **Inbound Route** that calls the `verify.php` endpoint. The SIP `Identity` header is available in FreeSWITCH as the `sip_h_Identity` channel variable.

```xml
<action application="curl" data="http://127.0.0.1/app/identity/verify.php POST identity=${sip_h_Identity}"/>
<action application="set" data="stir_shaken_result=${curl_response_data}"/>
```

You can then use the `stir_shaken_result` variable in subsequent dialplan actions (e.g., to reject calls with a failed attestation level or to log the result).

## Security Considerations

- **CIDR Restrictions:** Both `sign.php` and `verify.php` check the requesting IP against the `identity.allowed_cidr` setting. Only allow trusted addresses (e.g., localhost, or your FreeSWITCH server's IP).
- **Private Key Protection:** Ensure the private key file is readable only by the web server user and is not exposed through the web root.
- **Certificate URL:** The `certificate_url` must be publicly accessible but should only expose the public certificate, never the private key.
- **Debug Mode:** Keep `identity.debug` set to `false` in production. Debug output may leak sensitive information about signing or verification failures.

## Troubleshooting

- **`TN-Validation-Failed` from sign.php:** Check that the private key file exists at the configured path and is readable by the web server user. Enable `identity.debug = true` to see detailed error messages.
- **`TN-Validation-Failed` from verify.php:** Verify that the `certificate_url` in the sender's PASSporT header is reachable. Check that the certificate has not expired. Enable `identity.debug = true` for detailed error messages.
- **No Identity header on outbound calls:** Confirm the dialplan actions are in the correct outbound route and that the `curl` application is available in FreeSWITCH. Use `fs_cli` to inspect the SIP message headers of an outbound call.
- **HTTP access denied:** Ensure the server's IP address is included in `identity.allowed_cidr` with the correct CIDR notation.

## Files

| File | Description |
|------|-------------|
| `/var/www/fusionpbx/app/identity/sign.php` | HTTP/CLI endpoint for generating signed PASSporT tokens |
| `/var/www/fusionpbx/app/identity/verify.php` | HTTP/CLI endpoint for verifying PASSporT tokens |
| `/var/www/fusionpbx/app/identity/resources/functions.php` | Utility functions (CIDR check, UUID validation, CLI detection) |
| `/var/www/fusionpbx/app/identity/resources/classes/identity.php` | Core STIR/SHAKEN identity class (signing, verification, key management) |
| `/etc/fusionpbx/config.conf` | Configuration settings (under the `#identity` section) |
| `/etc/fusionpbx/certs/` | Directory for the private key and certificate files |

## References

- [RFC 8225 — PASSporT (PASSport for Telephone Identity)](https://datatracker.ietf.org/doc/html/rfc8225)
- [RFC 8228 — Authentication, Authorization, and Accounting for the STIR/SHAKEN Secure Telephone Identity](https://datatracker.ietf.org/doc/html/rfc8228)
- [RFC 7845 — JWT Profile for Secure Web Proxy Authentication](https://datatracker.ietf.org/doc/html/rfc7845)
- [STIR/SHAKEN Overview (NIST)](https://csrc.nist.gov/pubs/sp/1800/18/final)
- [FCC — STIR/SHAKEN Implementation](https://www.fcc.gov)
