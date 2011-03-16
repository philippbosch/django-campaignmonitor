# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Recipients'
        db.create_table('campaignmonitor_recipients', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaignmonitor.Campaign'])),
            ('list_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('segment_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal('campaignmonitor', ['Recipients'])


    def backwards(self, orm):
        
        # Deleting model 'Recipients'
        db.delete_table('campaignmonitor_recipients')


    models = {
        'campaignmonitor.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'cm_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'campaignmonitor.list': {
            'Meta': {'object_name': 'List'},
            'cm_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'confirmation_success_page': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'confirmed_opt_in': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unsubscribe_page': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'campaignmonitor.recipients': {
            'Meta': {'object_name': 'Recipients'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaignmonitor.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'segment_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        'campaignmonitor.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'campaignmonitor.subscribercustomfield': {
            'Meta': {'object_name': 'SubscriberCustomField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'custom_fields'", 'to': "orm['campaignmonitor.Subscriber']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['campaignmonitor']
