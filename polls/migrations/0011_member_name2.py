# Generated by Django 3.0.3 on 2020-02-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200228_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='name2',
            field=models.CharField(default='', max_length=60, verbose_name='name'),
        ),
    ]
