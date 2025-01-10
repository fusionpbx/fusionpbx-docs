##############
Email
##############

This is where you configure email settings to receive email notifications of voicemail, missed calls and fax.

Here are some example settings for some of the most common email providers.

*  `SMTP2GO <http://docs.fusionpbx.com/en/latest/advanced/default_settings/smtp2go.html>`_
*  `GMAIL <http://docs.fusionpbx.com/en/latest/advanced/default_settings/gmail.html>`_

+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| Default Setting Subcategory | Default Setting Name | Default Setting Value          | Default Setting Enabled | Default Setting Description                                                       |
+=============================+======================+================================+=========================+===================================================================================+
| smtp_host                   | text                 | mail.server.provider.com       | TRUE                    |  email providers server address                                                   |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from                   | text                 | emailexample@emailprovider.com | TRUE                    |  smtp from emaill address                                                         |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_port                   | numeric              | 587                            | TRUE                    | port number of the mail server provider                                           |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_from_name              | text                 | Voicemail                      | TRUE                    |  smtp from name                                                                   |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_auth                   | text                 | TRUE                           | TRUE                    |  If smtp auth is required                                                         |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_username               | text                 |  user name                     | TRUE                    |  typically the email user name                                                    |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_password               | text                 |  supersecurepassword!          | TRUE                    |   typically the email password                                                    |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_secure                 | text                 | tls                            | TRUE                    |  tls or ssl depending on the provider.                                            |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| smtp_validate_certificate   | boolean              | TRUE                           | TRUE                    | set to false to ignore SSL certificate warnings e.g. for self-signed certificates |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+
| method                      | text                 | smtp                           | TRUE                    | smtp|sendmail|mail|qmail                                                          |
+-----------------------------+----------------------+--------------------------------+-------------------------+-----------------------------------------------------------------------------------+

Error log for failed or sucessfully sent messages.

* `Email Log <http://docs.fusionpbx.com/en/latest/advanced/default_settings/email_error_log.rst>`_




How to Configure Email Settings in FusionPBX​ v5.3

1. Access the FusionPBX Web Interface

    Open your browser and go to your FusionPBX URL (e.g., http://<your-ip-or-domain>/).

2. Navigate to Default Settings

    Go to Advanced > Default Settings.

3. Filter for Email Settings

    In the Default Settings section, select "Email" from the drop-down filter.

4. Update and Enable Email Configuration

  Locate and update the following settings:

  - smtp_host: Set to your SMTP server (e.g., smtp.your-email-provider.com).

  - smtp_port: Set to 587 (or the port required by your SMTP server).

  - smtp_secure: Choose tls (or ssl if required by your provider).

  - smtp_auth: Set to true.

  - smtp_username: Enter your SMTP username.

  - smtp_password: Enter your SMTP password.

  - smtp_from: Specify the sender's email address (e.g., noreply@example.com).

  - smtp_from_name: Enter the sender's name.

5. Save and Reload

  Save the changes and click Reload to apply the settings.

6. Test the Email Configuration

  Navigate to Status > Email Queue.

  Send a test email to confirm that the configuration works correctly.
