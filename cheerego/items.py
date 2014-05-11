from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from cheerweb.models import CheerBoard

#class CheeregoItem(Item):
#    scraptime = Field()
#    message = Field()

class CheeregoItem(DjangoItem):
  django_model = CheerBoard 

