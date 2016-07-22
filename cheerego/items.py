from scrapy_djangoitem import DjangoItem
from cheerbook.models import CheerBoard


class CheeregoItem(DjangoItem):
  django_model = CheerBoard 

