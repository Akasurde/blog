Title: Grep command
Date: 2016-01-1 12:03
Modified: 2016-01-1 12:03
Category: grep
Tags: grep, hacks, cheatsheet
Slug: grep-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Grep command - Cheatsheet

* Search file for keyword `Error`

    <pre>$ grep "Error" mylogfile.log</pre>

* Search file for keyword `Error` with case-insensitivity

    <pre>$ grep -i "error" mylogfile.log</pre>

* Searching several words in file

    <pre>$ grep -Ei "error|exception|fatal" mylogfile.log</pre>

* See more after and more before keyword in file

    <pre>$ grep -A 10 -B 20 "exception" mylogfile.log</pre>

    **Usage**: Above grep will show 10 line after and 20 line before `exception` word in `mylogfile.log`

* Search file and line with filename

    <pre>$ grep -nrH MyMethodName *</pre>

    **Usage**: Above grep command will search files in current directory recursively with line and filename.

* Search keyword in file and print only filename

    <pre>$ grep -ril keyword location</pre>

    **Usage**: `grep -ril "*myword*"`

* Find keyword in file and print filename only

	<pre>$ grep -l "word" *</pre>
