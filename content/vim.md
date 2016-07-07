Title: Vim cheatsheet - Part I
Date: 2016-05-18 12:03
Modified: 2016-05-18 12:03
Category: vim
Tags: vim, hacks, cheatsheet
Slug: vim-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Vim command - Cheatsheet

* Read command output to current line

    <pre>:read ! command </pre>

* Open file under cursor

    <pre><kbd>ESC</kbd> + gf</pre>

* Create heading 1 in markdown

    <pre>:map h1 yypVr=o</pre>

* Create heading 2 in markdown

	<pre>:map h2 yypVr-o</pre>

* Replace content from current file to end of file

	<pre>:.,$s/pattern1/pattern2/gc</pre>

* Change certain number of lines from current line

	<pre>:.,.+<number>s/pattern1/pattern2/gc</pre>

    **Usage** : `:.,.+4s/foo/bar/gc` # this is will replace foo to bar
                from current line to next 4 lines.

* Creating mark

    <pre><kbd>ESC</kbd> + m + key_name </pre>

* Return to mark

    <pre><kbd>ESC</kbd> + ' + key_name </pre>

* Deleting everything from paraenthese or ()

    <pre><kbd>ESC</kbd> + di( </pre>

* Using temporary buffers

    <pre><kbd>ESC</kbd> + "a4yy </pre>
    <pre><kbd>ESC</kbd> + "ap </pre>

* Using <kbd>F5</kbd> to automatically remove all trailing spaces in code

    <pre>nnoremap &lt;F5&gt; :let _s=@/&lt;Bar&gt;:%s/\s\+$//e&lt;Bar&gt;:let @/=_s&lt;Bar&gt;&lt;CR&gt;</pre>

* Go to specific character on current line. If you want to go to first occurance of '=' then

    <pre><kbd>ESC</kbd>f + = </pre>
