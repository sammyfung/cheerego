from scrapy.exceptions import DropItem
from cheerbook.models import CheerBoard


class CheeregoPipeline(object):
    def process_item(self, item, spider):
        last_msg = CheerBoard.objects.all().order_by("-pk")[0]
        if item['message'] != last_msg.message:
            item.save()
        else:
            raise DropItem("duplicated message with last message - id %s."% (lastid))
