#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'皓禹'
SITENAME = u'老运维人员'
SITEURL = 'http://opslinux.com'
#SITEURL = ''
SITE_SOURCE = u"https://github.com/zbing3/opslinux.git"
SLUGIFY_ATTRIBUTE = 'filename'
ARTICLE_URL = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'
TIMEZONE = 'Asia/Shanghai'
THEME = "JekyllBootstrap4Pelican"
DEFAULT_LANG = u'zhs'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = "fs"
DISQUS_SITENAME = "codenut"
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ()
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
GITHUB_URL = 'https://github.com/zbing3'
#默认分类
DEFAULT_CATEGORY = 'Blog'
# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://opslinux.com'
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM  = None
TAG_FEED_RSS  = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS  = None
FEED_MAX_ITEMS = 20
#标签设置
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50
# 生成PDF选项
PDF_GENERATOR = False
PDF_STYLE = 'styles.style'
PDF_STYLE_PATH = ''
# 日期格式
DATE_FORMATS = {
        'en': '%a, %d %b %Y',
        'zhs': '%Y-%m-%d',
}
# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/zbing3'),
          ('weibo', 'http://weibo.com/zb311'),)


# 每页文章数量
DEFAULT_PAGINATION = 10
#静态页面
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),('extra/404.shtml', '404.shtml'),('extra/search.html', 'search.html'),)
FILES_TO_COPY = (('extra/search.html', 'search.html'),)
STATIC_PATHS = [u"upload"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#加载plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["sitemap","neighbors","random_article","related_posts"]
#sitemap
SITEMAP = {
        'format': 'xml',
        'priorities': {
                    'articles': 0.7,
                    'indexes': 0.8,
                    'pages': 0.5
                },
        'changefreqs': {
                    'articles': 'monthly',
                    'indexes': 'daily',
                    'pages': 'monthly'
                }
}
#随机跳转到某一日志
RANDOM = 'random.html'
#相关文章
RELATED_POSTS_MAX = 10
