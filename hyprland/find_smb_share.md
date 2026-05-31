# Mount with fstab

You will need `cifs-utils`.

To mount a smb share automatically, first create a `credentials` file. You only need one per account, so if you mount multiple from one share, you can reuse it.

```
username=...
password=...
```

Make sure `credentials` can only be read by the user and root with `chmod 600 credentials` when in the folder where the file is.

Make the folder to mount at. This can be anywhere but to keep it tidy, make it in `/mnt`. You can make a subfolder for the share itself and then subfolders in that for the folders on that share if you want. `/mnt/<share_name>/<folder_name>`

Run `id -u` and `id -g` and note the output, these are your `uid` and `gid`.

Now open fstab with `sudo <editor> /etc/fstab`

Add the following line per folder on the share:

```
//<url_to_share/<folder_name>  /mnt/<share_name>/<folder_name>  cifs  credentials=<path_to_credentials_file>,uid=<your_uid>,gid=<your_gid>,iocharset=utf8,nofail,vers=<2.0_or_3.0>  0  0
```

You may need to try both `vers=2.0` and `vers=3.0` depending on your share.

Test with `sudo mount -a`.

If that works, test with reboot.

If that works, it will automount at startup.

You can make a file manager bookmark to `/mnt/<share_name>`.

# thunar

To find a smb share in Thunar, install `gvfs-smb` via `pacman -S`.

Now you can go to `smb://<location>`

You can set a bookmark.
