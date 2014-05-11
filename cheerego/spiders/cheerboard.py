from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cheerego.items import CheeregoItem
from datetime import datetime

class CheerboardSpider(BaseSpider):
    name = "cheerboard"
    allowed_domains = ["cheerego.com"]
    start_urls = (
      'http://cheerego.com/dome_web/guest.php',
    )

    def parse(self, response):
      hxs = HtmlXPathSelector(response)
      msg = hxs.select('//div[contains(@class,"reply_content_demo")]/text()').extract()
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
