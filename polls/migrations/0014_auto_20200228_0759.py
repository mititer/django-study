# Generated by Django 3.0.3 on 2020-02-27 23:59

from django.db import migrations
from polls.models import MemberType
from django.utils.translation import gettext_lazy as _


def initalize_member_type(apps, schema_editor):
    member_list = apps.get_model('polls', 'Member')

    MemberType(name=_('member level 1')).save()
    MemberType(name=_('member level 2')).save()
    MemberType(name=_('member level 3')).save()


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200228_0748'),
    ]

    operations = [
        migrations.RunPython(initalize_member_type),
    ]