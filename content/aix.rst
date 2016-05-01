Title: AIX Command line hacks
Date: 2016-01-23 12:03
Modified: 2016-01-23 12:03
Category: command-line
Tags: AIX
Slug: aix-commandline
Authors: Abhijeet Kasurde
Summary: Few handy AIX Command line hacks

* Reset the NIM client machine state from NIM server

    <pre># nim -Fo reset hostname</pre>

    **Usage**: `$ nim -Fo reset dbaix1-v8`

	This is will reset NIM client dbaix1-v8 to ready state

* Deallocate resources from NIM client from NIM server

    <pre># nim -Fo deallocate -a lpp_source=LPP_61TL7SP5 dbaix2-v10</pre>

* Remove NIM client from NIM server

    <pre># nim -Fo remove hostname</pre>

* List down all NIM client form NIM server

    <pre># lsnim -l</pre>

* List down properties of particular NIM client from NIM server

    <pre># lsnim -l hostname</pre>

* Increase file system size by 1 GB

    <pre># chfs -a size=+1G /opt</pre>

* Decrease file system by 1 GB

    <pre># chfs -a size=-1G /opt</pre>

* List Fibre Card adapter

    <pre># lsdev -Cc adapter_name</pre>

* Get Fibre Card WWPN number

    <pre># lscfg -v1 adapter_name</pre>

* Get statistics for Fibre Card adapter

	<pre># fcstat adapter_name</pre>
