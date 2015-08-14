# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'requests_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'requests', ['User'])

        # Adding model 'Request'
        db.create_table(u'requests_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['requests.User'])),
            ('request_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('days', self.gf('django.db.models.fields.IntegerField')()),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'requests', ['Request'])

        # Adding model 'Vacation'
        db.create_table(u'requests_vacation', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['requests.User'], unique=True, primary_key=True)),
            ('days', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('days_total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'requests', ['Vacation'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'requests_user')

        # Deleting model 'Request'
        db.delete_table(u'requests_request')

        # Deleting model 'Vacation'
        db.delete_table(u'requests_vacation')


    models = {
        u'requests.request': {
            'Meta': {'object_name': 'Request'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'days': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {}),
            'request_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['requests.User']"})
        },
        u'requests.user': {
            'Meta': {'object_name': 'User'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'requests.vacation': {
            'Meta': {'object_name': 'Vacation'},
            'days': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'days_total': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['requests.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['requests']