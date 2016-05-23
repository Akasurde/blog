Title: Using IFS in Bash for-loop
Date: 2016-05-23 12:03
Modified: 2016-05-23 12:03
Category: Shell Scripting, Bash, for-loop
Tags:  shell, bash, scripting, for
Slug: using-ifs-in-bash-for-loop
Authors: Abhijeet Kasurde
Summary: Using IFS variable in Bash for loop


While using for loop in Shell scripting, there are times when you want to use
filenames or variables with spaces

like

    # firewall-cmd --list-rich-rule
      rule family="ipv4" source address="192.168.122.1" forward-port port="80" protocol="tcp" to-port="8188"

    # for i in `firewall-cmd --list-rich-rule`; do echo $i ; done

      rule
      family="ipv4"
      source
      address="192.168.122.1"
      forward-port
      port="80"
      protocol="tcp"
      to-port="8188"

But, you want whole command output in single variable. Then, IFS will come to your help. First, replace IFS environment variable to new line character.

    # OLDIFS=$IFS
    # IFS=$"\n"

Notice that we are storing IFS in variable with `$"\n"`. Read more about this [here](http://www.gnu.org/software/bash/manual/bash.html#ANSI_002dC-Quoting)

Now, script looks like this

    # OLDIFS=$IFS
    # IFS=$"\n";
    # for i in `firewall-cmd --list-rich-rule`; do  echo $i ; done
    # IFS=$OLDIFS

And, you are done.

Output is something like this,

    rule family="ipv4" source address="192.168.122.1" forward-port port="80" protocol="tcp" to-port="8188"
