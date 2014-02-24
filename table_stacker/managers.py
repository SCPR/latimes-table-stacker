from django.db import models
from django.template.defaultfilters import slugify


class TableManager(models.Manager):
    """
    A few tricks we'll use with our tables.
    """
    def live(self):
        """
        Returns only Tables that are ready to publish.
        """
        return self.filter(is_published=True, show_in_feeds=True)

    def update_or_create(self, yaml_data):
        """
        If the Table outlined by the provided YAML file exists, it's updated.

        If it doesn't, it's created.

        Returns a tuple with the object first, and then a boolean that is True
        when the object was created.
        """
        try:
            obj = self.get(slug=yaml_data.get("slug", yaml_data['yaml_name']))
        except self.model.DoesNotExist:
            obj = None

        if obj:
            obj.csv_name=yaml_data['file']
            obj.yaml_name=yaml_data['yaml_name']
            obj.yaml_data=str(yaml_data)
            obj.title=yaml_data['title']
            obj.slug=yaml_data.get("slug", yaml_data['yaml_name'])
            obj.description=yaml_data.get('description', '')
            obj.keywords=yaml_data.get('keywords', '')
            obj.project_directory=yaml_data.get('project_directory', '')
            obj.twitter_share_text=yaml_data.get('twitter_share_text', '')
            obj.allow_others_embed=yaml_data.get("allow_others_embed", False)
            obj.open_about_this_onload=yaml_data.get("open_about_this_onload", False)
            obj.kicker=yaml_data.get('kicker', '')
            obj.byline=yaml_data.get("byline", '')
            obj.credits=yaml_data.get('credits', '')
            obj.content_explainer=yaml_data.get('content_explainer', '')
            obj.publication_message=yaml_data['publication_message']
            obj.publication_date=yaml_data['publication_date']
            obj.publication_time=yaml_data.get("publication_time", None)
            obj.sources=yaml_data.get('sources', '')
            obj.read_more_link=yaml_data.get('read_more_link', '')
            obj.footer=yaml_data.get('footer', '')
            obj.is_published=yaml_data.get('is_published', False)
            obj.show_download_links=yaml_data.get("show_download_links", True)
            obj.show_in_feeds=yaml_data.get("show_in_feeds", True)
            obj.show_search_field=yaml_data.get("show_search_field", True)
            created = False
        else:
            obj = self.create(
                csv_name=yaml_data['file'],
                yaml_name=yaml_data['yaml_name'],
                yaml_data=str(yaml_data),
                title=yaml_data['title'],
                slug=yaml_data.get("slug", yaml_data['yaml_name']),
                description=yaml_data.get('description', ''),
                keywords=yaml_data.get('keywords', ''),
                project_directory=yaml_data.get('project_directory', ''),
                twitter_share_text=yaml_data.get('twitter_share_text', ''),
                allow_others_embed=yaml_data.get("allow_others_embed", False),
                open_about_this_onload=yaml_data.get("open_about_this_onload", False),
                kicker=yaml_data.get('kicker', ''),
                byline=yaml_data.get("byline", ''),
                credits=yaml_data.get('credits', ''),
                content_explainer=yaml_data.get('content_explainer', ''),
                publication_message=yaml_data['publication_message'],
                publication_date=yaml_data['publication_date'],
                publication_time=yaml_data.get("publication_time", None),
                sources=yaml_data.get('sources', ''),
                read_more_link=yaml_data.get('read_more_link', ''),
                footer=yaml_data.get('footer', ''),
                is_published=yaml_data.get('is_published', False),
                show_download_links=yaml_data.get("show_download_links", True),
                show_in_feeds=yaml_data.get("show_in_feeds", True),
                show_search_field=yaml_data.get("show_search_field", True),
            )
            created = True
        obj.save()
        return obj, created

class TableLiveManager(models.Manager):
    """
    Returns only Tables that are ready to publish.
    """
    def get_query_set(self):
        qs = super(TableLiveManager, self).get_query_set()
        return qs.filter(is_published=True, show_in_feeds=True)