# Scrapy settings for cheerego project
BOT_NAME = 'cheerego'

SPIDER_MODULES = ['cheerego.spiders']
NEWSPIDER_MODULE = 'cheerego.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cheerego (+http://www.yourdomain.com)'

# Initialize Django web framework for data store
# Use environment variable PYTHONPATH for abspath to Django project
# and DJANGO_SETTINGS_MODULE for Settings filename of Django project
try:
    import django
    django.setup()
except ImportError:
    # Allow to work without Django
    pass

ITEM_PIPELINES = {
    'cheerego.pipelines.CheeregoPipeline': 300,
}

