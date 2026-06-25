There are a few things that need to be done in order to make VMs work on Linux

The QEMU socket must be started

```
# systemctl start virtqemud.socket
```

The storage pools must be enabled

```
# systemctl start virtstoraged.socket
```
