# Generated by Django 3.0.3 on 2020-02-26 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200226_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='date_removed',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_removed',
        ),
    ]
