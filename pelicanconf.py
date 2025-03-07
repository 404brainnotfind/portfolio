AUTHOR = 'Hui Miao'
SITENAME = "Hui Miao's Portfolio"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Winnipeg'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/404brainnotfind"),
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'favicon.ico']
EXTRA_PATH_METADATA = {'favicon.ico': {'path': 'favicon.ico'}}

ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

THEME = 'pelican-themes/simple-bootstrap'
RELATIVE_URLS = True

# 显示页面菜单
DISPLAY_PAGES_ON_MENU = True
