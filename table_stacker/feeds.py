from datetime import datetime
from table_stacker.models import Table
from django.contrib.syndication.feeds import Feed


class LatestTables(Feed):
    title = "Latest spreadsheets"
    link = "/feeds/latest/"
    description = "The latest spreadsheets"
    title_template = "feeds/table_title.html"
    description_template = "feeds/table_description.html"
    
    def items(self):
        qs = Table.objects.all().filter(is_published=True, show_in_feeds=True)
        return qs.order_by("-publication_date")[:10]
    
    def item_pubdate(self, item):
        return datetime(*(item.publication_date.timetuple()[:6]))