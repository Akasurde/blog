Title: Fibonacci Python Codes
Date: 2017-08-31 12:03
Modified: 2016-08-31 12:03
Category: python, dynamic programming, algorithms, fibonacci
Tags: python, dynamic programming, algorithms, fibonacci
Slug: fibonacci
Authors: Abhijeet Kasurde
Summary: A few Fibonacci Python implementations


* Using recursion

```Python
def fib2(n):
    if n <= 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
```

* Using existing data

```python
def fib(n):
    fibValues = [0, 1]
    for i in range(2, n+1):
        fibValues.append(fibValues[i-1] + fibValues[i-2])
    return fibValues[n]
```

* Using dictionary

```python
fib_data = {1:1, 2:1}
def fib3(n):
    print(fib_data)
    print(n)
    if n <= 2:
        return 1
    if n in fib_data:
        return fib_data[n]
    else:
        fib_data[n] = fib3(n-1) + fib3(n-2)
        return fib_data[n]
```

* Using memorization decorator

```python
def memorize(f):
    cache = {}
    def memorizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    memorizedFunction.cache = cache
    return memorizedFunction

@memorize
def fib4(n):
    if n <= 2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)
```

* The ugly way

```python
fib5_data = [0, 1]
def fib5(n):
    if n <= 1:
        return fib5_data[n]
    try:
        if fib5_data[n]:
            return fib5_data[n]
    except:
        for i in range(len(fib5_data), n+1):
            fib5_data.append(fib5_data[i-1] + fib5_data[i-2])
        return fib5_data[n]
```

* Another way

```python
def fib6(n):
    a, b = 0, 1
    for i in range(n):
        b, a = a, a+b
    return a
```


Some of the code is shamelessly copied from [Jeremy Kun's Blog](https://jeremykun.com/2012/01/12/a-spoonful-of-python/)