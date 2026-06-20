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
