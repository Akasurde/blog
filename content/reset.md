Title: Reset root password in CentOS 7
Date: 2016-04-25 12:03
Modified: 2016-04-25 12:03
Category: System Administration
Tags: root, CentOS
Slug: reset-root-password-centos7
Authors: Abhijeet Kasurde
Summary: Article about resetting root password in CentOS 7

Following steps will guide you in resetting root password

* Restart the CentOS 7 system

* Press any key to interrupt the boot loader countdown

* Select Linux Kernel line which needs to be booted

* Press <kbd>e</kbd> to edit the select Linux Kernel entry

* Append `rd.break` at end of `linux16` line

* Press <kbd>CTRL</kbd> + <kbd>x</kbd> to boot system

* Mount /sysroot in read-write mode

    <pre>switch_root:/# mount -oremount,rw /sysroot</pre>

* Switch into a chroot jail environment

    <pre>switch_root:/# chroot /sysroot</pre>

* set a new root password

    <pre>sh-4.2# passwd root</pre>

* To enable SELinux relabeling of `/etc/shadow` file, create a empty file like

    <pre>sh-4.2# touch /.autorelabel</pre>

* Press `exit` twice to exit `chroot` and `initrdramfs` shell
