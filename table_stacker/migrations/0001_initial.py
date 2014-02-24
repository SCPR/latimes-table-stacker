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
            ('csv_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('yaml_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('yaml_data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('kicker', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('byline', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
            ('publication_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_explainer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('legend', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('footer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('read_more', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sources', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('facebook_share_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('twitter_share_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('embed_share_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('open_about_this', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('credits', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('show_download_links', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_search_field', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_in_feeds', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('table_stacker', ['Table'])


    def backwards(self, orm):
        # Deleting model 'Table'
        db.delete_table('table_stacker_table')


    models = {
        'table_stacker.table': {
            'Meta': {'ordering': "('-publication_date', '-publication_time')", 'object_name': 'Table'},
            'byline': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'content_explainer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credits': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'csv_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'embed_share_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'facebook_share_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'footer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kicker': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'legend': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'open_about_this': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publication_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'read_more': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show_download_links': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_feeds': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_search_field': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sources': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'twitter_share_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'yaml_data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'yaml_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['table_stacker']