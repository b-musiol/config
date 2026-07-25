# Default opening with scale down and start at

`feh` usually opens any file as is and does not scale up or down.

If the image is too large but it should be scaled, so it fits into the window, you need the option `--scale-down`

```
$ feh --scale-down <file>
```

Per default, `feh` opens just the file. But it can also just start at the file and then allow moving through the folder with `--start-at <file>`

```
$ feh --start-at <file>
```

Together:

```
$ feh --scale-down --start-at <file>
```

To now make it start if you, e.g., double click on the file in thunar or hit Enter in Midnight Commander, the config for `xdg-open` must be adjusted. Additionally, because that config cannot accept arguments, we need a `feh_scaled.desktop` file in `~/.local/share/applications`

```
[Desktop Entry]
Type=Application
Name=Feh (--scale-down)
Exec=feh --scale-down --start-at %f
MimeType=image/jpeg;image/ong;image/gif;image/webp;image/heic
NoDisplay=true
```
With this we can adjust `~/.config/mimeapps.list` by adding the following entries to `[Default Applications]` (if such an entry with the mime-type exists, replace it)

```
image/jpeg=feh_scaled.desktop
image/png=feh_scaled.desktop
image/gif=feh_scaled.desktop
image/webp=feh_scaled.desktop
image/heic=feh_scaled.desktop
```
