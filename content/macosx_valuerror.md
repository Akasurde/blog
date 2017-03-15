Title: Python - UTF-8 ValueError
Date: 2017-03-17 12:03
Modified: 2016-03-17 12:03
Category: Python, MacOSX
Tags: Python, osx, mac, django, utf8, valueerror, locale
Slug: python-macosx-utf8-valuerror
Authors: Abhijeet Kasurde
Summary: Mac OS X: ValueError: unknown locale: UTF-8 in Python

If you get the error on MacOS X, here's the quick fix - add these lines to your `~/.bash_profile`:

<pre>
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
</pre>
