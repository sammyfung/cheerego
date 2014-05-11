# Scrapy settings for cheerego project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cheerego'

SPIDER_MODULES = ['cheerego.spiders']
NEWSPIDER_MODULE = 'cheerego.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cheerego (+http://www.yourdomain.com)'

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","cheerdb.settings")
path = os.path.join(os.path.dirname(__file__),'../cheerdb')
sys.path.append(os.path.abspath(path))
from django.conf import settings

ITEM_PIPELINES = {
  'cheerego.pipelines.CheeregoPipeline': 300,
}

