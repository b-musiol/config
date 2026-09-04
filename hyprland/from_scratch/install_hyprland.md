This has been done for hyprland 0.56.2

Dotfiles are available separately in this repo.

# Install

After installing CachyOS without a desktop, run

```
sudo pacman -S hyprland ttf-noto-nerd alacritty noctalia firefox btop thunar mc xdg-desktop-portal-hyprland ly pipewire wireplumber grim slurp hyprpicker hyprlock hypridle git
```

## Fonts

If all you see are blocks, you have no proper fonts. You need a nerd-font. Here is one possibility:

```
sudo pacman -S ttf-noto-nerd
```

Relaunch hyprland afterwards to see text rendered.

# Get dotfiles

Clone this repository.

Copy the following files in the following folders (create folders if they do not exist):

```
hyprland/dotfiles/hyprland.lua -> ~/.config/hypr/hyprland.lua
hyprland/dotfiles/alacritty/alacritty.toml -> ~/.config/alacritty/alacritty.toml
hyprland/dotfiles/fastfetch/config.jsonc -> ~/.config/fastfetch/config.jsonc
hyprland/dotfiles/fish/config.fish -> ~/.config/fish/config.fish
hyprland/dotfiles/noctalia/settings.toml -> ~/.config/noctalia/settings.toml
hyprland/dotfiles/noctalia/palettes/Carmine.json -> ~/.config/noctalia/palettes/Carmine.json
hyprland/gtk-themes/Material-Black-Carmine-strong/ -> ~/.themes/Material-Black-Carmine-strong
```

## Adjusting hyprland.lua

Change the following block to match your monitor configuration:

```
local wide_monitor = "DP-1"
local side_monitor = "DP-3"


hl.monitor({
    output = wide_monitor,
    mode = "5120x1440@165.0",
    position = "0x190",
    scale = 1.0
})
hl.monitor({
    output = side_monitor,
    mode = "1920x1080@60.0",
    position = "5120x0",
    scale = 1.0,
    transform = 1
})
```

To find out which monitors to put, first figure out which are connected. For this `cd` to `/sys/class/drm` and for each `card%-*` folder `cat` the file `status` and check which are connected. Then you can do `hwinfo --monitor` to see which mode to put.

Also change the workspaces in the below part to point to the correct monitors, especially when you only have one monitor.

```
for i = 1, 4 do
    hl.workspace_rule({workspace = i, monitor=wide_monitor, layout="master", persistent=true})
end
for i = 5, 8 do
    hl.workspace_rule({workspace = i, monitor=side_monitor, layout="dwindle", persistent=true})
end
for i = 9, 10 do
    hl.workspace_rule({workspace = i, monitor=wide_monitor, layout="dwindle", persistent=true})
end
for i = 11, 12 do
    hl.workspace_rule({workspace = i, monitor=wide_monitor, layout="scrolling", persistent=true})
end
```

If you want to have no custom hyprcursor, delete/comment the following lines from `hyprland.lua`.

```
hl.env("XCURSOR_SIZE", "80")
hl.env("XCURSOR_THEME", "Nordzy-hyprcursors-dash")
hl.env("HYPRCURSOR_SIZE", "80")
hl.env("HYPRCURSOR_THEME", "Nordzy-hyprcursors-dash")
hl.env("HYPRCURSOR_THEME_DIRS", "~/.local/share/icons/")
```

# Set up ly

To log set up logging in with ly, execute
```
sudo systemctl disable getty@tty2
sudo systemctl enable ly@tty2
```

After a restart you log in with ly.

# Done

From here on out adjust further as necessary. Especially in Noctalia.
