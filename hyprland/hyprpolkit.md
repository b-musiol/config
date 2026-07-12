There are situations where polkit is installed and hyprpolkitagent as well, but hyprpolkitagent is not running in systemd.

In this case run
```
systemctl --user start hyprpolkitagent
```

To make this run each time you log in:

```
systemctl --user enable hyprpolkitagent
```
