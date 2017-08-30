Title: Using IFS in Bash forloop
Date: 2016-05-23 12:03
Modified: 2016-05-23 12:03
Category: Shell Scripting, Bash, forloop
Tags:  shell, bash, scripting, for
Slug: using-ifs-in-bash-for-loop
Authors: Abhijeet Kasurde
Summary: Using IFS variable in Bash for loop


While using for loop in Shell scripting, there are times when you want to use
filenames or variables with spaces like

<pre>
$ firewall-cmd --list-rich-rule
rule family="ipv4" source address="192.168.122.1" forward-port port="80" protocol="tcp" to-port="8188"

$ for i in `firewall-cmd --list-rich-rule`; do echo $i ; done

rule
family="ipv4"
source
address="192.168.122.1"
forward-port
port="80"
protocol="tcp"
to-port="8188"
</pre>


But, you want whole command output in single variable. Then, IFS will come to your help. First, replace IFS environment variable to new line character.

<pre>
OLDIFS=$IFS
IFS=$"\n"
</pre>


Notice that we are storing IFS in variable with `$"\n"`. Read more about this [here](http://www.gnu.org/software/bash/manual/bash.html#ANSI_002dC-Quoting)

Now, script looks like this

<pre>
OLDIFS=$IFS
IFS=$"\n";
for i in `firewall-cmd --list-rich-rule`; do  echo $i ; done
IFS=$OLDIFS
</pre>

And, you are done.

Output is something like this,

<pre>
rule family="ipv4" source address="192.168.122.1" forward-port port="80" protocol="tcp" to-port="8188"
</pre>
