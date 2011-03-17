# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'SubscriberCustomField'
        db.delete_table('campaignmonitor_subscribercustomfield')

        # Deleting model 'Subscriber'
        db.delete_table('campaignmonitor_subscriber')

        # Deleting model 'List'
        db.delete_table('campaignmonitor_list')

        # Adding field 'Campaign.status'
        db.add_column('campaignmonitor_campaign', 'status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'SubscriberCustomField'
        db.create_table('campaignmonitor_subscribercustomfield', (
            ('subscriber', self.gf('django.db.models.fields.related.ForeignKey')(related_name='custom_fields', to=orm['campaignmonitor.Subscriber'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('campaignmonitor', ['SubscriberCustomField'])

        # Adding model 'Subscriber'
        db.create_table('campaignmonitor_subscriber', (
            ('state', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('campaignmonitor', ['Subscriber'])

        # Adding model 'List'
        db.create_table('campaignmonitor_list', (
            ('confirmed_opt_in', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cm_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('confirmation_success_page', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unsubscribe_page', self.gf('django.db.models.fields.URLField')(max_length=255)),
        ))
        db.send_create_signal('campaignmonitor', ['List'])

        # Deleting field 'Campaign.status'
        db.delete_column('campaignmonitor_campaign', 'status')


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
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'campaignmonitor.recipients': {
            'Meta': {'object_name': 'Recipients'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaignmonitor.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'segment_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
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
