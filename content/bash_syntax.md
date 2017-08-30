Title: Bash Scripting Syntax
Date: 2016-06-07 12:03
Modified: 2016-06-07 12:03
Category: bash, scripting, command line
Tags: bash, shell, scripting, command line
Slug: bash-syntax-cheat-sheet
Authors: Abhijeet Kasurde
Summary: Bash scripting syntax cheatsheet

* Compare integer in bash, (for avoiding error : `unary operator expected error`)

<pre>
if [[ $i -ge 2 ]]
</pre>

* Number tables (for loop example)

<pre>
for i in {1..9};
do
    for j in $(seq 1 9);
    do
        echo -ne $i×$j=$((i*j))\\t;
    done;
    echo;
done
</pre>

* Test of variable is a number in bash shell script

<pre>
re='^[0-9]+$'
if ! [[ $yournumber =~ $re ]] ; then
    echo "error: Not a number" >&2;
    exit 1
fi
</pre>

* Remove last character of variable

<pre>
something="myname"
echo ${something%?}
</pre>

* Removing first character of variable

<pre>
something="myname"
echo ${something#?}
</pre>

* Using nested variable in bash

<pre>
array=(1 2 3 4 5)
for i in ${array[@]}
do
    v=$(printf "str%s" $i)
    echo $v
done
</pre>

* Redirecting eval to log file

<pre>
eval ls 2>&1 > /tmp/av.log
</pre>

* Converting variable string into lower case using bash

<pre>
REALM="Sample.Example.COM"
echo $REALM
echo ${REALM,,}
</pre>
