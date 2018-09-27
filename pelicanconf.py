#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Franklin'
SITENAME = u'Franklin is Blogging'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Robotics Software Engineer, Part time Trader,  Consultant'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
PATH = 'content'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

TIMEZONE = 'Europe/Paris'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('Portfolio', 'http://yang2lalang.github.io'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/franklinokoli/'),
          ('github', 'https://github.com/yang2lalang'),
          ('researchgate', 'https://www.researchgate.net/profile/Franklin_Okoli'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
STATIC_PATHS = ['images']
PLUGIN_PATH = './plugins/pelican-plugins'
PLUGINS = ['sitemap', 'post_stats','i18n_subsites']
IGNORE_FILES = ['.ipynb_checkpoints']
THEME = './themes/Flex'


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "http-yang2lalang-github-io"
ADD_THIS_ID = 'ra-5bac97e477d3d598'

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-9421131783612830',
    'page_level_ads': True,
    'ads': {
        'aside': '5340595560',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '9584371569',
        'article_top': '',
        'article_bottom': '7257980762',
    }
}
