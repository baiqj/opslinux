#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###########################################################
##                     Basic settings                    ##
###########################################################
SITEURL = 'http://opslinux.com'
AUTHOR = u'创e'
SITENAME = u'老运维创e'

DATE_FORMATS = {
    'zh': ('zh_CN', '%x'),
    'en': ('en_US', '%a, %d %b %Y'),
}



#SITEURL = ''
SITE_SOURCE = u"https://github.com/zbing3/opslinux.git"
SLUGIFY_ATTRIBUTE = 'filename'



DEFAULT_LANG = u'zhs'
USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE = "fs"

PAGE_DIR = 'pages'
PAGE_EXCLUDES = ()
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
GITHUB_URL = 'https://github.com/zbing3'

DEFAULT_CATEGORY = 'Blog'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (('未分类', 'test.html'), )

DEFAULT_METADATA = ()
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = ()
JINJA_EXTENSIONS = []
JINJA_FILTERS = {}
LOCALE = ('zh_CN', 'en_US')
READERS = {}
IGNORE_FILES = ['.#*']
OUTPUT_PATH = 'output/'
PATH = None
PAGE_DIR = 'pages'
ARTICLE_DIR = ''
ARTICLE_EXCLUDES = ('pages', 'drafts')
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
RELATIVE_URLS = False

TEMPLATE_PAGES = None
TIMEZONE = 'Asia/Shanghai'
# TYPOGRIFY = True
# 设置目录
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search', '404')
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc', 'fenced_code', 'footnotes']  
PAGINATED_DIRECT_TEMPLATES = ('index',)
SUMMARY_MAX_LENGTH = 50
ASCIIDOC_OPTIONS = []
WITH_FUTURE_DATES = False
INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}





STATIC_PATHS = [
    'extra/robots.txt',
    'extra/.htaccess',
    u'upload',
    'theme/images',
    'images'
]


EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/CNAME': {'path': 'CNAME'},
    # 'extra/search.html': {'path': 'search.html'},
    }
# Uncomment following line if you want document-relative URLs when developing

###########################################################
##                     URL settings                      ##
###########################################################

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# ARTICLE_URL = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/'
# ARTICLE_SAVE_AS = 'post/{date:%Y}-{date:%m}-{date:%d}-{slug}/index.html'

CATEGORY_URL = 'categories.html#{slug}-ref'
CATEGORY_SAVE_AS = ''
CATEGORIES_URL = 'categories.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAG_URL = 'tags.html#{slug}-ref'
TAG_SAVE_AS = ''
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'archives.html'
# YEAR_ARCHIVE_SAVE_AS = False
# MONTH_ARCHIVE_SAVE_AS = False

DEFAULT_PAGINATION = False
# ARTICLE_LANG_URL = '{slug}-{lang}.html'
# ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'

# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'
# PAGE_LANG_URL = '{slug}-{lang}'
# PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# CATEGORY_URL = 'category/{slug}/'
# # CATEGORY_URL = 'categories.html#{slug}-ref'
# CATEGORY_SAVE_AS = 'category/{slug}/index.html'
# CATEGORIES_URL = 'categories/'
# CATEGORIES_SAVE_AS = 'categories/index.html'

# TAG_URL = 'tag/{slug}/'
# # TAG_URL = 'tags.html#{slug}-ref'
# TAG_SAVE_AS = 'tag/{slug}/index.html'
# TAGS_URL = 'tags/'
# TAGS_SAVE_AS = 'tags/index.html'

# AUTHOR_URL = 'author/{slug}/'
# AUTHOR_SAVE_AS = 'author/{slug}/index.html'
# AUTHORS_URL = 'authors.html'
# AUTHORS_SAVE_AS = 'authors.html'

# ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = False

SLUG_SUBSTITUTIONS = ()






###########################################################
##                       Feed Settings                   ##
###########################################################

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://opslinux.com'
# FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_ATOM = 'feed/all.atom.xml'
FEED_RSS = 'rss.xml'
FEED_ATOM = None
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


###########################################################
##                       Pagination                      ##
###########################################################
DEFAULT_ORPHANS = 0 
# 每页文章数量
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = [
    (0, '{name}{number}.html', '{name}{number}.html'),
]

###########################################################
##                         Tag Cloud                     ##
###########################################################
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

###########################################################
##                   Translations                        ##
###########################################################
DEFAULT_LANG = 'zh'
TRANSLATION_FEED_ATOM = 'feed/all-%s.atom.xml'
TRANSLATION_FEED_RSS = None

###########################################################
##                      Ordering content                 ##
###########################################################
NEWEST_FIRST_ARCHIVES = True
REVERSE_CATEGORY_ORDER = False

###########################################################
##                        Theme                          ##
###########################################################
THEME = "pelican-elegant"
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

###########################################################
##                          Plugins                      ##
###########################################################
PLUGIN_PATH = 'plugins'
#加载plugins
PLUGINS = [
    'sitemap',
    'extract_toc',
    'tipue_search',
    'latex',
    'neighbors',
    # 'assets',
    'related_posts',
    'multi_part',
    'random_article',
]


#随机跳转到某一日志
RANDOM = 'random.html'
#相关文章
RELATED_POSTS_MAX = 10
#RST
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}



###########################################################
##                       Plugin: Sitemap                 ##
###########################################################
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


## Elegant Theme
RECENT_ARTICLES_COUNT = 15
# COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'
SITE_LICENSE = u'Copyright &copy; 2013-2014 <a href="http://opslinux.com"><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> 老运维创e</span></a>. All Rights Reserved. <a href="http://opslinux.com/rss.xml">网站地图</a> <a href="http://www.51.la/?16996417" target="_blank"><img alt="&#x6211;&#x8981;&#x5566;&#x514D;&#x8D39;&#x7EDF;&#x8BA1;" src="http://img.users.51.la/16996417.asp" style="border:none" /></a>'
SITE_DESCRIPTION = u'关注和分享python、linux。'
SITE_SUBTITLE = u'分享技术'
USE_SHORTCUT_ICONS = True

SITESUBTITLE = '分享技术'
#LANDING_PAGE_ABOUT
#PROJECTS

# MailChimp
# EMAIL_SUBSCRIPTION_LABEL = u'Get Weekly Updates'
# EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
# SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
# MAILCHIMP_FORM_ACTION = u'http://seisman.us3.list-manage1.com/subscribe/post?u=03bdd9e889c533d6db4dd0454&amp;id=dc5a50f619'

DISQUS_SITENAME = "opslinux"

## Social
SOCIAL = [
    {   
        'icon': 'GitHub',
        'title': 'GitHub主页',
        'url':  'http://github.com/zbing3'},
    {   
        'icon': 'envelope',
        'title': '电子邮件',
        'url': 'mailto:zbing3@163.com'},
    {   
        'icon': 'Weibo',
        'title': '新浪微博',
        'url': 'http://weibo.com/zb311'},
    {
        'icon': 'RSS',
        'title': 'RSS订阅',
        'url': SITEURL + "/" + FEED_ALL_ATOM},
    {
        'icon': 'CNY',
        'title': '捐赠本博',
        'url': 'http://opslinux.com/'},
]


# LINKS = (
#     ('Bebluesky', 'http://www.bebluesky.com/'),  # 快乐生活，幽它一默
#     ('Python俱乐部', 'http://www.pythonclub.org/'),  # 以提供Python知识为目标，原创并收集Python编程相关的知识
#     ('东华博客', 'http://www.truevue.org/'),  # 关注生活，关注科技，关注互联网，了解互联网，了解科技，了解生活！
#     ('阅微堂', 'http://zhiqiang.org/blog/'), # 数学、金融、计算机
#     ('Pelican', 'http://getpelican.com/'),
#     ('Python.org', 'http://python.org/'),
#     ('Jinja2', 'http://jinja.pocoo.org/'),
# )

SOCIAL = (
    ('Email', 'mailto:zbing3@163.com'),
    ('Weibo', 'http://weibo.com/zb311'),
    ('Github', 'https://github.com/zbing3'),
    ('RSS', SITEURL + "/" + FEED_ALL_ATOM),

    # ('Facebook', 'https://www.facebook.com/calfzhou'),
    # ('Twitter', 'https://twitter.com/calfzhou'),
)

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)




#静态页面
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),('extra/404.shtml', '404.shtml'),('extra/search.html', 'search.html'),)






