To use JACK (e.g. with Ardour) it can be advantageous to open it manually and let ardour use that.

Take note, if you are running a rt (realtime) kernel or not.

Consider installing `jack2-dbus` to gracefully borrow and return hardware from pipewire.

# Opening JACK

To open JACK use the following command

```
jackd -R -v -d alsa -d hw:0 -r 192000 -p 256 -n 3
```

If you are not running a rt-kernel, omit `-R`.

Check if you really need `hw:0` or a different soundcard with

```
cat /proc/asound/cards
```

With that in mind, check what sample rate in Hz you need after `-r`.

With `-p` (samples per period) and `-n` (periods in buffer) you set up the latency in tradeoff with the performance requirements. Increase either if the audio is unstable.
