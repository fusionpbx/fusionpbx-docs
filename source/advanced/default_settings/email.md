# Email

This is where you configure email settings to receive email
notifications of voicemail, missed calls and fax.

Here are some example settings for some of the most common email
providers.

-   [SMTP2GO](http://docs.fusionpbx.com/en/latest/advanced/default_settings/smtp2go.html)
-   [GMAIL](http://docs.fusionpbx.com/en/latest/advanced/default_settings/gmail.html)

+---------+-------+----------+--------+-----------------------------+
| Default | De    | Default  | D      | Default Setting Description |
| Setting | fault | Setting  | efault |                             |
| Subc    | Se    | Value    | S      |                             |
| ategory | tting |          | etting |                             |
|         | Name  |          | E      |                             |
|         |       |          | nabled |                             |
+=========+=======+==========+========+=============================+
| smt     | text  | mail.ser | TRUE   | > email providers server    |
| p[host] |       | ver.prov |        | > address                   |
| {#host} |       | ider.com |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smt     | text  | <emailex | TRUE   | > smtp from emaill address  |
| p[from] |       | ample@em |        |                             |
| {#from} |       | ailprovi |        |                             |
|         |       | der.com> |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smt     | nu    | 587      | TRUE   | port number of the mail     |
| p[port] | meric |          |        | server provider             |
| {#port} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smtp[f  | text  | V        | TRUE   | > smtp from name            |
| rom_nam |       | oicemail |        |                             |
| e]{#fro |       |          |        |                             |
| m_name} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smt     | text  | TRUE     | TRUE   | > If smtp auth is required  |
| p[auth] |       |          |        |                             |
| {#auth} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smtp    | text  | > user   | TRUE   | > typically the email user  |
| [userna |       | > name   |        | > name                      |
| me]{#us |       |          |        |                             |
| ername} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smtp    | text  | > supe   | TRUE   | > typically the email       |
| [passwo |       | rsecurep |        | > password                  |
| rd]{#pa |       | assword! |        |                             |
| ssword} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smtp[se | text  | tls      | TRUE   | > tls or ssl depending on   |
| cure]{# |       |          |        | > the provider.             |
| secure} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| smtp[va | bo    | TRUE     | TRUE   | set to false to ignore SSL  |
| lidate_ | olean |          |        | certificate warnings e.g.   |
| certifi |       |          |        | for self-signed             |
| cate]{# |       |          |        | certificates                |
| validat |       |          |        |                             |
| e_certi |       |          |        |                             |
| ficate} |       |          |        |                             |
+---------+-------+----------+--------+-----------------------------+
| method  | text  | smtp     | TRUE   | smtp[\|sendmail\|](##SU     |
|         |       |          |        | BST##|sendmail|)mail\|qmail |
+---------+-------+----------+--------+-----------------------------+

Error log for failed or sucessfully sent messages.

-   [Email
    Log](http://docs.fusionpbx.com/en/latest/advanced/default_settings/email_error_log.rst)

How to Configure Email Settings in FusionPBX​ v5.3

1.  Access the FusionPBX Web Interface

    > Open your browser and go to your FusionPBX URL (e.g.,
    > <http://>\<your-ip-or-domain\>/).

2.  Navigate to Default Settings

    > Go to Advanced \> Default Settings.

3.  Filter for Email Settings

    > In the Default Settings section, select \"Email\" from the
    > drop-down filter.

4.  Update and Enable Email Configuration

> Locate and update the following settings:
>
> -   smtp[host]{#host}: Set to your SMTP server (e.g.,
>     smtp.your-email-provider.com).
> -   smtp[port]{#port}: Set to 587 (or the port required by your SMTP
>     server).
> -   smtp[secure]{#secure}: Choose tls (or ssl if required by your
>     provider).
> -   smtp[auth]{#auth}: Set to true.
> -   smtp[username]{#username}: Enter your SMTP username.
> -   smtp[password]{#password}: Enter your SMTP password.
> -   smtp[from]{#from}: Specify the sender\'s email address (e.g.,
>     <noreply@example.com>).
> -   smtp[from_name]{#from_name}: Enter the sender\'s name.

5.  Save and Reload

> Save the changes and click Reload to apply the settings.

6.  Test the Email Configuration

> Navigate to Status \> Email Queue.
>
> Send a test email to confirm that the configuration works correctly.
