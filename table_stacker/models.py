# Table biz
import os
import csv
import yaml
from table_fu import TableFu
from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils import simplejson
from django.contrib.sites.models import Site
from managers import TableLiveManager, TableManager

class Table(models.Model):
    """
    Ready-to-serve CSV data.
    """

    # The config
    yaml_name = models.CharField(max_length=100)
    yaml_data = models.TextField(blank=True)

    # required setup
    csv_name = models.CharField(max_length=100)
    slug = models.SlugField()

    # metadata and configuration
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    project_directory = models.TextField(blank=True)
    twitter_share_text = models.TextField(blank=True, null=True)
    allow_others_embed = models.BooleanField(default=True)
    open_about_this_onload = models.BooleanField(default=True)

    # public facing content
    kicker = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500)
    byline = models.CharField(max_length=500, blank=True, null=True)
    credits = models.TextField(blank=True, null=True)
    content_explainer = models.TextField(blank=True, null=True)
    publication_message = models.TextField(blank=True, null=True)
    publication_date = models.DateField()
    publication_time = models.TimeField(blank=True, null=True)
    sources = models.TextField(blank=True, null=True)
    read_more_link = models.TextField(blank=True, null=True)
    footer = models.TextField(blank=True, null=True)

    # table configuration
    is_published = models.BooleanField()
    show_download_links = models.BooleanField(default=True)
    show_in_feeds = models.BooleanField(default=True)
    show_search_field = models.BooleanField(default=True)

    objects = TableManager()
    live = TableLiveManager()

    class Meta:
        ordering = ("-publication_date", "-publication_time")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('table-detail', [self.slug,])

    @models.permalink
    def get_csv_url(self):
        return ('table-csv', [self.slug,])

    @models.permalink
    def get_xls_url(self):
        return ('table-xls', [self.slug,])

    @models.permalink
    def get_json_url(self):
        return ('table-json', [self.slug,])

    def get_share_url(self):
        """
        The link we can use for share buttons.
        """
        site = Site.objects.get_current()
        return 'http://%s%s' % (site.domain, self.get_absolute_url())

    def get_tablefu_opts(self):
        return yaml.load(self.yaml_data).get('column_options', {})

    def get_tablefu(self):
        """
        Trick the data out with TableFu.
        """
        path = os.path.join(settings.CSV_DIR, self.csv_name)
        data = open(path, 'r')
        return TableFu(data, **self.get_tablefu_opts())
    tablefu = property(get_tablefu)

    def get_publication_datetime(self):
        """
        Combine publication date and time where possible.
        """
        if not self.publication_time:
            return datetime(
                self.publication_date.year,
                self.publication_date.month,
                self.publication_date.day,
                0, 0, 0
            )
        else:
            return datetime.combine(
                self.publication_date,
                self.publication_time
            )
    publication_datetime = property(get_publication_datetime)