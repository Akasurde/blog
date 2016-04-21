Title: Command line hacks
Date: 2016-03-12 12:03
Modified: 2016-03-12 12:03
Category: gnome-terminal
Tags: gnome-terminal, bash, ls, dd, swap, shortcut, hacks, bash
Slug: gnome-terminal-hacks
Authors: Abhijeet Kasurde
Summary: Command line hacks

* Running previous command with sudo

   	<pre>$ ls -la
   	$ sudo !!</pre>

    **Usage**: This will run `ls -la` command using sudo command

* Using !! on shell prompt

   	<pre>$ ls -la a  && echo !!:2</pre>

    **Usage**: This will print a on screen.

* Finding top 5 largest files in directory

    <pre>$ ls -lSh . | head -5</pre>

* Finding top 5 smallest files in directory

   	<pre>$ ls -lSr . | head -5</pre>

* Finding top 10 directories in /

   	<pre>$ du -a /var | sort -n -r | head -n 10</pre>

* Finding top directories in /

   	<pre>$ du -ch --max-depth 1 /</pre>

* Using !! to replace some part of command

   	<pre>$ echo "foo"
   	$ !!:gs/foo/bar</pre>

    **Usage**: Runs previous command replacing `foo` by `bar` every time that `foo` appears in previous command

* Using !$, !^, !*

   	<pre>$ echo foo bar baz
   	$ echo !$ # will return baz
   	$ echo !^ # will return foo
   	$ echo !* # will return foo bar baz</pre>

* Press ESC + . to copy last argument of bash command

   	<pre>$ cp /from/same/path/file /to/some/path
   	$ cd [ESC + . ] # This will take you to /to/some/path</pre>

* Tail to dmesg

   	<pre>$ watch 'dmesg | tail -10'</pre>

* To determine if you have a process holding an unlinked file open

   	<pre>$ lsof -a +L1 path_of_directory</pre> or
	<pre>$ lsof +D +L1 path_of_directory</pre>

* Find the directory which takes highest space in root

   	<pre>$ du --max-depth=1 -h</pre>

* Report XSI interprocess communication facilities status

   	<pre>$ ipcs -s # for seamphore</pre>
   	<pre>$ ipcs -q # for message queues</pre>
   	<pre>$ ipcs -m # for shared memory segments</pre>

* Delete till last word in gnome-terminal

   	<pre> CRTL + w </pre>

* Go to start of line in gnome-terminal

    <pre>CTRL + a</pre>

* Delete single word on gnome-terminal

    <pre>ALT + BACKSPACE</pre>

* Ask Linux to rescan the SCSI devices on that FC HBA

    <pre>$ echo - - - >/sys/class/scsi_host/host$NUMBER/scan</pre>

    **Usage**: The wildcards “- - -” mean to look at every channel, every target, every LUN.

* Taking diff of directory

    <pre>$ diff -bur directory_2 directory_1</pre>

* Executing multiple commands using xargs

    <pre>$ echo 1 | xargs -I{} sh -c "echo {} && echo {}"</pre>

    **Usage**: Here xargs will take arguments in {}, replace {} in next shell prompt

* Force running logrotate configuration file

    <pre>$ logrotate --force /etc/logrotate.d/nginx</pre>

* Check permissions of file or directory

    <pre>$ stat /var/lib/kdcproxy| sed -n '/^Access: (/{s/Access: (\([0-9]\+\).*$/\1/;p}'</pre>

* Find which process owns port number

    <pre>$ fuser -v -n tcp port_number</pre>

    **Usage**: fuser -v -n tcp 6000

* List used ports

    <pre>$ lsof -i protocol_name:port_number</pre>

    **Usage**: `lsof -i tcp:80` checks apache running on port number 80 or not

* Get blocks and partitions

    <pre>$ egrep -v "#blocks|^$" /proc/partitions|awk '{print $3,  $4}'</pre>

* More swap with a swap file

   	<pre>$ dd if=/dev/zero of=/swapfile bs=1024 count=65536 #Create 64MB swap file on your root partition
   	$ mkswap /swapfile 65536          #convert file to swap file
   	$ sync
   	$ swapon /swapfile        #add swapfile to your swapspace</pre>

* Create file of 1 TB file with 8192 blocksize

   	<pre>$ dd if=/dev/zero of=/mnt/disk8 bs=8192 seek=134217728 count=0</pre>

* Post data using curl

	<pre>$ curl http://10.209.103.136:443 -d 'hostname=blah' -X POST -v</pre>

