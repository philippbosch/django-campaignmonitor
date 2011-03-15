# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Subscriber'
        db.create_table('campaignmonitor_subscriber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('campaignmonitor', ['Subscriber'])

        # Adding model 'SubscriberCustomField'
        db.create_table('campaignmonitor_subscribercustomfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscriber', self.gf('django.db.models.fields.related.ForeignKey')(related_name='custom_fields', to=orm['campaignmonitor.Subscriber'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('campaignmonitor', ['SubscriberCustomField'])

        # Adding model 'Campaign'
        db.create_table('campaignmonitor_campaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cm_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('html_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('text_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('campaignmonitor', ['Campaign'])

        # Adding model 'List'
        db.create_table('campaignmonitor_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cm_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('unsubscribe_page', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('confirmed_opt_in', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('confirmation_success_page', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('campaignmonitor', ['List'])


    def backwards(self, orm):
        
        # Deleting model 'Subscriber'
        db.delete_table('campaignmonitor_subscriber')

        # Deleting model 'SubscriberCustomField'
        db.delete_table('campaignmonitor_subscribercustomfield')

        # Deleting model 'Campaign'
        db.delete_table('campaignmonitor_campaign')

        # Deleting model 'List'
        db.delete_table('campaignmonitor_list')


    models = {
        'campaignmonitor.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'cm_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
