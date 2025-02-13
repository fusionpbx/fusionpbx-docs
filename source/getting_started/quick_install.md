## FusionPBX Install

A Simple Guide to installing FusionPBX
 
---

### Debian
Debian 12 is the recommended operating system. Start with a minimal install.
Download: [Debian 12](https://cdimage.debian.org/cdimage), [Debian 11](https://cdimage.debian.org/cdimage/archive)

For best results, please ensure your server has been fully updated first...
```
sudo apt update && apt upgrade
```

Then run the following as root.
```
wget -O - https://raw.githubusercontent.com/fusionpbx/fusionpbx-install.sh/master/debian/pre-install.sh | sh;
cd /usr/src/fusionpbx-install.sh/debian && ./install.sh
```

---

### Ubuntu
Ubuntu 24.04 LTS. Start with a minimal install.

Download: [Ubuntu 24.04 LTS](https://ubuntu.com/download/server)

For best results, please ensure your server has been fully updated first

```
sudo apt update && apt upgrade
```

Then run the following as root
```
wget -O - https://raw.githubusercontent.com/fusionpbx/fusionpbx-install.sh/master/ubuntu/pre-install.sh | sh;
cd /usr/src/fusionpbx-install.sh/ubuntu && ./install.sh
```

### Raspberry Pi OS (Previously Raspbian)

Based on Debian Buster, Raspberry Pi OS works on the Raspberry Pi 2, 3, 4, and Zero W.

Download the [newest version](https://www.raspberrypi.com/software/) of Raspbian. Tools and information on unzipping the image and writing the operating system image to an SD card are available on the [Installing OS Images page](https://www.raspberrypi.org/documentation/installation/installing-images/README.md). Then run the following commands as root...

```
wget -O - https://raw.githubusercontent.com/fusionpbx/fusionpbx-install.sh/master/debian/pre-install.sh | sh;
cd /usr/src/fusionpbx-install.sh/debian && ./install.s
```

---

### FreeBSD
Start with a minimal install of FreeBSD 14.1. Then run the following commands:

```
pkg install --yes git
cd /usr/src && git clone https://github.com/fusionpbx/fusionpbx-install.sh.git
cd /usr/src/fusionpbx-install.sh/freebsd && ./install.sh
```


