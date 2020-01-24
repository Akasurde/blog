# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Abhijeet Kasurde'
SITENAME = u'http://akasurde.github.io'
SITEURL = ''
SITETITLE= "Abhijeet Kasurde"
SITESUBTITLE = "Developer, Hacker"
SITELOGO="https://pbs.twimg.com/profile_images/598341193336954882/HHxz7Y7G.png"
THEME="./Flex"
PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = u'en'
COPYRIGHT_YEAR = 2020
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HOMEURL = "https://akasurde.github.io"

SOCIAL = (('github', "https://github.com/akasurde"),
          ('twitter', 'https://twitter.com/Pyro46'),
          ('linkedin', 'https://www.linkedin.com/in/abhijeet-kasurde-baab8519'),
          ('stack-overflow', 'http://stackoverflow.com/users/1075324/abhijeet-kasurde'),
         )
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
#LINKS = (('Open Source For You', 'http://opensourceforu.com/author/abhijeet-kasurde/'),
#        )


CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

GOOGLE_ANALYTICS='UA-76778737-1'
DISQUS_SITENAME = "akasurdegithubio"
