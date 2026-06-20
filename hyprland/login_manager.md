To change your login manager, you have to install it, disable the service for the old one and enable the service for the new one (e.g. in systemd)

# Ly

To activate Ly, first install it

```
sudo pacman -S ly
```

Figure out which login manager you are using right now

```
systemctl list-units
```

Disable your current login manager

```
sudo systemctl disable <your_login_manager>.service
sudo systemctl disable getty@tty2.service
```

Enable Ly

```
sudo systemctl enable ly@tty2.service
```

Reboot system to test

You can adapt `/etc/ly/config.ini` to adjust your preferences

## Multi-head monitors

If you have multiple monitors, which are of different resolution (e.g. a 32:9 5120x1440 + a 16:9 1920x1080 Monitor), then Ly will adjust to the size of the smallest monitor. This is not a Ly issue.

The tty terminals are set to the size of the smallest monitor, because the output is mirrored on each of these monitors. This can look ugly.

What cannot easily be done is that only one monitor shows the tty without permanently disabling it. However it is possible to adapt it to one monitor. If, e.g., your 32:9 monitor (examples from above) is your main monitor and your 16:9 monitor is just a side monitor, and you are fine with ignoring what is happening on your side monitor, you can adjust the resolution to the 32:9 monitor and Ly will scale accordingly. You need the resolution for it.

First make sure that `fbset` is installed

```
sudo pacman -S fbset
```

Now you need to set up a systemd service, which runs before Ly. What works is to run it after `sysinit.target`. If you need more fine grained control, use `systemd-analyze plot > startup_order.svg` to pick the exact point where you want to run the service.

```
cd /etc/systemd/system
nano setfont_tty.service
```

Now write this (adjust the resolution according to your target monitor, and adjust the ly service name):

```
[Unit]
Description=Set Terminal Screensize for Ly
After=sysinit.target

[Service]
Type=oneshot
ExecStart=/bin/bash/ -c "fbset -xres 5129 -yres 1440"

[Install]
WantedBy=ly@tty2.service
```

Finally enable the service

```
sudo systemctl enable setfont_tty.service
```

At next boot, Ly should appear at the right resolution in your main monitor. It will overflow on the other monitors.
