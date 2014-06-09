# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'survey_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'survey', ['Survey'])

        # Adding model 'Question'
        db.create_table(u'survey_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'survey', ['Question'])

        # Adding model 'Answers'
        db.create_table(u'survey_answers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'survey', ['Answers'])

        # Adding model 'Users'
        db.create_table(u'survey_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'survey', ['Users'])

        # Adding model 'Results'
        db.create_table(u'survey_results', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'survey', ['Results'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table(u'survey_survey')

        # Deleting model 'Question'
        db.delete_table(u'survey_question')

        # Deleting model 'Answers'
        db.delete_table(u'survey_answers')

        # Deleting model 'Users'
        db.delete_table(u'survey_users')

        # Deleting model 'Results'
        db.delete_table(u'survey_results')


    models = {
        u'survey.answers': {
            'Meta': {'object_name': 'Answers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'survey.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'survey.results': {
            'Meta': {'object_name': 'Results'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'survey.users': {
            'Meta': {'object_name': 'Users'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['survey']