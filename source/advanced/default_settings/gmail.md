# Gmail

Goto Advanced \> Default Settings and under the `Email` Section. Make
sure these settings are enabled. Once these values are set press the
**Reload** button at the top right of the page.

-   There is a good chance you will have to do this via command line on
    your FusionPBX install
    <https://accounts.google.com/b/0/DisplayUnlockCaptcha>
-   If you have a headless install(no desktop gui) then you will have to
    install lynx. Lynx is a command line web browser. For Debian you
    would type the example below. Follow the prompts for email address
    and password.

<!-- -->

    apt-get install lynx
    lynx https://accounts.google.com/b/0/DisplayUnlockCaptcha

-   You may also have to enable less secure apps
    <https://support.google.com/accounts/answer/6010255?hl=en>

+----------+-------+---------+--------+------------------------------+
| Default  | De    | Default | D      | Default Setting Description  |
| Setting  | fault | Setting | efault |                              |
| Sub      | Se    | Value   | S      |                              |
| category | tting |         | etting |                              |
|          | Name  |         | E      |                              |
|          |       |         | nabled |                              |
+==========+=======+=========+========+==============================+
| s        | text  | smtp.gm | True   | > email providers server     |
| mtp[host |       | ail.com |        | > address                    |
| ]{#host} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | text  | <em     | True   | > smtp from emaill address   |
| mtp[from |       | ailaddr |        |                              |
| ]{#from} |       | ess@gma |        |                              |
|          |       | il.com> |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | nu    | 587     | True   | port number of the mail      |
| mtp[port | meric |         |        | server provider              |
| ]{#port} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| smt      | text  | Vo      | True   | > smtp from name             |
| p[from_n |       | icemail |        |                              |
| ame]{#fr |       |         |        |                              |
| om_name} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | text  | true    | True   | > smtp auth is required      |
| mtp[auth |       |         |        |                              |
| ]{#auth} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | text  | <em     | True   | > Use the full email address |
| mtp[user |       | ailaddr |        |                              |
| name]{#u |       | ess@gma |        |                              |
| sername} |       | il.com> |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | text  | -----   | True   | > typically the email        |
| mtp[pass |       |         |        | > password                   |
| word]{#p |       |         |        |                              |
| assword} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| smtp[    | text  | tls     | True   | > tls or ssl depending on    |
| secure]{ |       |         |        | > the provider.              |
| #secure} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| s        | bo    | true    | True   | set to false to ignore SSL   |
| mtp[vali | olean |         |        | certificate warnings e.g.    |
| date_cer |       |         |        | for self-signed certificates |
| tificate |       |         |        |                              |
| ]{#valid |       |         |        |                              |
| ate_cert |       |         |        |                              |
| ificate} |       |         |        |                              |
+----------+-------+---------+--------+------------------------------+
| method   | text  | smtp    | True   | smtp[\|sendmail\|](##S       |
|          |       |         |        | UBST##|sendmail|)mail\|qmail |
+----------+-------+---------+--------+------------------------------+

To see if there are any failed email attempts goto Status \> Emails.
Once the issue causing the emails to fail is found you can click to
resent them.

:::: note
::: title
Note
:::

The log is stored in the /tmp directory.
::::
