Noctalia is great

# V5

Get yay or paru first. Noctalia is only on the AUR (or on git). ALWAYS CHECK THE DIFFS!

`yay -S noctalia-git`
`paru -S noctalia-git`

Then in `~/.config/hypr/hyprland.lua`

```
hl.on("hyprland.start", function()
  -- there is probably stuff here, so append
  hl.exec_cmd("noctalia --daemon")
end)
```

On next restart, hyprland will launch with Noctalia.
