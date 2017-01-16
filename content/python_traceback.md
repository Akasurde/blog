Title: Python - Traceback module
Date: 2017-01-16 12:03
Modified: 2016-01-16 12:03
Category: Python, traceback
Tags: Python, Traceback, module
Slug: python-traceback-module
Authors: Abhijeet Kasurde
Summary: Python - Traceback module

How to print current call stack for debugging purpose

<pre>import traceback
def f():
    g()
def g():
    for line in traceback.format_stack():
        print(line.strip())
f()</pre>

It gives output as follows : 

<pre>
# Prints:
# File "example_tracestack.py", line 10, in <module>
#     f()
# File "example_tracestack.py", line 4, in f
#     g()
# File "exampel_tracestack.py", line 7, in g
#     for line in traceback.format_stack():</pre>
