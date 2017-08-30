Title: Palindrome
Date: 2017-08-30 12:03
Modified: 2016-08-30 12:03
Category: programming, alogrithms, palindrome
Tags: python, programming, alogrithms, palindrome
Slug: python
Authors: Abhijeet Kasurde
Summary: Palindrome

* Check if characters of a given string can be rearranged to form a palindrome or not

```
from collections import Counter
import pytest

def palindrome_detect(string):
    return len([e for e in Counter(string).values() if e % 2 == 1]) <= 1

# Testcases
@pytest.mark.parametrize(
    'string, palindrome',[
        ('aa', True),
        ('aabb', True),
        ('nniit', True),
        ('aaabbbccc', False),
        ('abc', False),
    ]
)
def test_sample(string, palindrome):
    assert palindrome_detect(string) == palindrome
```
