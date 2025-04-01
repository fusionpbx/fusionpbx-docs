# Email

Configure your email settings to enable notifications for voicemails, missed calls, transcriptions and faxes directly to your inbox.

Below are some example configurations for popular email providers:

- [SMTP2GO](#smtp2go)
- [Gmail](#gmail)

Review logs of sent or failed email attempts:

- [Email Log](#email-log)

***

## Configuring Email Settings in FusionPBX v5.3

Follow these steps to set up email notifications:

1. **Access the FusionPBX Web Interface**

   Launch your web browser and navigate to your FusionPBX URL (e.g., `http://<your-ip-or-domain>/`).

2. **Navigate to Default Settings**

   From the menu, select **Advanced** > **Default Settings**.

3. **Filter for Email Settings**

   In the Default Settings section, choose "Email" from the drop-down filter.

4. **Configure Email Parameters**

   Update the following settings with your provider’s details:

   - `smtp_host`: Enter your SMTP server address (e.g., `smtp.your-email-provider.com`).
   - `smtp_port`: Set to `587` (or your provider’s specified port).
   - `smtp_secure`: Select `tls` (or `ssl`, depending on your provider’s requirements).
   - `smtp_auth`: Enable by setting to `true`.
   - `smtp_username`: Input your SMTP username.
   - `smtp_password`: Provide your SMTP password.
   - `smtp_from`: Specify the sender email address (e.g., `noreply@example.com`).
   - `smtp_from_name`: Define the sender’s display name (e.g., "FusionPBX Alerts").
   

5. **Save and Reload**

   Save the changes and click **Reload** to apply the new settings.

6. **Verify the Configuration**

   From the menu. select **Status** > **Email Queue** and send a test email to ensure everything works as expected.

***

## SMTP2GO

SMTP2GO is a paid email service for sending email. They do however have 1,000 free messages a month and paid plans that are reasonable.

1. Sign up for the service

![SMTP2GO Signup](../../_static/images/advanced/default_settings/fusionpbx_smtp2go.jpg)

2. After you confirm your email, sign in. You can create an smtp user at this screen or in the next step.

![SMTP2GO Signin](../../_static/images/advanced/default_settings/fusionpbx_smtp2go3.jpg)

3. Go to Settings > Users and create an smtp user or additional smtp users.

![SMTP2GO Users](../../_static/images/advanced/default_settings/fusionpbx_smtp2go_users.jpg)

4. You can set authentication by ip address. It's a good idea to set the limit here also from Unlimited to match which plan you choose.

![SMTP2GO Authentication](../../_static/images/advanced/default_settings/fusionpbx_smtp2go1.jpg)

5. Set the domain to your domain to make delivery seem as it came right from your own mail server. This can help sending to strict email domains.

![SMTP2GO Domain](../../_static/images/advanced/default_settings/fusionpbx_smtp2go2.jpg)

6. From your FusionPBX server install go to Advanced > Default Settings > Email section.

| Default Setting Subcategory | Default Setting Name | Default Setting Value      | Default Setting Enabled | Default Setting Description                                                       |
|-----------------------------|----------------------|----------------------------|-------------------------|-----------------------------------------------------------------------------------|
| smtp_host                   | text                 | mail.smtp2go.com           | True                    | email providers server address                                                    |
| smtp_from                   | text                 | emailaddress@gmail.com     | True                    | smtp from emaill address                                                          |
| smtp_port                   | numeric              | 587                        | True                    | port number of the mail server provider                                           |
| smtp_from_name              | text                 | Voicemail                  | True                    | smtp from name                                                                    |
| smtp_auth                   | text                 | TRUE                       | True                    | smtp auth is required                                                             |
| smtp_username               | text                 | emailaddress@gmail.com     | True                    | Use the full email address                                                        |
| smtp_password               | text                 | ************************** | True                    | typically the email password                                                      |
| smtp_secure                 | text                 | tls                        | True                    | tls or ssl depending on the provider.                                             |
| smtp_validate_certificate   | boolean              | TRUE                       | True                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
| method                      | text                 | sendmail                   | False                   | smtp\|sendmail\|mail\|qmail                                                       |

***

## Gmail

Goto Advanced > Default Settings and under the `Email` Section. Make sure these settings are enabled. Once these values are set press the **Reload** button at the top right of the page.

- There is a good chance you will have to do this via command line on your FusionPBX install https://accounts.google.com/b/0/DisplayUnlockCaptcha
- If you have a headless install(no desktop gui) then you will have to install lynx. Lynx is a command line web browser. For Debian you would type the example below. Follow the prompts for email address and password.

~~~
apt-get install lynx
lynx https://accounts.google.com/b/0/DisplayUnlockCaptcha
~~~

- You may also have to enable less secure apps https://support.google.com/accounts/answer/6010255?hl=en

| Default Setting Subcategory | Default Setting Name | Default Setting Value      | Default Setting Enabled | Default Setting Description                                                       |
|-----------------------------|----------------------|----------------------------|-------------------------|-----------------------------------------------------------------------------------|
| smtp_host                   | text                 | smtp.gmail.com             | True                    | email providers server address                                                    |
| smtp_from                   | text                 | emailaddress@gmail.com     | True                    | smtp from emaill address                                                          |
| smtp_port                   | numeric              | 587                        | True                    | port number of the mail server provider                                           |
| smtp_from_name              | text                 | Voicemail                  | True                    | smtp from name                                                                    |
| smtp_auth                   | text                 | true                       | True                    | smtp auth is required                                                             |
| smtp_username               | text                 | emailaddress@gmail.com     | True                    | Use the full email address                                                        |
| smtp_password               | text                 | ************************** | True                    | typically the email password                                                      |
| smtp_secure                 | text                 | tls                        | True                    | tls or ssl depending on the provider.                                             |
| smtp_validate_certificate   | boolean              | true                       | True                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
| method                      | text                 | smtp                       | True                    | smtp\|sendmail\|mail\|qmail                                                       |

To see if there are any failed email attempts goto Status > Emails. Once the issue causing the emails to fail is found you can click to resend them.

:::{note}
The log is stored in the /tmp directory.
:::

***

## Email Log

Successfully sent email example.

```
cat /tmp/mailer-app.log
```

- X-FusionPBX-Domain-Name: sub.domain.tld
- X-FusionPBX-Email-Type: voicemail
- X-FusionPBX-Call-UUID: 9jys3222-e9dd-4dc1-89df-aafb21349c5f
- X-FusionPBX-Domain-UUID: f98j8df-37da-4cef-bf42-0dc8c2093f9b
- Subject: =?utf-8?B?Vm9pY2VtYWlsIGZyb20gNDIwIDw0MjA+IDAwOjAwOjE0?=
- From: server notify<server notify>
- Reply-to:
- To: len.pgh@gmail.com
- Date:
- Add Address: len.pgh@gmail.com
- SMTP -> FROM SERVER:220 smtp.gmail.com ESMTP d192-v6sm2771356qkb.46 - gsmtp
- SMTP -> FROM SERVER: 250-smtp.gmail.com at your service, [192.168.100.113]
- 250-SIZE 35882577
- 250-8BITMIME
- 250-STARTTLS
- 250-ENHANCEDSTATUSCODES
- 250-PIPELINING
- 250-CHUNKING
- 250 SMTPUTF8
- SMTP -> FROM SERVER:220 2.0.0 Ready to start TLS
- SMTP -> FROM SERVER: 250-smtp.gmail.com at your service, [192.168.100.113]
- 250-SIZE 35882577
- 250-8BITMIME
- 250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH
- 250-ENHANCEDSTATUSCODES
- 250-PIPELINING
- 250-CHUNKING
- 250 SMTPUTF8
- SMTP -> FROM SERVER:250 2.1.0 OK d192-v6sm2771356qkb.46 - gsmtp
- SMTP -> FROM SERVER:250 2.1.5 OK d192-v6sm2771356qkb.46 - gsmtp
- SMTP -> FROM SERVER:354  Go ahead d192-v6sm2771356qkb.46 - gsmtp
- SMTP -> FROM SERVER:250 2.0.0 OK 1527795092 d192-v6sm2771356qkb.46 - gsmtp
- SMTP -> FROM SERVER:221 2.0.0 closing connection d192-v6sm2771356qkb.46 - gsmtp

Message sent!
