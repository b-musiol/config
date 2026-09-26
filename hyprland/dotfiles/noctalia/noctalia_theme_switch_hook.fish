#!/usr/bin/fish

########### Paths

## Alacritty
set alacritty_config_folder ~/.config/alacritty/
set alacritty_config_live alacritty.toml
set alacritty_config_dark alacritty_dark.toml
set alacritty_config_light alacritty_light.toml

## btop
set btop_config_folder ~/.config/btop/
set btop_config_live btop.conf
set btop_config_dark btop_dark.conf
set btop_config_light btop_light.conf

############ General in all themes pre
noctalia msg wallpaper-random

############ Per Theme
if test $NOCTALIA_THEME_MODE = "dark"
    cp $alacritty_config_folder$alacritty_config_dark $alacritty_config_folder$alacritty_config_live
    cp $btop_config_folder$btop_config_dark $btop_config_folder$btop_config_live
    # alacritty --hold -e fish -c 'echo "DEBUG NOCTALIA HOOK: dark mode"'
else if test $NOCTALIA_THEME_MODE = "light"
    cp $alacritty_config_folder$alacritty_config_light $alacritty_config_folder$alacritty_config_live
    cp $btop_config_folder$btop_config_light $btop_config_folder$btop_config_live
    # alacritty --hold -e fish -c 'echo "DEBUG NOCTALIA HOOK: light mode"'
end

############ General in all themes post
pkill -USR2 btop