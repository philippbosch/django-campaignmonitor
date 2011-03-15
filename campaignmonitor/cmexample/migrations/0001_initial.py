# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SimpleNewsletter'
        db.create_table('cmexample_simplenewsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cmexample', ['SimpleNewsletter'])


    def backwards(self, orm):
        
        # Deleting model 'SimpleNewsletter'
        db.delete_table('cmexample_simplenewsletter')


    models = {
        'cmexample.simplenewsletter': {
            'Meta': {'object_name': 'SimpleNewsletter'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cmexample']
