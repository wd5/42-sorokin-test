# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'DbEntry.created'
        db.alter_column('core_dbentry', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'DbEntry.created'
        db.alter_column('core_dbentry', 'created', self.gf('django.db.models.fields.DateField')(auto_now_add=True))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.dbentry': {
            'Meta': {'object_name': 'DbEntry'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'presentation': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.requeststore': {
            'Meta': {'ordering': "['-created']", 'object_name': 'RequestStore'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req_cookies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'req_get': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'req_meta': ('django.db.models.fields.TextField', [], {}),
            'req_post': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'req_session': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'req_status_code': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']
