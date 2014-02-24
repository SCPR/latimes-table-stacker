# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Table'
        db.create_table('table_stacker_table', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('yaml_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('yaml_data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('csv_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project_directory', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('twitter_share_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('allow_others_embed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('open_about_this_onload', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('kicker', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('credits', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_explainer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publication_message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
            ('publication_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('sources', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('read_more_link', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_download_links', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_in_feeds', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_search_field', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('table_stacker', ['Table'])


    def backwards(self, orm):
        # Deleting model 'Table'
        db.delete_table('table_stacker_table')


    models = {
        'table_stacker.table': {
            'Meta': {'ordering': "('-publication_date', '-publication_time')", 'object_name': 'Table'},
            'allow_others_embed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'content_explainer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'credits': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'csv_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'kicker': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'open_about_this_onload': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'project_directory': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publication_message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publication_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'read_more_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'show_download_links': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_feeds': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_search_field': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sources': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'twitter_share_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'yaml_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'yaml_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['table_stacker']