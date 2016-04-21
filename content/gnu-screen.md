Title: gnu-screen cheatsheet
Date: 2016-02-12 12:03
Modified: 2016-02-12 12:03
Category: gnu-screen
Tags: gnu-screen, shortcut, hacks
Slug: gnu-screen-hacks
Authors: Abhijeet Kasurde
Summary: GNU screen hacks and cheatsheet

**All commands are inside screen **


* Open new window

    <kbd>Ctrl</kbd>+<kbd>a</kbd>+<kbd>c</kbd>

* Close windows in screen

	<kbd>CTRL</kbd>+<kbd>a</kbd>+<kbd>k</kbd>

* Detaching the screen (Coming to normal non-screen window)

	<kbd>CTRL</kbd> +<kbd>a</kbd>+<kbd>d</kbd>

* GoTo next windows

	<kbd>CTRL</kbd>+<kbd>a</kbd>+<kbd>n</kbd>

* Goto previous windows

	<kbd>CTRL</kbd>+<kbd>a</kbd>+<kbd>p</kbd>

* Show list of windows

	<kbd>CTRL</kbd> +<kbd>a</kbd>+<kbd>Shift</kbd>+<kbd>"</kbd>

* Split panes

	 <kbd>CTRL</kbd> +<kbd>a</kbd>+<kbd>Shift</kbd>+<kbd>s</kbd>

* Toggle between split panes

	 <kbd>CTRL</kbd>+<kbd>a</kbd>+<kbd>Tab</kbd>

* Closing split panes

	 <kbd>CTRL</kbd>+<kbd>a</kbd>+<kbd>Shift</kbd>+<kbd>x</kbd>

* Locking the screen

	 <kbd>CTRL</kbd> +<kbd>a</kbd>+<kbd>x</kbd> # Enter password for locking and unlocking

* Fancy hardstatus

	<pre>$ vi /etc/screenrc</pre>
    <pre>hardstatus on
	hardstatus alwayslastline
	hardstatus string "%{.bW}%-w%{.rW}%n %t%{-}%+w %=%{..G} %H %{..Y} %m/%d %C%a "</pre>

* Reattaching the screen

	<pre>$ screen -R</pre>

