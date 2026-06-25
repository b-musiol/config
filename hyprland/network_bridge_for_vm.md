To set up network for a VM, you typically want to set up a bridge between your actual ethernet device and your VM.

First figure out which network devices exist

```
$ ip address show
```

Remember the name of your ethernet device (e.g. `eno1`).

Now set up the bridge device. Choose a name for it. Enumerating `bri` is a possible scheme. This is the virtual ethernet port that you will provide to your VM.

```
# ip link add bri1 type bridge
```

Finally connect the real ethernet port to the bridge

```
# ip link set eno1 master bri1
# ip link set bri1 up
```

Now you can pass the bridge device `bri1` to your VM.

