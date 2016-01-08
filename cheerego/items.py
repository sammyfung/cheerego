#from scrapy.item import Item, Field
from scrapy_djangoitem import DjangoItem
from cheerbook.models import CheerBoard

# class CheeregoItem(Item):
#    scraptime = Field()
#    message = Field()


class CheeregoItem(DjangoItem):
  django_model = CheerBoard 

