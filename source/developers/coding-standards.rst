****************
Coding Standards
****************

- **All processes are running**

    **Run location: GZ**
    Command (example):

    .. code-block:: bash

        ps -afe | grep run_erl | grep -v grep
        root 48037 1 0 Dec 27 ? 0:00 /opt/chunter/erts-5.9.1/bin/run_erl -daemon /tmp/chunter /var/log/chunter exec 
        0000105 65606 1 0 10:38:57 ? 0:00 /opt/local/wiggle/erts-5.9.1/bin/run_erl -daemon /tmp/wiggle/ /var/log/wiggle e
        0000104 99374 1 0 08:39:13 ? 0:00 /opt/local/sniffle/erts-5.9.1/bin/run_erl -daemon /tmp/sniffle/ /var/log/sniffl
        0000103 42238 1 0 06:55:02 ? 0:00 /opt/local/snarl/erts-5.9.1/bin/run_erl -daemon /tmp/snarl/ /var/log/snarl exec
        0000106 56504 1 0 07:20:50 ? 0:00 /opt/local/howl/erts-5.9.1/bin/run_erl -daemon /tmp/howl /var/log/howl exec /op

____
