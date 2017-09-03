Title: Any and All
Date: 2017-09-01 12:03
Modified: 2017-09-01 12:03
Category: any, all, python
Tags: any, all, python
Slug: any-all-python
Authors: Abhijeet Kasurde
Summary: Test truth values of iterable

Python provides two functions that deal with iterable and return `True` or `False`
depending on which boolean values elements of the sequence evaluate to.

* All

`all(iterable)` returns `True` if all elements of an iterable are considered as true values 

e.g., 
```python
all(l == 'y' for l in 'Python') # Returns False. Not all of the letters are 'y'.
```

* Any

`any(iterable)` returns `True` if at least one element of the iterable is a true value


e.g.,

```python
any(l == 't' for l in 'python') # Returns True. Same as: 't' in 'python'
```
