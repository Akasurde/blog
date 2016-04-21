Title: dpkg
Date: 2016-01-11 12:03
Modified: 2016-01-11 12:03
Category: dpkg
Tags: dpkg, ubuntu, command-line
Slug: dpkg-cheatsheet
Authors: Abhijeet Kasurde
Summary: Quick cheat sheet you will find handy while using `dpkg` at shell prompt

* Installing deb file using dpkg

    <pre>$ dpkg -i <package_name>.deb</pre>

    **Usage**: `dpkg -i apache2_2.2.17-1ubuntu1.5_i386.deb`

* Installing deb packages recursively from given directory

	<pre>$ dpkg -R path_to_directory</pre>

    **Usage**: `dpkg -R /var/cache/apt/archives/`

* Find all files related to package

    <pre>$ dpkg -L package_name</pre>

    **Usage**: `dpkg -L apache2`

* List all package by name

    <pre>$ dpkg -l | grep package_name</pre>

    **Usage**: `dpkg -l | grep apache2`

* Find which package is related to particular file

    <pre>$ dpkg -S file_name</pre>

    **Usage**: `dpkg -S /etc/apache2/apache2.conf`

* Find status of package

    <pre>$ dpkg -s <package_name> | grep Status</pre>

    **Usage**: `dpkg -s apache2 | grep Status`

* Display details about package package group, version, maintainer, Architecture, display depends packages, description etc.

	<pre>$ dpkg -p package_name</pre>

    **Usage**: `dpkg -p apache2`

* List files provided by given package

	<pre>$ dpkg -c deb_package_name</pre>

    **Usage**: `dpkg -c apache2_2.2.17-1ubuntu1.5_i386.deb`

* List individual package name installed with short description

	<pre>$ dpkg -l package_name</pre>

    **Usage**: `dpkg -l apache2`

* List all package name installed with short description

	<pre>$ dpkg -l</pre>

    **Usage**: `dpkg -l`

* Remove package

	<pre>$ dpkg -r package_name</pre>

    **Usage**: `dpkg -r apache2`

* Remove package with all configuration

	<pre>$ dpkg -P package_name</pre>

    **Usage**: `dpkg -P apache2`
