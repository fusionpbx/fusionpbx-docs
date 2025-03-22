# Let\'s Encrypt

Let\'s Encrypt is one of the most recent and widely used form of free
SSL security and supports wildcard DNS. You can use Let\'s Encrypt with
your FusionPBX install and WebRTC like [Verto
Communicator](https://freeswitch.org/confluence/display/FREESWITCH/Verto+Communicator).

## Dehydrated (Recommended)

FusionPBX has an option to easily and quickly install SSL with Let\'s
Encrypt using **letsencrypt.sh** With this script you can choose either
to request an SSL certificate with wildcard (\*.domain.tld) or hostnames
(domain.tld).

The letsencrypt.sh will do the following:

-   Download [dehydrated](https://github.com/lukas2511/dehydrated).
-   Request an SSL certificate from [Let\'s
    Encrypt](https://letsencrypt.com).
-   Configure NGINX to use the SSL certificate.
-   Combine and place the SSL certificate in the proper
    [FreeSWITCH](https://freeswitch.org/confluence/display/FREESWITCH/FreeSWITCH+Explained)
    directory for using TLS.
-   Test and make sure the SSL cert works and outputs if successful.

### Using letsencrypt.sh

With letsencrypt.sh you have the choice of creating an SSL certificate
for a single domain (domain.tld), multiple subdomains (sub.domain.tld,
sub1.domain.tld, etc.domain.tld) or wildcard (\*.domain.tld). The easy
way however is using the hostname method.

#### Hostname

To create a hostname or multiple hostname SSL certificate go to:

    cd /usr/src/fusionpbx-install.sh/debian/resources/

Then execute the script.

    ./letsencrypt.sh

You should then see and follow the prompts.

    Domain Name: domain.tld
    Email Address: support@fusionpbx.com

After that, you should see the following output.

    Cloning into 'dehydrated'...
    remote: Counting objects: 1914, done.
    remote: Total 1914 (delta 0), reused 0 (delta 0), pack-reused 1914
    Receiving objects: 100% (1914/1914), 616.01 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (1199/1199), done.
    # INFO: Using main config file /etc/dehydrated/config
    + Generating account key...
    + Registering account key with ACME server...
    + Done!
    # INFO: Using main config file /etc/dehydrated/config
    + Creating chain cache directory /etc/dehydrated/chains
    Processing domain.tld
    + Creating new directory /etc/dehydrated/certs/domain.tld ...
    + Signing domains...
    + Generating private key...
    + Generating signing request...
    + Requesting new certificate order from CA...
    + Received 1 authorizations URLs from the CA
    + Handling authorization for domain.tld
    + 1 pending challenge(s)
    + Deploying challenge tokens...
    + Responding to challenge for domain.tld authorization...
    + Challenge is valid!
    + Cleaning challenge tokens...
    + Requesting certificate...
    + Checking certificate...
    + Done!
    + Creating fullchain.pem...
    + Done!

    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful

#### Wildcard

To create a wildcard SSL certificate go to:

    cd /usr/src/fusionpbx-install.sh/debian/resources/

Then execute the script.

    ./letsencrypt.sh

You should then see and follow the prompts:

    Domain Name: *.domain.tld
    Email Address: support@fusionpbx.com

    Cloning into 'dns-01-manual'...
    remote: Counting objects: 9, done.
    remote: Total 9 (delta 0), reused 0 (delta 0), pack-reused 9
    Unpacking objects: 100% (9/9), done.
    Checking connectivity... done.
    # INFO: Using main config file /etc/dehydrated/config
    + Account already registered!
    # INFO: Using main config file /etc/dehydrated/config
    Processing *.domain.tld
    + Checking domain name(s) of existing cert... changed!
    + Domain name(s) are not matching!
    + Names in old certificate: domain.tld
    + Configured names: *.domain.tld
    + Forcing renew.
    + Checking expire date of existing cert...
    + Valid till Nov 19 16:08:32 2018 GMT (Longer than 30 days). Ignoring because renew was forced!
    + Signing domains...
    + Generating private key...
    + Generating signing request...
    + Requesting new certificate order from CA...
    + Received 1 authorizations URLs from the CA
    + Handling authorization for domain.tld
    + 1 pending challenge(s)
    + Deploying challenge tokens...

:::: note
<p class="admonition-title">Note</p>

When you define the txt record with your domain registrar be sure to use
the output of the script you are running and not what is in this
example.
::::

    Add the following to the zone definition of domain.tld:
    _acme-challenge.domain.tld. IN TXT "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"

    **Press enter to continue...**

    + Responding to challenge for domain.tld authorization...
    + Challenge is valid!
    + Cleaning challenge tokens...

    Now you can remove the following from the zone definition of domain.tld:
    _acme-challenge.domain.tld. IN TXT "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"

    **Press enter to continue...**

    + Requesting certificate...
    + Checking certificate...
    + Done!
    + Creating fullchain.pem...

    deploy_cert()

    Done!

    **done**

    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful

:::: tip
<p class="admonition-title">Tip</p>

Use the dig command to check that the txt record is correct. 
```
dig -t txt _acme-challenge.domain.tld
```

Output should show:

;; ANSWER SECTION:
_acme-challenge.domain.tld. 1799 IN TXT  "PY7ttk6no_5eG7WtAbO6qs5-NzA-Kigko375omKc0nw"
::::

