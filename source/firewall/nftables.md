# Nftables

Nftables is the successor to iptables and the default netfilter front
end on recent Debian releases. The Debian install script supports
nftables as an alternative firewall (added in fusionpbx-install.sh
pull request #465).

:::: note
<p class="admonition-title">Note</p>

By default the install script installs **iptables**. The nftables
option is commented out and must be enabled manually (see below). On
Debian 13 (trixie) the standard `iptables` binary is actually
nft-backed (`iptables-nft`); when iptables is selected the install
script pins the `iptables-legacy` alternatives so the two options
behave consistently.
::::

## Enabling in the Install Script

In `debian/install.sh`, the firewall install step looks like this:

```
#IPTables
resources/iptables.sh

#NFTables
#resources/nftables.sh
```

To install nftables instead of iptables, comment out the iptables line
and uncomment the nftables line:

```
#IPTables
#resources/iptables.sh

#NFTables
resources/nftables.sh
```

## What the Install Script Does

The `nftables.sh` script:

- Installs the `nftables` package
- Purges `iptables-persistent` and removes `/etc/iptables`
- Writes the rule set to `/etc/nftables.conf` (see
  [Basic Rules](#basic-rules))
- Enables and starts the `nftables` service
- Loads the rules with `nft -f /etc/nftables.conf`

**Fail2ban integration.** The fail2ban install script detects which
firewall was installed. If `/etc/iptables/rules.v4` is **not**
present, nftables was selected - the script installs the nftables
version of `jail.local` (all jails use the `nftables-allports`
action) and rewrites `iptables` to `nftables` in
`/etc/fail2ban/jail.conf`. If the file is present, the regular
iptables `jail.local` is installed. See [Fail2ban](fail2ban.md).

## Basic Rules

The install script writes the following rule set to
`/etc/nftables.conf`:

```
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
    chain input {
        type filter hook input priority 0;
        policy drop;

        # Block specific IP addresses
        #ip saddr 10.1.0.3 drop

        # Allow loopback interface traffic
        iifname "lo" counter accept

        # Accept related and established connections
        ct state related,established counter accept

        # Allow SSH port
        tcp dport 22 counter accept

        # Allow HTTP/HTTPS
        tcp dport {80,443} counter accept

        # Secure Websocket port
        tcp dport 7443 counter accept

        # Allow SIP ports
        tcp dport 5060-5091 counter accept
        udp dport 5060-5091 counter accept

        # Allow RTP Media ports
        udp dport 16384-32768 counter accept

        # Accept ICMP echo requests (ping)
        icmp type echo-request counter accept

        # Allow OpenVPN port
        udp dport 1194 counter accept
    }

    chain forward {
        type filter hook forward priority 0;
        policy drop;
    }

    chain output {
        type filter hook output priority 0;
        policy accept;
    }

    chain sip-auth-ip {
        type filter hook input priority -50;
        policy accept;

        # Block specific IP addresses
        #ip saddr 10.1.0.3 counter drop
    }

    chain sip-auth-fail {
        type filter hook input priority -50;
        policy accept;
    }
}

table inet mangle {
    chain output {
        type route hook output priority -150;

        # Set DSCP value for TCP and UDP traffic from source ports
        tcp sport 5060-5091 counter ip dscp set 0x1a
        udp sport 5060-5091 counter ip dscp set 0x1a

        # Set DSCP value for UDP traffic from source ports
        udp sport 16384-32768 counter ip dscp set 0x2e

        policy accept;
    }
}
```

The `inet` family covers both IPv4 and IPv6. The `sip-auth-ip` and
`sip-auth-fail` chains are pre-created for the
[Event Guard](../status/event_guard.md) feature, which blocks
addresses that repeatedly fail SIP authentication; they are empty by
default.

## Optional Rules

**OpenVPN**

```
nft add rule inet filter input udp dport 1194 counter accept
```

**ICMP**

```
nft add rule inet filter input icmp type echo-request counter accept
```

Both rules are already included in the base rule set; add them back
if you remove them.

## Friendly Scanner

The iptables install script drops SIP packets that contain scanner
user-agent strings (`friendly-scanner`, `VaxSIPUserAgent`, and more)
using `-m string` matches. The nftables rule set does **not** include
these rules because nftables has no direct equivalent of the iptables
string match - payload string matching requires string set maps.
Abusive scanners are still covered by the fail2ban jails (see
[Fail2ban](fail2ban.md)).

## DSCP Rules

The `inet mangle` table marks outgoing call traffic, equivalent to
the DSCP rules in the [iptables](iptables.md) documentation:

- `0x1a` (26) - SIP traffic from source ports 5060-5091
- `0x2e` (46) - RTP media from source ports 16384-32768

## Show Rules

```
nft list ruleset
```

Show rule handles and counters (the nftables equivalent of line
numbers):

```
nft -a list ruleset
```

## Show DSCP Rules

```
nft list table inet mangle
```

## Add a Rule

Rules can be added at runtime; they stay in memory until saved
(see [Save Changes](#save-changes)).

**Open a Port for a Specific IP Address**

```
nft add rule inet filter input ip saddr x.x.x.x/32 tcp dport 5432 counter accept
```

**Block an IP Address**

```
nft add rule inet filter input ip saddr 62.210.245.132 counter drop
```

## Delete a Rule

Unlike iptables, nftables rules have no line numbers; they are
addressed by handle. Find the handle with `nft -a list ruleset`, then
delete the rule:

```
nft delete rule inet filter input handle 9
```

## Flush

Flush all rules:

```
nft flush ruleset
```

Flush without losing access to SSH - accept SSH first, then flush:

```
nft add rule inet filter input tcp dport 22 counter accept
nft flush ruleset
```

## Restore Rules

Load the saved rule set back into memory:

```
nft -f /etc/nftables.conf
```

The `nftables` service loads this file automatically on boot.

## Save Changes

The `nftables` service persists rules via `/etc/nftables.conf`. To
save the current in-memory rule set:

```
nft list ruleset > /etc/nftables.conf
systemctl restart nftables
```

## Differences from iptables

| | iptables | nftables |
|---|---|---|
| Install script | `resources/iptables.sh` (default) | `resources/nftables.sh` (commented out) |
| Saved rules | `/etc/iptables/rules.v4` via `iptables-persistent` | `/etc/nftables.conf` via the `nftables` service |
| Show rules | `iptables -L -n` | `nft list ruleset` |
| Restore rules | `iptables-restore < /etc/iptables/rules.v4` | `nft -f /etc/nftables.conf` |
| Fail2ban action | `iptables-allports` | `nftables-allports` |
| Fail2ban jail file | `jail.local` | `jail.local.nft` (auto-selected) |
| Scanner string blocks | Included | Not included (no `-m string` equivalent) |
