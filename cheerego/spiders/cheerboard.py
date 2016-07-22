import scrapy
from cheerego.items import CheeregoItem
from datetime import datetime


class CheerboardSpider(scrapy.Spider):
    name = "cheerboard"
    allowed_domains = ["cheerego.com"]
    start_urls = (
      'http://cheerego.com/dome_web/guest.php',
    )

    def parse(self, response):
      hxs = scrapy.selector.Selector(response)
      msg = hxs.xpath('//div[contains(@class,"reply_content_demo")]/text()').extract()
      if (msg > 0):
        fullmsg = ''
        for i in msg:
          fullmsg += i
        cheer = CheeregoItem()
        cheer['scraptime'] = datetime.now()
        cheer['posttime'] = cheer['scraptime']
        cheer['poster'] = u'cheer'
        cheer['message'] = fullmsg
      return cheer
