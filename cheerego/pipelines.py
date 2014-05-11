from scrapy.exceptions import DropItem
from cheerweb.models import CheerBoard

class CheeregoPipeline(object):
    def process_item(self, item, spider):
        lastid = len(CheerBoard.objects.all())
        if not CheerBoard.objects.filter(id = lastid, message = item['message']):
          item.save()
        else:
          raise DropItem("duplicated message with last message - id %s."% (lastid))
        return item
