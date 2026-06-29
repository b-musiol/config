This has been done for hyprland 0.55

Dotfiles are available separately.

# Install

After installing Arch Linux, run

```
# pacman -S hyprland
```

## Fonts

If all you see are blocks, you have no proper fonts. You need a nerd-font. Here is one possibility:

```
# pacman -S ttf-noto-nerd
```

Relaunch hyprland afterwards to see text rendered.

## Accompanying Applications

Hyprland "needs" additional packages to run. There are usually choices for each. Here is my current setup.

```
# pacman -S hyprpolkitagent awww dunst rofi thunar pipewire wireplumber xdg-desktop-portal-hyprland pavucontrol nwg-bar playerctl hyprlock wl-clipboard ly quickshell firefox
```
