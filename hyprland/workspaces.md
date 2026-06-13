To set up workspaces, first find out which monitors you have with

```
hyprctl monitors | less
```

Use `less`, because the output might be large.

Note which connections (e.g. `DP-1`) the monitors are set to. With that you can edit your `.conf` file (if you are using KoolDots, put it under `~/.config/hypr/UserConfigs/UserSettings.conf`.

There you add lines like

```
workspace = 1, monitor:DP_1, layout:master
```

for each workspace that you number through. Save and if necessary, reload hyprland.
